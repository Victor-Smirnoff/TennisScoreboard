from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Index
import uuid
from database import Base, str_50
from typing import Annotated


int_pk_ai = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
player_id = Annotated[int, mapped_column(ForeignKey("players.ID", ondelete="CASCADE"))]


class PlayersOrm(Base):
    """
    Класс, представляющий таблицу players в SQLAlchemy
    """
    __tablename__ = "players"

    ID: Mapped[int_pk_ai]
    name: Mapped[str_50] = mapped_column(nullable=False)

name_index = Index("name_index", PlayersOrm.name)


class MatchesOrm(Base):
    """
    Класс, представляющий таблицу matches в SQLAlchemy
    """
    __tablename__ = "matches"

    ID: Mapped[int_pk_ai]
    UUID: Mapped[str] = mapped_column(String(255), default=str(uuid.uuid4()))
    player1: Mapped[player_id]
    player2: Mapped[player_id]
    winner: Mapped[player_id]
    score: Mapped[str_50] = mapped_column(nullable=False)