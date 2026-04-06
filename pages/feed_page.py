#./pages/feed_page.py
import allure
from locators.feed_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from config import *
from selenium.webdriver.common.action_chains import ActionChains

class FeedPage(BasePage):
    
    @allure.step('Ожидаем загрузку заголовка "Лента заказов"')
    def wait_for_order_feed_title(self):
        self.wait_visible(ORDER_FEED_TITLE, 10)
    
    @allure.step('Ожидаем когда загрузятся заказы "В работе"')
    def wait_for_today_order(self):
        self.wait_visible(TODAY_DONE_VALUE, 10)
    
    @allure.step('Кликаем по первому заказу в ленте')
    def click_first_order(self):
        self.click(FIRST_ORDER_CARD)
    
    @allure.step('Открываем страницу со всем заказами')
    def open_feed_page(self):
        self.open(FEED_URL)
    
    @allure.step('Ожидаем открытие модального окна')
    def wait_order_modal(self):
        self.wait_visible(ORDER_MODAL)

    @allure.step('Получаем номера всех заказов')
    def get_all_order_numbers(self):
        elements = self.find(ORDER_NUMBERS)
        return [el.text.strip().replace('#', '') for el in elements]

    @allure.step('Получаем колличество всех заказов')
    def get_total_done_value(self):
        return int(self.get_text(TOTAL_DONE_VALUE))

    @allure.step('Получаем колличество сегодгяшних заказов')
    def get_today_done_value(self):
        return int(self.get_text(TODAY_DONE_VALUE))

    @allure.step('Получаем заказы "В работе"')
    def get_orders_in_progress(self):
        elements = self.find(IN_PROGRESS_ORDERS)
        return [int(el.text.strip().replace('#', '')) for el in elements]

    @allure.step('Ожидаем когда загрузятся заказы "В работе"')
    def wait_until_orders_appear(self):
        return self.wait_until_element_appear(IN_PROGRESS_ORDERS, MESSAGE_IN_PROGGERSS_ORDERS)