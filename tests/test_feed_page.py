import allure
import pytest
from conftest import *
from config import *
from locators.main_page_locators import *
from locators.feed_page_locators import *

@allure.epic("Страница ленты заказов")
@allure.tag('feet page')
@pytest.mark.gui
class TestFeetPage:
    
    @allure.title("Проверка что клик по заказу в ленте открывает модальное окно с деталями")
    def test_feed_page_click_order_opens_order_details_modal(self, feed_page):
        page = feed_page
        page.open_feed_page()
        page.click_first_order()
        with allure.step("Проверяем, что открылось модальное окно"):
            page.wait_order_modal()
            assert page.is_visible(ORDER_MODAL), "Модальное окно с деталями заказа не открылось"
    
    @allure.title("Проверка что заказ из истории заказов пользователя отображается в ленте заказов")
    def test_feed_page_user_order_from_history_is_displayed_in_feed(self,browser,created_order, profile_page, feed_page):
        profile = profile_page
        with allure.step("Открываем историю заказов пользователя"):
            profile.click_order_history_link()
            profile.wait_for_order_history()
            user_order_number = profile.get_first_history_order_number()
        feed = feed_page
        with allure.step("Получаем номера заказов из ленты"):
            feed.open(FEED_URL)
            feed.wait_for_order_feed_title()
            feed_numbers = feed.get_all_order_numbers()
        with allure.step("Проверяем, что заказ пользователя есть в ленте"):
            assert user_order_number in feed_numbers, f"Заказ пользователя {user_order_number} не найден в ленте заказов"

    @pytest.mark.parametrize('type_counter,method, message',[ 
        pytest.param('totalOrder','get_total_done_value','Выполнено за всё время', id='total_order'), 
        pytest.param('totalToday','get_today_done_value','Выполнено за сегодня', id='total_order_today'), 
        ]
    )
    def test_feed_page_create_order_increases_total_done_counter(self,total_order,created_order, feed_page, type_counter,method, message):
        allure.dynamic.title(f"Проверка что после создания заказа счётчик '{message}' увеличивается")
        feed = feed_page
        with allure.step(f"Сохраняем текущее значение счётчика '{message}'"):
            before_value = total_order[type_counter]
        with allure.step("Обновляем ленту и получаем новое значение счётчика"):
            feed.open_feed_page()
            feed.wait_until_orders_appear()
            after_value = getattr(feed, method)()
        with allure.step("Проверяем увеличение счётчика"):
            assert after_value > before_value, f"Счётчик не увеличился. Было: {before_value}, стало: {after_value}"
        
    @allure.title("Проверка что после создания заказа его номер появляется в разделе 'В работе'")
    def test_feed_page_created_order_number_appears_in_progress_section(self, created_order, feed_page):
        feed = feed_page
        with allure.step("Создаём заказ и сохраняем его номер"):
            created_order_number = created_order.strip()
        feed.open_feed_page()
        feed.wait_for_order_feed_title()
        feed.wait_until_orders_appear()
        in_progress_numbers = feed.get_orders_in_progress()
        with allure.step("Проверяем, что номер заказа появился в разделе 'В работе'"):
            assert int(created_order_number) in in_progress_numbers, f"Номер заказа {created_order_number} не найден в разделе 'В работе'"