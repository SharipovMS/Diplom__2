import requests
from urls.urls import Urls
import allure

class TestGetUserOrders:

    @allure.title('Получение заказов не авторизованного пользователя')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_get_not_auth_user_order(self, user_static_data):
        order_req = requests.get(Urls.get_orders)
        assert order_req.status_code == 401 and order_req.json()['message'] == 'You should be authorised'

    @allure.title('Получение заказов авторизованного пользователя')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_get_auth_user_order(self, user_static_data):
        token = str(user_static_data.json()['accessToken'])
        order_req = requests.get(Urls.get_orders, headers={'Authorization': token})
        assert order_req.status_code == 200 and order_req.json()['success'] == True

