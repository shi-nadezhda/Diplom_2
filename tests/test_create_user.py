import allure
import requests
import json
from endpoints import Api
from helpers import Register
from data import ResponseText


class TestCreateUser:
    user = json.dumps(Register.generate_new_random_user())
    
    @allure.title('Проверка создания уникального пользователя')
    @allure.description('Создаем уникального пользователя. Получаем ответ "true" и код 200')
    def test_create_user_success(self):                       
        headers = {"Content-type": "application/json"}

        r = requests.post(Api.create_user, data=self.user, headers=headers)
         
        assert r.status_code == 200
        assert r.json().get("success") is True        
        

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    @allure.description('Создаем пользователя, который уже зарегистрирован. Получаем сообщение об ошибке "User already exists" и код 403')
    def test_create_user_double(self):
        headers = {"Content-type": "application/json"}
        
        r = requests.post(Api.create_user, data=self.user, headers=headers)
         
        assert r.status_code == 403
        assert r.json().get('message') == ResponseText.user_already_exists


    @allure.title('Проверка создания пользователя с одним незаполненным обязательным полем')
    @allure.description('Создаем пользователя, оставляя одно из полей незаполненным. Получаем сообщение об ошибке "Email, password and name are required fields" и код 403')
    def test_create_user_less_requaed_field(self):
        payload = { 
            'password': 'Fedora1', 
            'name': 'Fedora'
        }  
        headers = {"Content-type": "application/json"}
        payload_string = json.dumps(payload)
         
        r = requests.post(Api.create_user, data=payload_string, headers=headers)
         
        assert r.status_code == 403
        assert r.json().get('message') == ResponseText.blank_field    
