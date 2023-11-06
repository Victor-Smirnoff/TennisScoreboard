from sqlalchemy import Column, Integer, String, create_engine, Index, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid


Base = declarative_base()

# with engine.connect() as conn:
#     res = conn.execute(text("SELECT VERSION()"))
#     print(f"{res.all()=}")


class Players(Base):
    """
    Класс, представляющий таблицу players в SQLAlchemy
    """
    __tablename__ = "players"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)


name_index = Index("name_index", Players.name)


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


connection_string = "mysql+pymysql://root:KUku1212_b2zZ@localhost/tennis"
engine = create_engine(url=connection_string, echo=False)
Base.metadata.create_all(engine)