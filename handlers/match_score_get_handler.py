from jinja2 import Template
from service.tennis_match import TennisMatch


class MatchScoreGetHandler:
    """
    Класс для возвращения страницы счета матча
    Создаем объект класса и вызываем его. В результате получаем HTML страницу
    """

    def __init__(self, tennis_match: TennisMatch):
        """
        Инициализатор класса MatchScoreGetHandler
        :param tennis_match: объект класса TennisMatch
        """
        self.tennis_match = tennis_match

    def __call__(self):
        """
        Метод ничего не принимает и возвращает match-score.html
        :return: HTML страница match-score.html
        """
        with open("view/pages/match-score.html", "r", encoding="UTF-8") as file:
            HTML = file.read()

            REQUEST_URI = "/match-score?uuid=" + self.tennis_match.match_uuid
            player_1_name = self.tennis_match.player_1_name
            player_2_name = self.tennis_match.player_2_name
            player_1_match_score = self.tennis_match.result_match_score["player_1"]
            player_2_match_score = self.tennis_match.result_match_score["player_2"]
            player_1_set_1_score = self.tennis_match.set_dict[1].result_set_score["player_1"]
            player_2_set_1_score = self.tennis_match.set_dict[1].result_set_score["player_2"]
            player_1_set_2_score = self.tennis_match.set_dict[2].result_set_score["player_1"]
            player_2_set_2_score = self.tennis_match.set_dict[2].result_set_score["player_2"]
            player_1_set_3_score = self.tennis_match.set_dict[3].result_set_score["player_1"]
            player_2_set_3_score = self.tennis_match.set_dict[3].result_set_score["player_2"]
            player_1_game_score = self.tennis_match.current_tennis_game.player_1_score
            player_2_game_score = self.tennis_match.current_tennis_game.player_2_score
            player_1_game_score_points = self.tennis_match.current_tennis_game.result_game_score["player_1"]
            player_2_game_score_points = self.tennis_match.current_tennis_game.result_game_score["player_2"]

            template = Template(HTML)
            HTML = template.render(REQUEST_URI=REQUEST_URI,
                                   player_1_name=player_1_name,
                                   player_2_name=player_2_name,
                                   player_1_match_score=player_1_match_score,
                                   player_2_match_score=player_2_match_score,
                                   player_1_set_1_score=player_1_set_1_score,
                                   player_2_set_1_score=player_2_set_1_score,
                                   player_1_set_2_score=player_1_set_2_score,
                                   player_2_set_2_score=player_2_set_2_score,
                                   player_1_set_3_score=player_1_set_3_score,
                                   player_2_set_3_score=player_2_set_3_score,
                                   player_1_game_score=player_1_game_score,
                                   player_2_game_score=player_2_game_score,
                                   player_1_game_score_points=player_1_game_score_points,
                                   player_2_game_score_points=player_2_game_score_points
                                   )

            return HTML