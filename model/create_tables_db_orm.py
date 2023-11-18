"""
Этот файл служит для создания таблиц players и matches в базе данных tennis и для первоначального наполнения этих таблиц
"""

from database import Base, engine, session_factory
from models import PlayersOrm, MatchesOrm


def create_tables():
    """
    Метод создает две таблицы в базе данных tennis:
    players - таблица с данными игроков
    matches - таблица с данными по сыгранным матчам
    :return: None
    """
    # engine.echo = True
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # engine.echo = True

def insert_data_players():
    """
    Метод добавляет 100 теннисистов в таблицу players
    Данные берутся из файла ATP_Rankings.txt - это 100 лучших теннисистов на текущий момент по рейтингу ATP
    :return: None
    """
    with open("static_data/ATP_Rankings.txt", "r", encoding="UTF-8") as file:
        tennis_players_lst = [name.strip() for name in file.readlines()]
    tennis_players = [PlayersOrm(name=player) for player in tennis_players_lst]
    with session_factory() as session:
        session.add_all(tennis_players)
        session.commit()

def insert_data_matches():
    """
    Метод добавляет сыгранные матчи из файла matches.csv - это рандомно написанные матчи, лишь бы было наполнение
    :return: None
    """
    with open("static_data/matches.csv", "r", encoding="UTF-8") as file:
        matches_lst = [name.strip().split(";") for name in file.readlines()][1:]
        matches_lst = [[int(match[0]), int(match[1]), int(match[2]), match[3]] for match in matches_lst]
    tennis_matches = [MatchesOrm(player1=player1, player2=player2, winner=winner, score=score) for player1, player2, winner, score in matches_lst]
    with session_factory() as session:
        session.add_all(tennis_matches)
        session.commit()


create_tables()
insert_data_players()
insert_data_matches()