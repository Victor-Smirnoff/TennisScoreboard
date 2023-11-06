from database import Base, engine, session_factory
from models import PlayersOrm, MatchesOrm


def create_tables():
    # engine.echo = True
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # engine.echo = True

def insert_data():
    with open("ATP_Rankings.txt", "r", encoding="UTF-8") as file:
        tennis_players_lst = [name.strip() for name in file.readlines()]
    tennis_players = [PlayersOrm(name=player) for player in tennis_players_lst]
    with session_factory() as session:
        session.add_all(tennis_players)
        session.commit()



create_tables()
insert_data()