from dao.dao_match_repository import DaoMatchRepository


class MatchService:
    """
    Класс для проведения матча
    Объект класса MatchService принимает объект класса TennisMatch, складывает его в коллекцию CURRENT_MATCHES и проводит этот матч
    По завершении матча записывает его в БД в таблицу matches и удаляет из коллекции CURRENT_MATCHES

    Для проведения матча необходимо создать объект класса MatchService
    И вызвать метод perform_match, в который будут передавать результаты POST запросов
    """

    def __init__(self, tennis_match):
        """
        Инициализатор класса MatchService
        :param tennis_match: объект класса TennisMatch
        """
        self.tennis_match = tennis_match

    def perform_match(self):
        """
        Метод выполняет логику проведения теннисного матча
        По завершении матча возвращает записанную строку прошедшего матча
        :return: объект класса MatchOrm
        """

        while not self.tennis_match.check_end_match():
            self.tennis_match.show_match_score()

            for tennis_set in self.tennis_match.set_dict.values():
                if self.tennis_match.check_end_match():
                    break
                while not tennis_set.check_end_set():
                    tennis_set.show_set_score()

                    for tennis_game in tennis_set.game_dict.values():
                        if tennis_set.check_end_set():
                            break
                        while not tennis_game.check_end_game():
                            tennis_game.show_game_score()
                            # здесь поменять ввод переменной player на данные из POST запроса
                            # обработчик POST запроса должен вернуть число 1 или 2
                            player = input("введите номер игрока 1 или 2: ")
                            tennis_game.add_point(player)
                            tennis_game.set_game_score()

                        tennis_game.show_game_score()
                        tennis_set.add_point(1) if tennis_game.player_1_win_game else tennis_set.add_point(2)
                        tennis_set.show_set_score()

                self.tennis_match.add_point(1) if tennis_set.player_1_win_set else self.tennis_match.add_point(2)
                self.tennis_match.show_match_score()

        winner = self.tennis_match.player_1_ID if self.tennis_match.player_1_win_match else self.tennis_match.player_2_ID

        dao_obj = DaoMatchRepository()
        new_match = dao_obj.save_to_database(UUID=self.tennis_match.match_uuid,
                                             player1=self.tennis_match.player_1_ID,
                                             player2=self.tennis_match.player_2_ID,
                                             winner=winner,
                                             score=str(self.tennis_match.result_match_score)
                                             )

        return new_match


# строчки для теста этого сервиса
# player_service = PlayerService("Илья Ивашка", "Vasa Pupkin")
# player_1, player_2 = player_service.get_two_players()
# match_service = MatchService(player_1, player_2)
# new_match = match_service.perform_match()
# print(new_match)