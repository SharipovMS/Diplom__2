import requests
from urls.urls import Urls
from data_for_tests.data import IngredientData
import allure

class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем')
    @allure.description('Проверка ответа в формате JSON')
    def test_create_order_with_auth(self, user_data):
        order_req = requests.post(Urls.order, json=IngredientData.immortal_burger).json()
        assert order_req['name'] == 'Бессмертный флюоресцентный бургер'

    @allure.title('Оформление заказа с неверным хэш ингридиента')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_create_order_incorrect_hash_ingridients(self, user_data):
        order_req = requests.post(Urls.order, json=IngredientData.incorrect_burger)
        assert order_req.status_code == 500

    @allure.title('Оформление заказа без ингридиентов')
    @allure.description('Проверка статус кода и ответа в формате JSON')
    def test_create_order_not_ingridients(self, user_data):
        order_req = requests.post(Urls.order, json=IngredientData.empty_burger)
        assert order_req.status_code == 400 and order_req.json()['message'] == 'Ingredient ids must be provided'

