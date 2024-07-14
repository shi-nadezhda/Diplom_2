import allure
import requests
import json
from endpoints import Api
from data import ResponseText


class TestCreateOrder:
    ingredients = requests.get(Api.ingredients)

    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description('Создаем заказ для авторизованного пользователя')
    def test_create_order_with_authorization_success(self, get_auth_user):
        headers = {"Content-type": "application/json", **get_auth_user[4].get('headers')}
        ingr = self.ingredients.json().get('data')
        payload = json.dumps({'ingredients': [ingr[0].get('_id'), ingr[1].get('_id')]})
        
        r = requests.post(Api.orders, data=payload, headers=headers)
        
        assert r.status_code == 200
        assert r.json().get("success") is True
        
        
    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('Создаем заказ для неавторизованного пользователя')
    def test_create_order_not_authorization_success(self):
        headers = {"Content-type": "application/json"}
        ingr = self.ingredients.json().get('data')
        payload = json.dumps({'ingredients': [ingr[0].get('_id'), ingr[1].get('_id')]})
        
        r = requests.post(Api.orders, data=payload, headers=headers)
        
        assert r.status_code == 200
        assert r.json().get("success") is True
     
            
    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Создаем заказ без ингридиентов')
    def test_create_order_not_ingredients_success(self, get_auth_user):
        headers = {"Content-type": "application/json", **get_auth_user[4].get('headers')}
        ingr = self.ingredients.json().get('data')
        payload = json.dumps({'ingredients': []})
        
        r = requests.post(Api.orders, data=payload, headers=headers)
        
        assert r.status_code == 400
        assert r.json().get("success") is False
        assert r.json().get('message') == ResponseText.ingredient_is_requaed
        
        
    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    @allure.description('Создаем заказ с неверным хешем ингридиентов')
    def test_create_order_with_incorrect_ingredient_hash(self, get_auth_user):
        headers = {"Content-type": "application/json", **get_auth_user[4].get('headers')}
        ingr = self.ingredients.json().get('data')
        payload = json.dumps({'ingredients': [4554545, 450894504]})
        
        r = requests.post(Api.orders, data=payload, headers=headers)
        
        assert r.status_code == 500
