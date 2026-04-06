import allure
import uuid
import random
import string
from config import *


@allure.step('Генерируем логин')
def generate_email() -> str:
    """Функция для генерации email"""
    return f"{uuid.uuid4().hex[:8]}@email.ru"

@allure.step('Генерируем пароль')
def generate_password() -> str:
    """Функция для генерации пароля"""
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(8))
    return random_string

@allure.step('Генерируем логин')
def generate_login() -> str:
    """Функция для генерации логина"""
    return f"test_{uuid.uuid4().hex[:8]}"

def registration_new_user_and_return_login_password(api) -> dict:
    """Функция для регистрации пользователя"""
    with allure.step(f'Регистрируем пользоваетля'):
        login_pass = {}
        payload = {
            "email":generate_email(),
            "password":generate_password(),
            "name":generate_login()
        }# собираем тело запроса
        # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
        with allure.step('Отправляем POST запрос для регистрации пользователя'):
            response = api.post(path = REGISTRATION_API_URL, json = payload)
        if response.status_code == 200:
            body = response.json()
            login_pass["accessToken"] = body.get("accessToken")
            login_pass["refreshToken"] = body.get("refreshToken")
        return login_pass

def delete_user_by_token(api, token:str) -> None:
    with allure.step(f'Удляем пользователя'):
        api.delete(path = USER_API_URL, headers={"Authorization": token})

def get_total_order(api):
    with allure.step(f'Получаем общее колличество заказов'):
        count_order = {}
        response = api.get(path = ALL_API_ORDERS_URL)
        count_order["totalOrder"] = response.json().get("total")
        count_order["totalToday"] = response.json().get("totalToday")
    return count_order
