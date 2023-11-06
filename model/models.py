from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Index
import uuid
from database import Base


class PlayersOrm(Base):
    """
    Класс, представляющий таблицу players в SQLAlchemy
    """
    __tablename__ = "players"

    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)

name_index = Index("name_index", PlayersOrm.name)


class MatchesOrm(Base):
    """
    Класс, представляющий таблицу matches в SQLAlchemy
    """
    __tablename__ = "matches"

    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    UUID: Mapped[str] = mapped_column(String(255), default=str(uuid.uuid4()))
    player1: Mapped[int] = mapped_column(ForeignKey('players.ID'))
    player2: Mapped[int] = mapped_column(ForeignKey('players.ID'))
    winner: Mapped[int] = mapped_column(ForeignKey('players.ID'))
    score: Mapped[str] = mapped_column(String(30))