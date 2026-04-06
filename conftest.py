import pytest
import allure
from config import *
from utils.webdriver_factory import BrowserFactory
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from locators.common_locators import *
from utils.api_client import ApiClient
from helpers import *


@pytest.fixture(params = ['chrome', 'firefox'])
def browser(request):
    '''Фикструа для получения инстанса драйвера'''
    with allure.step("Окрываем браузер"):
        driver = BrowserFactory.get_driver(request.param)
    yield driver
    with allure.step("Закрываем браузер"):
        driver.quit()

@pytest.fixture
def api():
    """Фикстура для создания объекта класса ApiClient"""
    with allure.step('Открываем сессию api'):
        client = ApiClient()
    yield client
    with allure.step('Закрываем сессию api'):
        client.close()

@pytest.fixture()
def registration_user(api):
    """Фикстура для регистрации пользователя и удаления его после теста"""
    user = registration_new_user_and_return_login_password(api)
    yield user
    token = user.get("token")
    if token:
        delete_user_by_token(api, token)

@pytest.fixture()
def total_order(api):
    """Фикстура для получения колличества заказов"""
    total_order = get_total_order(api)
    return total_order

@pytest.fixture()
def authorized_browser(browser, registration_user):
    browser.get(BASE_URL)
    browser.execute_script(
        """
        window.localStorage.setItem('accessToken', arguments[0]);
        window.localStorage.setItem('refreshToken', arguments[1]);
        """,
        registration_user['accessToken'],
        registration_user['refreshToken']
    )

@pytest.fixture()
def main_page(browser, authorized_browser):
    """Фикстура для создания объекта класса страницы авторизации"""
    #Создаем объект класса MainPage
    page = MainPage(browser)
    page.open(BASE_URL) #переходим по ссылке
    #добавляем явное ожиданяие для прогрузки страницы
    page.wait_for_load_burger_titel()
    return page

@pytest.fixture()
def login_page(browser):
    """Фикстура для создания объекта класса страницы авторизации"""
    #Создаем объект класса LoginPage
    page = LoginPage(browser)
    page.open(LOGIN_URL) #переходим по ссылке
    #добавляем явное ожиданяие для прогрузки страницы
    page.wait_for_load_login_form()
    return page

@pytest.fixture()
def password_recovery_page(browser):
    """Фикстура для создания объекта класса страницы авторизации"""
    #Создаем объект класса PasswordRecoveryPage
    page = PasswordRecoveryPage(browser)
    page.open(PASSWORD_RECOVERY_URL) #переходим по ссылке
    #добавляем явное ожиданяие для прогрузки страницы
    page.wait_for_load_password_recovery_form()
    return page

@pytest.fixture()
def profile_page(browser, authorized_browser):
    """Фикстура для создания объекта класса страницы профиля"""
    #Создаем объект класса ProfilePage
    page = ProfilePage(browser)
    #Решение ниже было сделанно так потому что на сайте баг, при котором когда на прямую заходишь по ссылке залогиненым пользователем, открывается статичный белый экран(открывается только если нажать на кнопку 'Личный кабинет')
    page.click(ACCOUNT_LINK)
    #добавляем явное ожиданяие для прогрузки страницы
    page.wait_for_load_profile_content()
    return page

@pytest.fixture()
def feed_page(browser):
    """Фикстура для создания объекта класса FeedPag"""
    #Создаем объект класса FeedPag
    page = FeedPage(browser)
    return page

@pytest.fixture()
def created_order(main_page):
    page = main_page
    page.drag_bun_to_constructor()
    page.click_order_button()
    page.wait_for_load_model_order()
    page.wait_for_load_model_order_number()
    order_number = page.get_created_order_number()
    page.click_modal_close_button()
    return order_number