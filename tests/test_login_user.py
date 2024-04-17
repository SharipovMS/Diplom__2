import requests
from data_for_tests.data import DataForTest
from urls.urls import Urls
import allure


class TestLoginUser:

    @allure.title('Успешный логин пользователя в системе')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_login_success(self):
        req_login_user_seccess = requests.post(Urls.user_login, data=DataForTest.static_user)
        assert req_login_user_seccess.status_code == 200 and req_login_user_seccess.json()['success'] == True

    @allure.title('Логин пользователя в системе с ошибкой при заполнении полей')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_incorrect_field(self):
        req_login_user_incorrect_field = requests.post(Urls.user_login, data=DataForTest.incorrect_user)
        assert req_login_user_incorrect_field.status_code == 401 and req_login_user_incorrect_field.json()['message'] == 'email or password are incorrect'

