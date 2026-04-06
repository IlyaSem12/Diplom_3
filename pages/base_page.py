#./pages/base_page.py
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from locators.password_recovery_page_locators import *
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from config import *


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url: str):
        '''Метод открытия страницы'''
        self.browser.get(url)

    def find(self, locator):
        """Метод поиска списка элементов"""
        return self.browser.find_elements(*locator)

    def wait_visible(self, locator, timeout: int = 10):
        '''Метод ожидания появления элемента'''
        return WebDriverWait(self.browser, timeout).until(expected_conditions.visibility_of_element_located(locator))
    
    def wait_invisible(self, locator, timeout: int = 10):
        '''Метод ожидает что элемент исчез'''
        return WebDriverWait(self.browser, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def wait_field_active(self,locator, color, timeout=10):
        """Метод ожидает пока поле станет активным"""
        return WebDriverWait(self.browser, timeout).until(
            lambda d: d.find_element(*locator).value_of_css_property("border-color") == color)
    
    def wait_for_order_number_not_placeholder(self, locator, placeholder, timeout=10):
        """Метод ожидает пока номер заказа перестанет быть равен placeholder"""
        return WebDriverWait(self.browser, timeout).until(lambda d: d.find_element(*locator).text.strip() != placeholder)

    def wait_until_element_appear(self, locator, message: str, timeout:int = 5):
        """Метод ожидает пока элемент пререстанет быть перестанет быть равен message"""
        WebDriverWait(self.browser, timeout).until(lambda d: message not in d.find_element(*locator).text)
    
    def is_visible(self, locator, timeout: int = 10) -> bool:
        '''Метод проверяет, что элемент появился'''
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_not_visible(self, locator, timeout: int = 10) -> bool:
        """Метод проверяет, что элемент исчез или стал невидимым"""
        try:
            self.wait_invisible(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_active_border(self, locator, color, timeout: int = 10) -> bool:
        """Проверяет, что у элемента появилась активная рамка"""
        try:
            self.wait_field_active(locator,color, timeout)
            return True
        except TimeoutException:
            return False
    
    def click(self, locator, timeout: int = 10):
        '''Метод для нажатия по элементу'''
        element = WebDriverWait(self.browser, timeout).until(expected_conditions.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.browser.execute_script("arguments[0].click();", element)
    
    def get_text(self,locator, timeout: int = 10):
        '''Метод полчения текста элемента '''
        return self.wait_visible(locator, timeout).text.strip()
    
    def send_text(self, locator, text, timeout: int = 10):
        '''Метод вставки текста в поле ввода'''
        self.wait_visible(locator, timeout).send_keys(text)
    
    def get_current_url(self):
        '''Метод для получения текучшего url'''
        return self.browser.current_url
    
    def drag_and_drop_by_offset(self, source_locator, target_locator):
        """Метод перетаскивает элемент в целевую зону через click_and_hold"""
        source =  self.wait_visible(source_locator)
        target = self.wait_visible(target_locator)
        #для "firefox" не работает click_and_hold поэтому применен скрипт
        if self.browser.capabilities.get("browserName") == "firefox":
            self.browser.execute_script(SCRIPT_DARG_AND_DROP, source, target)
        else:
            actions = ActionChains(self.browser)
            actions.click_and_hold(source).move_to_element(target).pause(0.5).release().perform()