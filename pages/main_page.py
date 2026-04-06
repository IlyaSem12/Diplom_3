#./pages/main_page.py
import allure
from locators.main_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from config import *

class MainPage(BasePage):
    
    @allure.step('Ожидаем загрузку заголовка "Соберите бургер"')
    def wait_for_load_burger_titel(self):
        self.wait_visible(BURGER_TITLE, 5)
    
    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_personal_account_button(self):
        self.click(ACCOUNT_LINK)
    
    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_order_feed_link(self):
        self.click(ORDER_FEED_LINK)
    
    @allure.step('Нажимаем на первую карточку булочки')
    def click_first_card_bun_link(self):
        self.click(FIRST_BUN_CARD)
    
    @allure.step('Нажимаем на кнопку закрытия модального окна')
    def click_modal_close_button(self):
        self.click(MODAL_CLOSE_BUTTON)
    
    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click(ORDER_BUTTON)
    
    @allure.step('Перетаскиваем булку в конструктор')
    def drag_bun_to_constructor(self):
        self.drag_and_drop_by_offset(FIRST_BUN_CARD, BURGER_CONSTRUCTOR)
    
    @allure.step('Ожидаем модальное окно заказа')
    def wait_for_load_model_order(self):
        self.wait_visible(MODAL_CONTENT)

    @allure.step('Ожидаем номер заказа')
    def wait_for_load_model_order_number(self):
        self.wait_for_order_number_not_placeholder(CREATED_ORDER_NUMBER, PLACEHOLDER_NUMBER)
    
    @allure.step('Получаем номер закзаа')
    def get_created_order_number(self):
        return self.get_text(CREATED_ORDER_NUMBER)

    @allure.step('Получаем значение счётчика булки')
    def get_bun_counter(self):
        return self.get_text(INGREDIENT_COUNTERS)