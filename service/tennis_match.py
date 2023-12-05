from service.tennis_set import TennisSet
import uuid


class TennisMatch:
    """
    Класс описывает сущность теннисного матча
    """
    def __init__(self, player_1_ID, player_1_name, player_2_ID, player_2_name):
        self.player_1_ID = player_1_ID
        self.player_1_name = player_1_name
        self.player_2_ID = player_2_ID
        self.player_2_name = player_2_name
        self.set_dict = {tennis_set: TennisSet() for tennis_set in range(1, 4)}
        self.player_1_win_match = False
        self.player_2_win_match = False
        self.player_1_score = 0
        self.player_2_score = 0
        self.result_match_score = {"player_1": 0, "player_2": 0}
        self.match_uuid = str(uuid.uuid4())
        self.current_tennis_set = self.set_dict[1] # сомнительная переменная, возможно, удалить её
        self.current_tennis_game = self.current_tennis_set.game_dict[1]

    def add_point(self, player: int):
        """
        Метод для добавления очков в гейме
        :param player: номер игрока цифра int 1 или 2
        :return: None
        """
        if int(player) == 1:
            self.player_1_score += 1
            self.update_result_match_score()
        elif int(player) == 2:
            self.player_2_score += 1
            self.update_result_match_score()

    def update_result_match_score(self):
        """
        Метод обновляет self.result_set_score
        :return: None
        """
        self.result_match_score = {"player_1": self.player_1_score, "player_2": self.player_2_score}

    def check_end_match(self):
        """
        Метод проверят завершился матч или нет
        :return: bool True - матч завершен, False - в противном случае
        """
        if self.player_1_score == 2:
            self.player_1_win_match = True
            return True
        elif self.player_2_score == 2:
            self.player_2_win_match = True
            return True
        return False

    def show_match_score(self):
        """
        Метод выводит в консоль текущий счёт матча
        :return: None
        """
        print("Это вывод результата матча")
        print(self.result_match_score)


# это строчки для запуска класса TennisMatch и проведения одного матча!!!

# tennis_match = TennisMatch()
# while not tennis_match.check_end_match():
#     tennis_match.show_match_score()
#     player = input("введите номер игрока 1 или 2: ")
#     tennis_match.add_point(player)
#
# tennis_match.show_match_score()
# print(f"Победил игрок_1: {tennis_match.player_1_win_match}")
# print(f"Победил игрок_2: {tennis_match.player_2_win_match}")


# Это логика проведения теннисного матча
# здесь поменять ввод переменной player = input("введите номер игрока 1 или 2: ") на данные из POST запроса
# и приложение будет работать - производить вычисления счета матча в зависимости от поступивших данных

# tennis_match = TennisMatch()
# while not tennis_match.check_end_match():
#     tennis_match.show_match_score()
#
#     for tennis_set in tennis_match.set_dict.values():
#         if tennis_match.check_end_match():
#             break
#         while not tennis_set.check_end_set():
#             tennis_set.show_set_score()
#
#             for tennis_game in tennis_set.game_dict.values():
#                 if tennis_set.check_end_set():
#                     break
#                 while not tennis_game.check_end_game():
#                     tennis_game.show_game_score()
#                     player = input("введите номер игрока 1 или 2: ")
#                     tennis_game.add_point(player)
#                     tennis_game.set_game_score()
#
#                 tennis_game.show_game_score()
#                 tennis_set.add_point(1) if tennis_game.player_1_win_game else tennis_set.add_point(2)
#                 tennis_set.show_set_score()
#
#         tennis_match.add_point(1) if tennis_set.player_1_win_set else tennis_match.add_point(2)
#         tennis_match.show_match_score()