from re import fullmatch
from jinja2 import Template

from service.tennis_match import TennisMatch
from service.player_service import PlayerService
from service.match_service import MatchService


class NewMatchPostHandler:
    """
    Класс для обработки поступающих данных на странице '/new-match'
    Проверяет что записи Имя игрока 1 и Имя игрока 2 не пустые
    Что Имя игрока 1 и Имя игрока 2 не равны друг другу
    А также что имя состоит только из букв

    Если с полученными данными всё ок, то:
    1. Проверяет существование игроков в таблице Players. Если игрока с таким именем не существует, создаём
    2. Создаём экземпляр класса Match (содержащий айди игроков и текущий счёт) и кладём в коллекцию текущих матчей
    (существующую только в памяти приложения, либо в key-value storage).
    Ключом коллекции является UUID, значением - экземпляр класса Match.
    3. Редирект на страницу /match-score?uuid=$match_id
    """

    def __call__(self, player_1_name, player_2_name):
        """
        Метод для вызова объекта класса NewMatchPostHandler
        :param player_1_name: имя игрока 1
        :param player_2_name: имя игрока 2
        :return: возвращаем HTML страницу если хоть одно имя игрока не корректно или объект класса TennisMatch если оба имени корректны
        """
        if not self.is_correct_player_name(player_1_name) or not self.is_correct_player_name(player_2_name) or player_1_name == player_2_name:
            if not self.is_correct_player_name(player_1_name) and not self.is_correct_player_name(player_2_name):
                error_message = f"имя игрока 1 “{player_1_name}“ и имя игрока 2 “{player_2_name}“ введено некорректно, попробуйте ещё раз"
            elif not self.is_correct_player_name(player_1_name):
                error_message = f"имя игрока 1 “{player_1_name}“ введено некорректно, попробуйте ещё раз"
            elif not self.is_correct_player_name(player_2_name):
                error_message = f"имя игрока 2 “{player_2_name}“ введено некорректно, попробуйте ещё раз"
            elif player_1_name == player_2_name:
                error_message = f"имя игрока 1 “{player_1_name}“ и имя игрока 2 “{player_2_name}“ не могут быть одинаковы, попробуйте ещё раз"

            with open("view/pages/new-match-incorrect.html", "r", encoding="UTF-8") as file:
                HTML = file.read()
            tm = Template(HTML)
            HTML = tm.render(error_message=error_message)
            return HTML
        else:
            player_service = PlayerService(player_1_name=player_1_name, player_2_name=player_2_name)
            player_1, player_2 = player_service.get_two_players()
            player_1_ID, player_1_name = player_1.ID, player_1.name
            player_2_ID, player_2_name = player_2.ID, player_2.name

            tennis_match = TennisMatch(player_1_ID=player_1_ID,
                                       player_1_name=player_1_name,
                                       player_2_ID=player_2_ID,
                                       player_2_name=player_2_name
                                       )
            return tennis_match

    def is_correct_player_name(self, player_name: str) -> bool:
        """
        Метод проверяет имя игрока на коррекность
        :param player_name: имя игрока
        :return: bool True - если имя корректное, False - имя не корректное
        """
        return True if fullmatch(r"^[a-zA-Zа-яА-ЯёЁ ]+$", player_name) else False

    def get_players_name_form_data(self, form_data: dict) -> tuple:
        """
        Метод принимает словарь с данными form_data, и выдает имя игрока 1 и имя игрока 2
        Если одна из форм пустая, то пары ключ-значения вообще не будет
        Поэтому пустую строку и ключ нужно сгенерировать в этом методе
        Этот метод добавляет отсутствующий ключ в словарь form_data и значение пустой строки для этого ключа
        :param form_data: словарь с данными форм
        :return: кортеж (имя игрока 1, имя игрока 2)
        """
        if len(form_data) == 2:
            return form_data["player_1_name"], form_data["player_2_name"]
        else:
            if "player_1_name" not in form_data:
                form_data["player_1_name"] = ""
            if "player_2_name" not in form_data:
                form_data["player_2_name"] = ""

            player_1_name = form_data["player_1_name"]
            player_2_name = form_data["player_2_name"]

            return player_1_name, player_2_name