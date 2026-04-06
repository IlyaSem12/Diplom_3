from selenium.webdriver.common.by import By


# ====== ОСНОВНОЙ КОНТЕЙНЕР ПРОФИЛЯ ======
PROFILE_CONTENT = (By.XPATH, "//main//div[.//ul and .//input]")
# ====== НАВИГАЦИЯ ======
PROFILE_LINK = (By.XPATH, "//nav//a[contains(@href, '/account/profile')]")
ORDER_HISTORY_LINK = (By.XPATH, "//nav//a[contains(@href, '/account/order-history')]")
LOGOUT_BUTTON = (By.XPATH, "//nav//button[@type='button']")
ORDER_CARDS = (By.XPATH,"//ul//a[contains(@href, '/order-history/')]")
FIRST_ORDER_CARD = (By.XPATH,"(//ul//a[contains(@href, '/order-history/')])[1]")
FIRST_ORDER_NUMBER = (By.XPATH,"(//ul//a[contains(@href, '/order-history/')]//p[starts-with(text(), '#')])[1]")