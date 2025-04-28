import os

from environs import Env


env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение 
                          
bot_token1 = env('TELEGRAM_BOT_TOKEN1')  # Получаем и сохраняем значение переменной окружения в переменную bot_token
bot_token2 = env('TELEGRAM_BOT_TOKEN2')
bot_token3 = env('TELEGRAM_BOT_TOKEN3')
admin_id = env.int('ADMIN_ID')  # Получаем и преобразуем значение переменной окружения к типу int, 
                                # затем сохраняем в переменной admin_id

# Выводим значения переменных в терминал
print(bot_token1)
print(bot_token2)
print(bot_token3)
print(admin_id)
print()

# Убедимся также, что переменные есть в окружении
print(os.getenv('TELEGRAM_BOT_TOKEN1'))
print(os.getenv('TELEGRAM_BOT_TOKEN2'))
print(os.getenv('TELEGRAM_BOT_TOKEN3'))
print(os.getenv('ADMIN_ID'))