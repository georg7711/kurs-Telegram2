import os

import dotenv


dotenv.load_dotenv()

print(os.getenv('TELEGRAM_BOT_TOKEN1'))
print(os.getenv('TELEGRAM_BOT_TOKEN2'))
print(os.getenv('TELEGRAM_BOT_TOKEN3'))
print(os.getenv('ADMIN_ID'))