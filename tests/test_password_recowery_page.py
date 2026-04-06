import allure
import pytest
from conftest import *
from config import *
from locators.password_recovery_page_locators import *


@allure.epic("Cтраница восстановления пароля")
@allure.tag('password redcovery page')
@pytest.mark.gui
class TestPasswordRecoveryPage:
    
    @allure.title('Проверка редиректа по кнопке «Восстановить пароль»')
    def test_password_recovery_page_click_forgot_password_link_redirect_password_recovery_page(self, login_page):
        '''Тест проверяет корректность работы кнопки "Восстановить пароль" на старнице авторизации.  
        Редирект на странцу восстановления пароля при нажатии на кнопку "Восстановить пароль"'''
        page = login_page
        page.click_herf_forgot_password()
        with allure.step(f"Проверяем редирект на '{PASSWORD_RECOVERY_URL}'"):
            assert page.get_current_url() == PASSWORD_RECOVERY_URL , f'Страница "{PASSWORD_RECOVERY_URL}" не открылась'

    @allure.title('Проверка кнопки «Восстановить»')
    def test_password_recovery_page_click_recover_button_view_password_recovery_form(self, password_recovery_page):
        """Тест проверяет, что после ввода email и нажатия кнопки 'Восстановить'
        появляется форма ввода нового пароля и кода из письма
        """
        page = password_recovery_page
        page.fill_email()
        page.click_recover_button()
        page.wait_for_load_password_recovery_form()
        with allure.step("Проверяем появление полей"):
            assert page.is_visible(NEW_PASSWORD_INPUT, 5), "Поле 'Пароль' не появилось"
            assert page.is_visible(CODE_INPUT, 5), "Поле 'Введите код из письма' не появилось"
    
    @allure.title('Проверка поле "Пароль" становится активным при клике на иконку видимости')
    def test_password_recovery_page_click_password_visibility_icon_shows_purple_password_field_borders(self, password_recovery_page):
        """Тест проверяет, что после клика по иконке видимости пароля поле становится активным"""
        page = password_recovery_page
        page.click_recover_button()
        page.wait_for_load_password_recovery_form()
        page.click_password_visibility_icon()
        with allure.step("Проверяем что поле стало активным"):
            assert page.is_active_border(PASSWORD_FIELD_CONTAINER, PASSWORD_FIELD_BORDERS), "Обводка не появилась, поле не было активировано"