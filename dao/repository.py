"""
Здесь описан класс для выполнения основных действий над базой данных:
позволяют создавать (C - create), читать (R - read)
"""


class Repository:
    """
    Класс для выполнения основных действий над базой данных
    Во всех методах вызываем raise NotImplementedError
    Чтобы в дочерних классах переопределить эти методы
    """

    def find_by_name(self, name):
        """
        Метод для нахождения данных по name
        Это метод Read	SELECT
        :param name: имя игрока
        :return: объект с данными из БД
        """
        raise NotImplementedError

    def save(self):
        """
        Метод для сохранения (добавления) данных в БД
        Это метод Create	INSERT
        :return: объект с данными из БД (данные которые были добавлены в БД)
        """
        raise NotImplementedError