import allure
import pytest
from conftest import *
from config import *
from locators.login_page_locators import *

@allure.epic("Cтраница личного кабинета")
@allure.tag('profile page')
@pytest.mark.gui
class TestPasswordRecoveryPage:
    
    @allure.title('Проверка редиректа по кнопке «Личный кабинет»')
    def test_profile_page_click_personal_account_link_redirect_profile_page(self, main_page):
        '''Тест проверяет корректность работы кнопки "Личный кабинет".  
        Редирект на странцу профиля при нажатии на кнопку "Личный кабинет"'''
        page = main_page
        page.click_personal_account_button()
        with allure.step(f"Проверяем редирект на '{PROFILE_URL}'"):
            assert page.get_current_url() ==  PROFILE_URL , f'Страница "{PROFILE_URL}" не открылась'
    
    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_profile_page_click_order_history_link_redirect_order_history_page(self, profile_page):
        '''Тест проверяет корректность работы кнопки "История заказов".  
        Редирект на странцу профиля при нажатии на кнопку "История заказов"'''
        page = profile_page
        page.click_order_history_link()
        with allure.step(f"Проверяем редирект на '{ORDER_HISTORY_URL}'"):
            assert page.get_current_url() ==  ORDER_HISTORY_URL , f'Страница "{ORDER_HISTORY_URL}" не открылась'
    
    @allure.title('Проверка выхода из профиля')
    def test_profile_page_logout_link_redirect_login_page(self, profile_page):
        '''Тест проверяет корректность работы кнопки "Выход".  
        Редирект на странцу авторизации при нажатии на кнопку "Выход"'''
        page = profile_page
        page.click_logout_link()
        with allure.step(f"Проверяем редирект на '{LOGIN_URL}'"):
            assert page.is_visible(LOGIN_FORM), f'Страница "{LOGIN_URL}" не открылась'
    