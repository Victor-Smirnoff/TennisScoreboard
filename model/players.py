from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Players(Base):
    """
    Класс, представляющий таблицу players в SQLAlchemy
    """
    __tablename__ = "players"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)