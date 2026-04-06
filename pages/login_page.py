#./pages/login_page.py
import allure
from locators.login_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from config import *
from helpers import *

class LoginPage(BasePage):
    
    @allure.step('Ожидаем загрузку формы "Вход"')
    def wait_for_load_login_form(self):
        self.wait_visible(LOGIN_FORM, 5)
    
    @allure.step('Нажимаем на ссылку "Восстановить пароль"')
    def click_herf_forgot_password(self):
        self.click(FORGOT_PASSWORD_LINK)
    

