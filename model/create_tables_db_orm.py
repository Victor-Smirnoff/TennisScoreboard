"""
Этот файл служит для создания таблиц players и matches в базе данных tennis и для первоначального наполнения этих таблиц
"""

from model.database import Base, engine, session_factory
from model.models import PlayerOrm, MatchOrm
import uuid
import csv
from random import choice
from sqlalchemy import select


class CreateTablesDataBase:
    """
    Класс для создания таблиц players и matches в базе данных tennis
    """

    def create_tables(self):
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

    def insert_data_players(self):
        """
        Метод добавляет 100 теннисистов в таблицу players
        Данные берутся из файла ATP_Rankings.txt - это 100 лучших теннисистов на текущий момент по рейтингу ATP
        :return: None
        """
        tennis_players_lst = self.get_lst_players()
        tennis_players = [PlayerOrm(name=player) for player in tennis_players_lst]
        with session_factory() as session:
            session.add_all(tennis_players)
            session.commit()

    def insert_data_matches(self):
        """
        Метод добавляет сыгранные матчи из файла matches.csv - это рандомно написанные матчи, лишь бы было наполнение
        :return: None
        """
        with open("static_data/generated_matches.csv", "r", encoding="UTF-8") as file:
            matches_lst = [name.strip().split(";") for name in file.readlines()][1:]
            matches_lst = [[int(match[0]), int(match[1]), int(match[2]), match[3]] for match in matches_lst]
        tennis_matches = [MatchOrm(UUID=str(uuid.uuid4()), player1=player1, player2=player2, winner=winner, score=score) for player1, player2, winner, score in matches_lst]
        with session_factory() as session:
            session.add_all(tennis_matches)
            session.commit()

    def get_lst_players(self):
        """
        Метод возвращает список из 100 игроков, который берет из файла 'static_data/ATP_Rankings.txt'
        :return: список 100 игроков
        """
        with open("static_data/ATP_Rankings.txt", "r", encoding="UTF-8") as file:
            tennis_players_lst = [name.strip() for name in file.readlines()]
            return tennis_players_lst

    def get_players_ID_lst(self):
        """
        Метод берез из базы данных айди всех игроков
        :return: список айди игроков
        """
        with session_factory() as session:
            query = select(PlayerOrm.ID)
            result = session.execute(query)
            players_ID_lst = result.scalars().all()

        return players_ID_lst

    def generate_matches(self, players_ID_lst, quantity_matches):
        """
        Метод генерирует список из строк с данными по матчам
        :param players_ID_lst: список действительных ID игроков для генерации матчей
        :param quantity_matches: количество матчей, которые надо сгенерировать
        :return: None. Ничего не возвращает, а просто записывает строки в csv файл
        """
        columns = ["player1", "player2", "winner", "score"]

        with open("static_data/generated_matches.csv", "w", encoding="UTF-8", newline='') as file:
            writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONE)
            writer.writerow(columns)
            for _ in range(quantity_matches):
                row = self.get_row_for_csv_file(players_ID_lst)
                writer.writerow(row)

    def get_row_for_csv_file(self, players_ID_lst):
        """
        Метод формирует список для заполнения csv файла
        :param players_ID_lst: список айди игроков
        :return: список row для записи
        """
        player_1_ID = choice(players_ID_lst)
        players_ID_lst.remove(player_1_ID)
        player_2_ID = choice(players_ID_lst)
        players_ID_lst.append(player_1_ID)
        winner = choice([player_1_ID, player_2_ID])
        if winner == player_1_ID:
            score = {'player_1': 2, 'player_2': choice([0, 1])}
        else:
            score = {'player_1': choice([0, 1]), 'player_2': 2}
        row = [player_1_ID, player_2_ID, winner, score]
        return row



data_base_obj = CreateTablesDataBase()
data_base_obj.create_tables()
data_base_obj.insert_data_players()
quantity_matches = 777
data_base_obj.generate_matches(players_ID_lst=data_base_obj.get_players_ID_lst(), quantity_matches=quantity_matches)
data_base_obj.insert_data_matches()