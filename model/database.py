from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy import create_engine
from model.config import settings


engine = create_engine(url=settings.DATA_BASE_URL, echo=True) # создаем движок sqlalchemy для работы с БД

session_factory = sessionmaker(bind=engine) # создаем переменную session_factory для создания сессий

class Base(DeclarativeBase):
    pass