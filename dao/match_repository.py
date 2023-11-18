from dao.repository import Repository


class MatchRepository(Repository):
    """
    Класс для выполнения действий над таблицей matches
    (добавляется метод find_all для нахождения всех завершенных матчей)
    """

    def find_all(self):
        """
        Метод для нахождения всех данных записей в БД
        Это метод Read	SELECT
        :return: список с объектами с данными из БД
        """
        raise NotImplementedError