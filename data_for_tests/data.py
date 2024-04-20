import random
from datetime import datetime
class DataForTest:

    static_user = {'email': 'sharipov_5@gmail.com', 'password': 'hSTwgB83', 'name': 'Марат Шарипов'}

    incorrect_password = {'email': 'sharipov_5@gmail.com', 'password': '', 'name': ''}

    incorrect_email = {'email': '', 'password': 'hSTwgB83', 'name': ''}

    @staticmethod
    def generate_data():
        name = "AutoTest" + datetime.now().strftime('%Y%m%d%H%M')
        email = name + '@yandex.ru'
        password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8)) + 'password'
        return {'email': email, 'password': password, 'name': name}

class IngredientData:

    immortal_burger = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

    incorrect_burger = {"ingredients": ["61c0c5проблема1bdaaa6d", "61c0c5a71проблемаdaaa72"]}

    empty_burger = {"ingredients": []}