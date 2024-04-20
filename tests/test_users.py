import requests
from data_for_tests.data import DataForTest
from urls.urls import Urls
import allure

class TestCreateUser:

    @allure.title('Создание пользователя.')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_create_unique_user(self, user_data):
        assert user_data.status_code == 200 and user_data.json()['success'] is True

    @allure.title('Создание пользователя, который уже есть в системе.')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_create_user_who_already_in_system(self):
        req_create_old_user = requests.post(Urls.create_user, data=DataForTest.static_user)
        assert req_create_old_user.status_code == 403 and req_create_old_user.json()['success'] == False

    @allure.title('Создание пользователя пропустив одно поле при заполнении.')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_create_user_one_field_null(self):
        req_create_incorrect_user = requests.post(Urls.create_user, data=DataForTest.incorrect_user)
        assert req_create_incorrect_user.status_code == 403 and req_create_incorrect_user.json()['success'] == False
