from typing import Annotated
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy import create_engine, String
from model.config import settings


# создаем движок sqlalchemy для работы с БД
# если базы tennis в базе данных нет, то она будет создана, если она есть, то будет создано подключение к ней
engine = create_engine(url=settings.DATA_BASE_URL, echo=True)

session_factory = sessionmaker(bind=engine) # создаем переменную session_factory для создания сессий

str_50 = Annotated[str, 50]         # тип данных строка длиной до 50 символов
str_250 = Annotated[str, 250]       # тип данных строка длиной до 250 символов


class Base(DeclarativeBase):
    """
    Базовый класс для создания моделей данных, которые представляют таблицы в базе данных.
    """
    type_annotation_map = {
        str_50: String(50),
        str_250: String(250)
    }