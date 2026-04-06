import allure
from locators.password_recovery_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from config import *
from helpers import *


class PasswordRecoveryPage(BasePage):
    
    @allure.step('Ожидаем загрузку формы "Восстановления пароля"')
    def wait_for_load_password_recovery_form(self):
        self.wait_visible(FORGOT_PASSWORD_FORM, 5)
    
    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_recover_button(self):
        self.click(RECOVER_BUTTON)
    
    @allure.step('Заполняем поле email"')
    def fill_email(self):
        email = generate_email()
        self.send_text(EMAIL_INPUT, email)

    @allure.step('Нажимаем кнопку "Показать/скрыть пароль"')
    def click_password_visibility_icon(self):
        self.click(PASSWORD_VISIBILITY_ICON)
