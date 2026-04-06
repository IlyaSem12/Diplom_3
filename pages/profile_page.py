import allure
from locators.profile_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from config import *
from helpers import *


class ProfilePage(BasePage):
    
    @allure.step('Ожидаем загрузку профиля')
    def wait_for_load_profile_content(self):
        self.wait_visible(PROFILE_CONTENT, 5)
    
    @allure.step('Нажимаем на кнопку "История заказов"')
    def click_order_history_link(self):
        self.click(ORDER_HISTORY_LINK)

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_logout_link(self):
        self.click(LOGOUT_BUTTON)
    
    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_constructor_link(self):
        self.click(CONSTRUCTOR_LINK)
    
    @allure.step('Ожидаем загрузку заказов')
    def wait_for_order_history(self):
        self.wait_visible(ORDER_CARDS, 10)
    
    @allure.step('Получаем номер первого заказа')
    def get_first_history_order_number(self):
        return self.get_text(FIRST_ORDER_NUMBER).strip().replace('#', '')