from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class BrowserFactory:
    @staticmethod
    def get_driver(browser_name: str, headless: bool = False):
        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            if headless:
                options.add_argument("--headless")
            return webdriver.Chrome(options=options)
        elif browser_name.lower() == 'firefox':
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Браузер {browser_name} не поддерживается.")