import allure
import requests
import json
from endpoints import Api
from helpers import Register
from data import ResponseText


class TestChangeUserData:
    @allure.title('Проверка изменения данных у авторизованного пользователя')
    @allure.description('Проверяем возможность изменить любое поле')
    def test_change_data_from_authorized_user_success(self):
        headers = {"Content-type": "application/json"}
        
        user = Register.generate_new_random_user()
        payload = json.dumps(user)
        r = requests.post(Api.create_user, data=payload, headers=headers)
        
        assert r.json().get('user').get('name') == user.get('name')
          
        login_payload = json.dumps({'email': user.get('email'), 'password': user.get('password')})
        l = requests.post(Api.login_user, data=login_payload, headers=headers)
    
        assert l.status_code == 200
        
        auth_headers = {**headers, 'Authorization': l.json().get("accessToken")}
        new_name = 'Blablabla'
        update_payload = json.dumps({'email': user.get('email'), 'name': new_name})
        
        e = requests.patch(Api.user_data, data=update_payload, headers=auth_headers)
        
        assert e.status_code == 200
        assert e.json().get('user').get('name') == new_name
        
    
    @allure.title('Проверка изменения данных у неавторизованного пользователя')
    @allure.description('Проверяем возможность изменить любое поле. Получаем сообщение об ошибке и код ответа 401')
    def test_change_data_from_unauthorized_user(self):
        headers = {"Content-type": "application/json"}
        
        user = Register.generate_new_random_user()
        payload = json.dumps(user)
        r = requests.post(Api.create_user, data=payload, headers=headers)
        
        assert r.json().get('user').get('name') == user.get('name')
          
        login_payload = json.dumps({'email': user.get('email'), 'password': user.get('password')})
        l = requests.post(Api.login_user, data=login_payload, headers=headers)
    
        assert l.status_code == 200
        
        new_name = 'Blablabla'
        update_payload = json.dumps({'email': user.get('email'), 'name': new_name})
        
        e = requests.patch(Api.user_data, data=update_payload, headers=headers)
        
        assert e.status_code == 401
        assert e.json().get('message') == ResponseText.change_data_from_unauthorized_user
