from dao.dao_match_repository import DaoMatchRepository
from handlers.match_final_score_handler import MatchFinalScoreHandler
from handlers.match_score_get_handler import MatchScoreGetHandler
from service.tennis_match import TennisMatch


class MatchScorePostHandler:
    """
    Класс для обработки поступающих данных на странице '/match-score'
    Обрабатывает нажатие на кнопки - “игрок 1 выиграл текущее очко”, “игрок 2 выиграл текущее очко”
    """

    def __init__(self, tennis_match: TennisMatch):
        """
        Инициализатор класса MatchScorePostHandler
        :param tennis_match: объект класса TennisMatch
        """
        self.tennis_match = tennis_match

    def __call__(self, player_win_game):
        """
        Метод для вызова обработчика POST запроса по адресу '/match-score'
        Метод принимает в качестве аргумента число player_win_game - 1 или 2
        Дальше обрабатывает это число в классе MatchService
        После чего обновляет данные на HTML странице
        :param player_win_game: число из данных формы - 1 или 2 (какой игрок выиграл очко в текущем гейме)
        :return: обновленная HTML страница match-score.html
        """
        # здесь надо, в соответствии с тем, какой игрок выиграл очко, добавить это очко в текущий гейм в классе TennisMatch

        self.tennis_match.current_tennis_game.add_point(player_win_game)
        self.tennis_match.current_tennis_game.set_game_score()

        if self.tennis_match.current_tennis_game.check_end_game(): # если текущий гейм завершен
            self.tennis_match.current_tennis_set.add_point(player_win_game)

            if self.tennis_match.current_tennis_set.check_end_set(): # если текущий сет завершен
                self.tennis_match.current_tennis_set.add_point(player_win_game)

                if self.tennis_match.check_end_match(): # если весь матч завершен
                    winner = self.tennis_match.player_1_ID if self.tennis_match.player_1_win_match else self.tennis_match.player_2_ID
                    dao_obj = DaoMatchRepository()
                    dao_obj.save_to_database(UUID=self.tennis_match.match_uuid,
                                             player1=self.tennis_match.player_1_ID,
                                             player2=self.tennis_match.player_2_ID,
                                             winner=winner,
                                             score=str(self.tennis_match.result_match_score)
                                             )

                    handler = MatchFinalScoreHandler(self.tennis_match)
                    HTML = handler()
                    return HTML

                else: # если матч не завершен
                    self.tennis_match.add_point(player_win_game)
                    self.tennis_match.update_result_match_score()

                    for i in range(1, 4):
                        tennis_set = self.tennis_match.set_dict[i]
                        if not tennis_set.check_end_set(): # находим незавершенный сет и ссылаемся current_tennis_set на него
                            self.tennis_match.current_tennis_set = tennis_set
                            self.tennis_match.current_tennis_game = self.tennis_match.current_tennis_set.game_dict[1]
                            break

            else: # если текущий сет НЕ завершен
                for i in range(1, 14):
                    tennis_game = self.tennis_match.current_tennis_set.game_dict[i]
                    if not tennis_game.check_end_game(): # находим незавершенный гейм и ссылаемся current_tennis_game на него
                        self.tennis_match.current_tennis_game = tennis_game
                        break

        handler = MatchScoreGetHandler(self.tennis_match)
        HTML = handler()
        return HTML