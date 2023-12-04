from jinja2 import Template

from service.match_service import MatchService


class MatchScorePostHandler:
    """
    Класс для обработки поступающих данных на странице '/match-score'
    Обрабатывает нажатие на кнопки - “игрок 1 выиграл текущее очко”, “игрок 2 выиграл текущее очко”
    """

    def __init__(self, REQUEST_URI):
        self.REQUEST_URI = REQUEST_URI

    def __call__(self, player_win_game):
        """
        Метод для вызова обработчика POST запроса по адресу '/match-score'
        Метод принимает в качестве аргумента число player_win_game - 1 или 2
        Дальше обрабатывает это число в классе MatchService
        После чего обновляет данные на HTML странице
        :param player_win_game: число из данных формы - 1 или 2 (какой игрок выиграл очко в текущем гейме)
        :return: обновленная HTML страница match-score.html
        """
        with open("view/pages/match-score.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
            template = Template(HTML)
            HTML = template.render(REQUEST_URI=self.REQUEST_URI)
            return HTML