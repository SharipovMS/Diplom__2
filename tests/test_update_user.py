import allure
import pytest
import requests
from urls.urls import Urls

class TestUpdateUser:

    @allure.title('Тест на обновление данных пользователя без авторизации')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    @pytest.mark.parametrize('incorrect_data',
                             [{'email': 'sharipov_5@gmail.com', 'password': '', 'name': ''},
                             {'email': '', 'password': 'hSTwgB83', 'name': ''}])
    def test_update_user_with_not_auth(self, incorrect_data):
        req_update_user_with_not_auth = requests.patch(Urls.update_user, data=incorrect_data)
        assert req_update_user_with_not_auth.status_code == 401 and req_update_user_with_not_auth.json()['message'] == 'You should be authorised'

    @allure.title('Тест на обновление данных авторизованного пользователя')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_update_user_with_auth(self, user_static_data):
        token = str(user_static_data.json()['accessToken'])
        req_update_user_with_auth = requests.patch(Urls.update_user, headers={'Authorization': token}, data={'name': 'М Шарипов2'})
        assert req_update_user_with_auth.status_code == 200 and req_update_user_with_auth.json()['user']['name'] == 'М Шарипов2'

    @allure.title('Тест на обновление данных авторизованного пользователя, обновление почты')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_update_user_with_auth(self, user_static_data):
        token = str(user_static_data.json()['accessToken'])
        req_update_user_email = requests.patch(Urls.update_user, headers={'Authorization': token}, data={'email': 'new_email@example.com'})
        assert req_update_user_email.status_code == 200 and req_update_user_email.json()['user']['email'] is True

    @allure.title('Тест на обновление данных авторизованного пользователя обновление пароля')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_update_user_with_auth(self, user_static_data):
        token = str(user_static_data.json()['accessToken'])
        req_update_user_password = requests.patch(Urls.update_user, headers={'Authorization': token}, data={'password': 'new_password'})
        assert req_update_user_password.status_code == 200 and req_update_user_password.json()['message'] is True