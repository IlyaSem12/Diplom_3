from selenium.webdriver.common.by import By

# ====== ЗАГОЛОВОК СТРАНИЦЫ ======
BURGER_TITLE = (By.XPATH, "//section//h1")
# ====== МОДАЛЬНОЕ ОКНО ======
MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal']")
MODAL_CONTENT = (By.CSS_SELECTOR, "section[class*='Modal_modal'] div[class*='contentBox']")
CREATED_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'text_type_digits-large')]")
# ====== ЗАГОЛОВОК ======
MODAL_TITLE = (By.XPATH, "//section[contains(@class, 'Modal_modal')]//h2")
# ====== КНОПКА ЗАКРЫТИЯ МОДАЛЬНОГО ОКНА ======
MODAL_CLOSE_BUTTON = (By.XPATH, "//section//button[@type='button']")
# ====== ПЕРВЫЕ КАРТОЧКИ В КАТЕГОРИЯХ ======
FIRST_BUN_CARD = (By.XPATH, "//section//h2[1]/following-sibling::ul[1]/a[1]")
# ====== ЭЛЕМЕНТЫ КАРТОЧКИ ======
INGREDIENT_COUNTERS = (By.XPATH, "//section//a[contains(@href, '/ingredient/')]//div[p]")
# ====== ОСНОВНОЙ БЛОК КОНСТРУКИТОРА ======
BURGER_CONSTRUCTOR = (By.XPATH,"//section[contains(@class,'BurgerConstructor_basket')]")
BUN_IN_CONSTRUCTOR = (By.XPATH,"//img[contains(@alt,'Флюоресцентная булка R2-D3')]")
ORDER_BUTTON = (By.XPATH,"//button[.//text()[contains(.,'Оформить заказ')]]")