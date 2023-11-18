from sqlalchemy import select
from dao.player_repository import PlayerRepository
from model.database import session_factory
from model.models import PlayersOrm


class DaoPlayerRepository(PlayerRepository):
    """
    Класс для выполнения действий над таблицей players
    """

    def save(self, name):
        """
        Метод для сохранения (добавления) данных в БД
        Это метод Create	INSERT
        :param name: имя игрока, которого надо добавить в таблицу players
        :return: объект с данными из БД (данные которые были добавлены в БД)
        """
        player = PlayersOrm(name=name)
        with session_factory() as session:
            session.add(player)
            session.commit()

    def find_by_name(self, name):
        """
        Метод для нахождения данных по name
        Это метод Read	SELECT
        :param name: имя игрока
        :return: объект с данными из БД
        Это либо объект класса PlayersOrm (данные по игроку)
        Либо это объект None (его вернёт нам алхимия)
        """
        with session_factory() as session:
            query = select(PlayersOrm).filter_by(name=name)
            result = session.execute(query)
            player = result.scalars().first()

        return player