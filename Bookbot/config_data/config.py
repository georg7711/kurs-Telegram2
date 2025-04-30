from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN5")
ADMIN_IDS = os.getenv("ADMIN_ID")

from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot


# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
    return Config(
        tg_bot=TgBot(
            token=TOKEN,
            admin_ids=list(map(int, ADMIN_IDS))
        )
    )