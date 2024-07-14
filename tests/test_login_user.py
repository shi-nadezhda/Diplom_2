import allure
import requests
import json
from endpoints import Api
from helpers import Register
from data import ResponseText


class TestLoginUsers:
    @allure.title('Проверка логина существующего пользователя')
    @allure.description('Авторизуемся под пользователем, заполняя поле существующими логином/паролем. Получаем ответ true')
    def test_login_with_existing_user_success(self):
        headers = {"Content-type": "application/json"}
        user = Register.generate_new_random_user()
        payload = json.dumps(user)
        r = requests.post(Api.create_user, data=payload, headers=headers)

        assert r.status_code == 200

        login_payload = json.dumps({'email': user.get('email'), 'password': user.get('password')})
        l = requests.post(Api.login_user, data=login_payload, headers=headers)
        
        assert l.status_code == 200
        assert l.json().get("success") is True
      
    
    @allure.title('Проверка логина с неверным логином и паролем')
    @allure.description('Авторизуемся под пользователем, заполняя поле несуществующим логином/паролем. Получаем сообщение об ошибке "email or password are incorrect" и код 401')         
    def test_login_with_invalid_field_login_failed(self):
        user = Register.generate_new_random_user()
        payload = json.dumps({'email': user.get('email'), 'password': user.get('password')})
        headers = {"Content-type": "application/json"}
        r = requests.post(Api.login_user, data=payload, headers=headers)
        
        assert r.status_code == 401
        assert r.json().get("success") is False
        assert r.json().get('message') == ResponseText.invalid_field
