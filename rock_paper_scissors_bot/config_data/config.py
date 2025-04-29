from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN4")
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    return Config(tg_bot=TgBot(token=TOKEN))