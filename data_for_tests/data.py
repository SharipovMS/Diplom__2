import random
from datetime import datetime
class DataForTest:

    static_user = {'email': 'sharipov_5@gmail.com', 'password': 'hSTwgB83', 'name': 'Марат Шарипов'}

    incorrect_user = {'email': 'sharipov_5@gmail.com', 'password': '', 'name': ''}

    @staticmethod
    def generate_data():
        name = "AutoTest" + datetime.now().strftime('%Y%m%d%H%M')
        email = name + '@yandex.ru'
        password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8)) + 'password'
        return {'email': email, 'password': password, 'name': name}
