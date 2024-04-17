import requests
from urls.urls import Urls
import allure

class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем')
    @allure.description('Проверка ответа в формате JSON')
    def test_create_order_with_auth(self, user_data):
        order_req = requests.post(Urls.order, json={"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}).json()
        assert order_req['name'] == 'Бессмертный флюоресцентный бургер'

    @allure.title('Создание заказа авторизованным пользователем')
    @allure.description('Проверка ответа в формате JSON')
    def test_create_order_auth(self):
        order_req = requests.post(Urls.order, json={"ingredients": ["61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa72"]}).json()
        assert order_req['name'] == 'Spicy био-марсианский бургер'

    @allure.title('Оформление заказа с неверным хэш ингридиента')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_create_order_incorrect_hash_ingridients(self, user_data):
        order_req = requests.post(Urls.order, json={"ingredients": ["61c0c5проблема1bdaaa6d", "61c0c5a71проблемаdaaa72"]})
        assert order_req.status_code == 500

    @allure.title('Оформление заказа без ингридиентов')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_create_order_not_ingridients(self, user_data):
        order_req = requests.post(Urls.order, json={"ingredients": []})
        assert order_req.status_code == 400 and order_req.json()['message'] == 'Ingredient ids must be provided'

