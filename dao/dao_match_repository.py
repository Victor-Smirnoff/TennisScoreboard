import uuid
from sqlalchemy import select, or_
from dao.match_repository import MatchRepository
from model.database import session_factory
from model.models import PlayerOrm, MatchOrm


class DaoMatchRepository(MatchRepository):
    """
    Класс для выполнения действий над таблицей matches
    """

    def find_all(self):
        """
        Метод для нахождения всех данных записей в БД
        Это метод Read	SELECT
        :return: список с объектами с данными из БД
        """
        with session_factory() as session:
            query = select(MatchOrm)
            result = session.execute(query)
            finished_all_mathches = result.scalars().all()

        return finished_all_mathches

    def save(self, UUID, player1, player2, winner, score):
        """
        Метод для сохранения (добавления) данных в БД
        Это метод Create	INSERT
        :param UUID: Уникальный айди матча
        :param player1: Айди первого игрока
        :param player2: Айди второго игрока
        :param winner: Айди победителя
        :param score: JSON представление объекта с текущим счётом в матче
        :return: объект класса MatchOrm с данными из БД (данные которые были добавлены в БД)
        """
        new_match = MatchOrm(player1=player1, player2=player2, winner=winner, score=score)
        with session_factory() as session:
            session.add(new_match)
            session.commit()

        return new_match

    def find_by_name(self, name):
        """
        Метод для нахождения данных по name
        Это метод Read	SELECT
        :param name: имя игрока
        :return: объект с данными из БД
        Это либо список объектов класса MatchOrm (данные по сыгранным мачтам)
        Либо это объект None - его я сам верну если такого игрока нет в таблице
        Либо пустой список - вернет алхимия если игрок есть, но у него нет ни одного матча
        """
        player_ID = self.get_player_ID(name)
        # если в результате получили какое-то число player_ID, то можно делать запрос
        if player_ID:
            with session_factory() as session:
                # запрос в БД SELECT * FROM matches WHERE matches.player1 = %(player1_1)s OR matches.player2 = %(player2_1)s
                query = select(MatchOrm).filter(or_(MatchOrm.player1 == player_ID, MatchOrm.player2 == player_ID))
                result = session.execute(query)
                finished_mathches = result.scalars().all()
            # здесь мы можем получить пустой список [] если у игрока не найдется ни одного матча в таблице matches
            return finished_mathches
        # если вместо player_ID получили None, то значит такого игрока нет в таблице players
        else:
            return None

    def get_player_ID(self, name):
        """
        Метод возвращает ID игрока по его имени name
        :param name: имя игрока
        :return: ID игрока из таблицы players
        """
        with session_factory() as session:
            query = select(PlayerOrm).filter_by(name=name)
            result = session.execute(query)
            player = result.scalars().first()
        if player:
            return player.ID
        else:
            return None