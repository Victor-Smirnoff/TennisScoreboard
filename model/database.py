from typing import Annotated
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy import create_engine, String
from model.config import settings


engine = create_engine(url=settings.DATA_BASE_URL, echo=True) # создаем движок sqlalchemy для работы с БД

session_factory = sessionmaker(bind=engine) # создаем переменную session_factory для создания сессий

str_50 = Annotated[str, 50]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_50: String(50)
    }