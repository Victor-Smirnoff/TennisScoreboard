class TennisGame:
    """
    Класс описывает один гейм игры в теннис
    """
    def __init__(self):
        self.player_1_win_game = False
        self.player_2_win_game = False
        self.player_1_score = 0
        self.player_2_score = 0
        self.result_game_score = {"player_1": 0, "player_2": 0}

    def add_point(self, player: int):
        """
        Метод для добавления очков в гейме
        :param player: номер игрока цифра int 1 или 2
        :return: None
        """
        if int(player) == 1:
            self.player_1_score += 1
        elif int(player) == 2:
            self.player_2_score += 1

    def check_end_game(self):
        """
        Метод проверят завершился гейм или нет
        :return: bool True - гейм завершен, False - в противном случае
        """
        if self.player_1_score == 4 and self.player_2_score < 3:
            self.player_1_win_game = True
            return True
        elif self.player_2_score == 4 and self.player_1_score < 3:
            self.player_2_win_game = True
            return True
        elif self.player_1_score > 4 and self.player_1_score - self.player_2_score == 2:
            self.player_1_win_game = True
            return True
        elif self.player_2_score > 4 and self.player_2_score - self.player_1_score == 2:
            self.player_2_win_game = True
            return True
        else:
            return False

    def set_game_score(self):
        """
        Метод для изменения данных теннисного счета в гейме
        Данные берет из параметров self.player_1_score и self.player_2_score
        И меняет данные в словаре self.result_game_score
        :return: None
        """
        tmp_dict = {0: 0, 1: 15, 2: 30, 3: 40, 4: "гейм"}
        if (self.player_1_score < 3 and self.player_2_score < 3) \
                or (self.player_1_score == 3 and self.player_2_score < 3) \
                or (self.player_1_score < 3 and self.player_2_score == 3):
            self.result_game_score["player_1"] = tmp_dict[self.player_1_score]
            self.result_game_score["player_2"] = tmp_dict[self.player_2_score]
        elif self.player_1_score > 2 or self.player_2_score > 2:
            if self.player_1_score - self.player_2_score == 0:
                self.result_game_score["player_1"] = self.result_game_score["player_2"] = "ровно"
            elif self.player_1_score - self.player_2_score == 1:
                self.result_game_score["player_1"] = "больше"
                self.result_game_score["player_2"] = "меньше"
            elif self.player_2_score - self.player_1_score == 1:
                self.result_game_score["player_1"] = "меньше"
                self.result_game_score["player_2"] = "больше"
            elif self.player_1_score - self.player_2_score > 1:
                self.result_game_score["player_1"] = "гейм"
            elif self.player_2_score - self.player_1_score > 1:
                self.result_game_score["player_2"] = "гейм"

    def show_game_score(self):
        """
        Метод выводит в консоль текущий счёт гейма
        :return: None
        """
        print(f"игрок_1: мячи: {self.player_1_score} очки: {self.result_game_score['player_1']}")
        print(f"игрок_2: мячи: {self.player_2_score} очки: {self.result_game_score['player_2']}")


class TennisGameTieBreak(TennisGame):
    """
    Класс описывает особый вид гейма - укороченный гейм tie-break до 7 мячей
    """
    def check_end_game(self):
        """
        Метод проверят завершился тай-брейк или нет
        :return: bool True - тай-брейк завершен, False - в противном случае
        """
        if self.player_1_score == 7 and self.player_2_score <= 5:
            self.player_1_win_game = True
            return True
        elif self.player_2_score == 7 and self.player_1_score <= 5:
            self.player_2_win_game = True
            return True
        elif self.player_1_score >= 6 and self.player_1_score - self.player_2_score == 2:
            self.player_1_win_game = True
            return True
        elif self.player_2_score >= 6 and self.player_2_score - self.player_1_score == 2:
            self.player_2_win_game = True
            return True
        else:
            return False

    def set_game_score(self):
        """
        Метод для изменения данных теннисного счета в тай-брейке
        Данные берет из параметров self.player_1_score и self.player_2_score
        И меняет данные в словаре self.result_game_score
        :return: None
        """
        self.result_game_score = {"player_1": self.player_1_score, "player_2": self.player_2_score}


# это строчки для теста класса TennisGame !!!

# game = TennisGame()
# while not game.check_end_game():
#     game.show_game_score()
#     player = input("введите номер игрока 1 или 2: ")
#     game.add_point(player)
#     game.set_game_score()
#
# game.show_game_score()
# print(f"Победил игрок_1: {game.player_1_win_game}")
# print(f"Победил игрок_2: {game.player_2_win_game}")


# это строчки для теста класса TennisGameTieBreak гейм тай-брейк !!!

# game = TennisGameTieBreak()
# while not game.check_end_game():
#     game.show_game_score()
#     player = input("введите номер игрока 1 или 2: ")
#     game.add_point(player)
#     game.set_game_score()
#
# game.show_game_score()
# print(f"Победил игрок_1: {game.player_1_win_game}")
# print(f"Победил игрок_2: {game.player_2_win_game}")