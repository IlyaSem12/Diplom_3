import allure
import pytest
from conftest import *
from config import *
from locators.main_page_locators import *
from locators.feed_page_locators import *

@allure.epic("Главная страница")
@allure.tag('main page')
@pytest.mark.gui
class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_main_page_click_constructor_link_redirect_main_page(self, profile_page):
        '''Тест проверяет корректность работы кнопки "Конструктор".  
        Редирект на странцу главную страницу при нажатии на кнопку "Конструктор"'''
        page = profile_page
        page.click_constructor_link()
        with allure.step(f"Проверяем редирект на '{BASE_URL}'"):
            assert page.is_visible(BURGER_TITLE), f'Страница "{BASE_URL}" не открылась'
    
    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_main_page_click_feed_link_redirect_feed_page(self, main_page):
        '''Тест проверяет корректность работы кнопки "Лента заказов".  
        Редирект на странцу заказов при нажатии на кнопку "Лента заказов"'''
        page = main_page
        page.click_order_feed_link()
        with allure.step(f"Проверяем редирект на '{FEED_URL}'"):
            assert page.is_visible(ORDER_FEED_TITLE), f'Страница "{FEED_URL}" не открылась'

    @allure.title('Проверка всплывающего окна с деталями ингридиента')
    def test_main_page_click_ingridient_card_open_modal_card(self, main_page):
        '''Тест проверяет наличие всплывающего окна с деталями ингридиент."'''
        page = main_page
        page.click_first_card_bun_link()
        with allure.step(f"Проверяем наличие всплывающего окна с деталями ингридиента"):
            assert page.is_visible(MODAL_CONTENT), f'Всплывающего окна с деталями ингридиента не открылось'
            assert page.is_visible(MODAL_TITLE), f'Данные в всплывающем окне не появились'
    
    @allure.title('Проверка закрытия всплывающего окна крестиком')
    def test_main_page_click_close_button_modal_card_close(self, main_page):
        '''Тест проверяет корректность работы кнопки "Закрыть" у всплывающего окна с деталями ингридинта."'''
        page = main_page
        page.click_first_card_bun_link()
        with allure.step(f"Проверяем наличие всплывающего окна с деталями ингридиента"):
            assert page.is_visible(MODAL_CONTENT), f'Всплывающего окна с деталями ингридиента не открылось'
        with allure.step(f"Проверяем возможность закрыть модальное окно"):
            page.click_modal_close_button()
            assert page.is_not_visible(MODAL), f'Всплывающее окно деталями ингридиента не было закрыто'
    
    @allure.title('Проверка счетчика ингредиента')
    def test_main_page_constructor_add_ingridient_increasing_counter_ingridient(self, main_page):
        '''Тест проверяет корректность счетчика ингредиента.  
        при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента'''
        page = main_page
        page.drag_bun_to_constructor()
        with allure.step('Проверяем, что булка появилась в конструкторе'):
            assert page.is_visible(BUN_IN_CONSTRUCTOR, 5), 'Булка не появилась в конструкторе'
        with allure.step('Проверяем, что счётчик булки увеличился до 2'):
            assert page.get_bun_counter() == "2", f"Счётчик булки не равен 2. Текущее значение: {page.get_bun_counter()}"

    @allure.title('Проверка создание заказа авториованным пользователем')
    def test_main_page_create_order_open_modal_card(self, main_page):
        '''Тест проверяет корректность счетчика ингредиента.  
        при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента'''
        page = main_page
        page.drag_bun_to_constructor()
        with allure.step('Проверяем, что булка появилась в конструкторе'):
            assert page.is_visible(BUN_IN_CONSTRUCTOR, 5), 'Булка не появилась в конструкторе'
        with allure.step('Проверяем, что заказ был создан'):
            page.click_order_button()
            assert page.is_visible(MODAL_CONTENT), f'Всплывающее окно с индификатором заказа не появилось'
            assert page.is_visible(CREATED_ORDER_NUMBER), f'Данные в всплывающем окне не появились'
    
    