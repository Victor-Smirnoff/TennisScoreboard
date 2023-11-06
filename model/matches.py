from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid


Base = declarative_base()


class Matches(Base):
    """
    Класс, представляющий таблицу matches в SQLAlchemy
    """
    __tablename__ = "matches"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    UUID = Column(String, default=str(uuid.uuid4()))
    player1 = Column(Integer, ForeignKey('players.ID'))
    player2 = Column(Integer, ForeignKey('players.ID'))
    winner = Column(Integer, ForeignKey('players.ID'))
    score = Column(String)

    player1 = relationship("Players", foreign_keys=[player1])
    player2 = relationship("Players", foreign_keys=[player2])