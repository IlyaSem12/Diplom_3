from selenium.webdriver.common.by import By


# ====== ФОРМА ВОССТАНОВЛЕНИЯ ======
# Контейнер формы
FORGOT_PASSWORD_FORM = (By.XPATH, "//form")
# ====== ЗАГОЛОВОК ======
# Заголовок "Восстановление пароля"
FORGOT_PASSWORD_TITLE = (By.XPATH,"//form/preceding-sibling::h2")
# ====== ПОЛЕ ВВОДА ======
#  через label 
EMAIL_INPUT = (By.XPATH,"//form//input[@type='text']")
# Поле нового пароля
NEW_PASSWORD_INPUT = (By.XPATH,"//form//input[@type='password']")
PASSWORD_FIELD_CONTAINER = ( By.XPATH, "//input[@name='Введите новый пароль']/parent::div" )
# Поле кода
CODE_INPUT = (By.XPATH,"//form//input[@type='password']/following::input[@type='text'][1]")
# ====== КНОПКА ======
# Кнопка "Восстановить"
RECOVER_BUTTON = (By.XPATH,"//form//button")
PASSWORD_VISIBILITY_ICON = (By.XPATH,"//input[@type='password']/following-sibling::div[contains(@class, 'input__icon')]")
