from selenium.webdriver.common.by import By


# ======ФОРМА ЛОГИНА======
# Контейнер формы
LOGIN_FORM = (By.XPATH, "//form")
# ======ПОЛЯ ВВОДА======
# Поле Email 
EMAIL_INPUT = (By.XPATH,"//form//input[@type='text']")
# Поле Пароль
PASSWORD_INPUT = (By.XPATH, "//form//input[@type='password']")
# ======КНОПКА======
# Кнопка "Войти"
LOGIN_BUTTON = (By.XPATH,"//form//button")
# ====== ССЫЛКИ ======
# Ссылка "Зарегистрироваться"
REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
# Ссылка "Восстановить пароль"
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")
# ======ЗАГОЛОВОК======
# Заголовок страницы "Вход"
LOGIN_TITLE = (By.XPATH, "//form/preceding-sibling::h2")
