from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Index
from model.database import Base, str_50, str_250
from typing import Annotated


int_pk_ai = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]             # тип данных int primary_key и autoincrement
player_id = Annotated[int, mapped_column(ForeignKey("players.ID", ondelete="CASCADE"))]     # тип данных int ForeignKey для players.ID


class PlayerOrm(Base):
    """
    Класс, представляющий таблицу players в SQLAlchemy
    """
    __tablename__ = "players"

    ID: Mapped[int_pk_ai]
    name: Mapped[str_50] = mapped_column(nullable=False, unique=True, index=True)

    def __str__(self):
        return f"PlayerOrm(ID={self.ID}, name={self.name})"


class MatchOrm(Base):
    """
    Класс, представляющий таблицу matches в SQLAlchemy
    """
    __tablename__ = "matches"

    ID: Mapped[int_pk_ai]
    UUID: Mapped[str_250] = mapped_column(unique=True, nullable=False)
    player1: Mapped[player_id]
    player2: Mapped[player_id]
    winner: Mapped[player_id]
    score: Mapped[str_250] = mapped_column(nullable=False)

    def __str__(self):
        return f"MatchOrm(ID={self.ID}, UUID={self.UUID}, player1={self.player1}, player1={self.player2}, winner={self.winner}, score={self.score})"