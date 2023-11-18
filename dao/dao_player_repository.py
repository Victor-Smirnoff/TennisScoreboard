from sqlalchemy import select
from dao.player_repository import PlayerRepository
from model.database import session_factory
from model.models import PlayerOrm


class DaoPlayerRepository(PlayerRepository):
    """
    Класс для выполнения действий над таблицей players
    """

    def save(self, name):
        """
        Метод для сохранения (добавления) данных в БД
        Это метод Create	INSERT
        :param name: имя игрока, которого надо добавить в таблицу players
        :return: объект класса PlayerOrm с данными из БД (данные которые были добавлены в БД)
        """
        new_player = PlayerOrm(name=name)
        with session_factory() as session:
            session.add(new_player)
            session.commit()

        return new_player

    def find_by_name(self, name):
        """
        Метод для нахождения данных по name
        Это метод Read	SELECT
        :param name: имя игрока
        :return: объект с данными из БД
        Это либо объект класса PlayerOrm (данные по игроку)
        Либо это объект None (его вернёт нам алхимия)
        """
        with session_factory() as session:
            query = select(PlayerOrm).filter_by(name=name)
            result = session.execute(query)
            player = result.scalars().first()

        return player