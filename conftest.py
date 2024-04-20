import pytest
import requests
from data_for_tests.data import DataForTest
from urls.urls import Urls


@pytest.fixture
def user_data():
    respons = requests.post(Urls.create_user, data=DataForTest.generate_data())
    yield respons
    token = str(respons.json()['accessToken'])
    requests.delete(Urls.update_user, headers={'Authorization': token})

@pytest.fixture
def user_static_data():
    respons = requests.post(Urls.user_login, data=DataForTest.static_user)
    yield respons