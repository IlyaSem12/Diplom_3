from selenium.webdriver.common.by import By


ORDER_FEED_TITLE = (By.CSS_SELECTOR, "main h1")
ORDER_NUMBERS = (By.XPATH, "//a[contains(@href, '/feed/')]//p[starts-with(text(), '#')]")
FIRST_ORDER_CARD = (By.XPATH, "(//a[contains(@href, '/feed/')])[1]")
TOTAL_DONE_VALUE = (By.XPATH, "(//p[contains(@class,'text_type_digits-large')])[1]")
TODAY_DONE_VALUE = (By.XPATH, "(//p[contains(@class,'text_type_digits-large')])[2]")
ORDER_MODAL = (By.XPATH,"//div[.//p[contains(text(), '#')]]")
ORDER_MODAL_NUMBER =  (By.XPATH,"//div//p[starts-with(normalize-space(), '#')]")
IN_PROGRESS_ORDERS = (By.XPATH,"(//ul[contains(@class,'OrderFeed_orderList')])[2]//li")
