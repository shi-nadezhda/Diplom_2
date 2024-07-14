import random
import allure
import string


class Register:
        
    @allure.step('Создаем рандомного пользователя')    
    def generate_new_random_user():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        email = generate_random_string(10) + '@mail.ru'
        password = generate_random_string(10)
        name = generate_random_string(10)

        return {
            "email": email,
            "password": password,
            "name": name
        }
