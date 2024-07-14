class Api:
    base_api_url = 'https://stellarburgers.nomoreparties.site/api' # главная страница
    create_user = base_api_url + '/auth/register' # создать пользователя
    login_user = base_api_url + '/auth/login' # логин пользователя
    user_data = base_api_url + '/auth/user' # изменение данных пользователя
    ingredients = base_api_url + '/ingredients' # ингредиенты
    orders = base_api_url + '/orders' # работа с заказами пользователя
    get_user_orders = base_api_url + '/account/order-history' # получить заказы конкретного пользователя
    delete_user = user_data # удаление пользователя
