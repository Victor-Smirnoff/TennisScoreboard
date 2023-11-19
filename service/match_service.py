from dao.dao_match_repository import DaoMatchRepository
from service.tennis_match import TennisMatch
from service.player_service import PlayerService


class MatchService:
    """
    Класс для проведения матча
    Объект класс создает объект класса TennisMatch и проводит этот матч
    По завершении матча записывает его в БД в таблицу matches

    Для проведения матча необходимо создать объект класса MatchService
    И вызвать метод perform_match, в который будут передавать результаты POST запросов
    """

    def __init__(self, player_1, player_2):
        """
        Инифиализатор класса MatchService
        :param player_1: объект класса PlayerOrm для игрока 1
        :param player_2: объект класса PlayerOrm для игрока 2
        """
        self.player_1 = player_1
        self.player_2 = player_2

    def perform_match(self):
        """
        Метод выполняет логику проведения теннисного матча
        По завершении матча возвращает записанную строку прошедшего матча
        :return: объект класса MatchOrm
        """
        player_1_ID, player_1_name = self.player_1.ID, self.player_1.name
        player_2_ID, player_2_name = self.player_2.ID, self.player_2.name

        tennis_match = TennisMatch(player_1_ID=player_1_ID,
                                   player_1_name=player_1_name,
                                   player_2_ID=player_2_ID,
                                   player_2_name=player_2_name
                                   )

        while not tennis_match.check_end_match():
            tennis_match.show_match_score()

            for tennis_set in tennis_match.set_dict.values():
                if tennis_match.check_end_match():
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

                tennis_match.add_point(1) if tennis_set.player_1_win_set else tennis_match.add_point(2)
                tennis_match.show_match_score()

        dao_obj = DaoMatchRepository()

        winner = player_1_ID if tennis_match.player_1_win_match else player_2_ID

        new_match = dao_obj.save_to_database(UUID=tennis_match.match_uuid,
                                             player1=player_1_ID,
                                             player2=player_2_ID,
                                             winner=winner,
                                             score=str(tennis_match.result_match_score)
                                             )

        # здесь тоже пересмотреть что выводится в return
        # почему-то доступа к объекту класса MatchOrm нет
        # или самого объекта класса MatchOrm нет
        # разобраться с этим!
        return dao_obj.find_match_from_uuid(tennis_match.match_uuid)


# строчки для теста этого сервиса
player_service = PlayerService("Илья Ивашка", "Vasa Pupkin")
player_1, player_2 = player_service.get_two_players()
match_service = MatchService(player_1, player_2)
new_match = match_service.perform_match()
print(new_match)
