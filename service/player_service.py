from dao.dao_player_repository import DaoPlayerRepository


class PlayerService:
    """
    Класс для получения объекта класса PlayerOrm
    Использование этого класса происходит во время написания имени игрока на странице нового матча по адресу /new-match
    HTML форма с полями “Имя игрока 1”, “Имя игрока 2” и кнопкой “начать”
    Нажатие кнопки “начать” приводить к POST запросу по адресу /new-match
    Вот тут “Имя игрока 1” и “Имя игрока 2” будут передаваться в инициализатор этого класса
    Дальше будет происходить проверка если ли имя в базе данных в таблице players или нет
    Если имя есть в таблице players, то получаем объект класса PlayerOrm и из него берем атрибуты ID и name
    Если имя нет в таблице players, то записываем его в БД, потом получаем эту записанную запись
    в виде объекта класса PlayerOrm и из него берем атрибуты ID и name

    Чтобы получить два объекта игроков: нужно создать экземпляр класса PlayerService и вызвать у него метод get_two_players
    """
    def __init__(self, player_1_name, player_2_name):
        """
        Инициализатор класса PlayerService
        :param player_1_name: Имя игрока 1
        :param player_2_name: Имя игрока 2
        """
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name

    def get_two_players(self):
        """
        Методя для получения двух объектов класса PlayerOrm, который будут проводить матч
        :return: кортеж из двух элементов - объектов класса PlayerOrm (игрока 1 и игрока 2)
        """
        player_1 = self.get_player(self.player_1_name)
        player_2 = self.get_player(self.player_2_name)
        return (player_1, player_2)

    def get_player(self, player_name):
        """
        Метод возвращает объект класса PlayerOrm
        Если игрок есть в базе, то он оттуда вытаскивается
        Если игрока такого нет, то он туда записывается и вытаскиывается
        :param player_name: имя игрока
        :return: объект класса PlayerOrm
        """
        dao_obj = DaoPlayerRepository()
        player = dao_obj.find_by_name(player_name)
        if player:
            return player
        else:
            player = dao_obj.save(player_name)
            return player