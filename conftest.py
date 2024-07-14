import pytest
import requests
import pytest
import json
from endpoints import Api
from helpers import Register


@pytest.fixture(scope='function')
def get_auth_user():
    headers = {"Content-type": "application/json"}
        
    user = Register.generate_new_random_user() 
    # Регистрация
    payload = json.dumps(user)
    r = requests.post(Api.create_user, data=payload, headers=headers)
    
    # Авторизация
    login_payload = json.dumps({'email': user.get('email'), 'password': user.get('password')})
    l = requests.post(Api.login_user, data=login_payload, headers=headers)
    
    result = {
        'user': user,
        'headers': {
            'Authorization': l.json().get("accessToken")
        }
    }
    
    yield payload, r, login_payload, l, result
    
    # Удаление пользователя
    requests.delete(Api.delete_user, headers={'Authorization': l.json().get("accessToken")})
