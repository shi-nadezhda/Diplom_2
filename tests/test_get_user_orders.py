import allure
import requests
from endpoints import Api


class TestGetUserOrders:
    @allure.title('Проверка получения заказов авторизованного пользователя')
    @allure.description('Получаем заказы у авторизованного пользователя')
    def test_receive_orders_from_authorized_user(self, get_auth_user):
        orders = requests.get(Api.orders, headers=get_auth_user[4].get('headers'))
        
        assert orders.status_code == 200
        assert orders.json().get("success") is True
        
    
    @allure.title('Проверка получения заказов неавторизованного пользователя')
    @allure.description('Получаем заказы у неавторизованного пользователя')
    def test_receive_orders_from_unauthorized_user(self):
        orders = requests.get(Api.orders)
        
        assert orders.status_code == 401
        assert orders.json().get("success") is False
