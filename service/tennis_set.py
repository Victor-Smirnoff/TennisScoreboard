from service.tennis_game import TennisGame, TennisGameTieBreak


class TennisSet:
    """
    Класс описывает один сет игры в теннис
    """
    def __init__(self):
        self.game_dict = {game: TennisGame() for game in range(1, 13)}
        self.game_dict[13] = TennisGameTieBreak()
        self.player_1_win_set = False
        self.player_2_win_set = False
        self.player_1_score = 0
        self.player_2_score = 0
        self.result_set_score = {"player_1": 0, "player_2": 0}

    def add_point(self, player: int):
        """
        Метод для добавления очков в гейме
        :param player: номер игрока цифра int 1 или 2
        :return: None
        """
        if int(player) == 1:
            self.player_1_score += 1
            self.update_result_set_score()
            self.check_end_set()
        elif int(player) == 2:
            self.player_2_score += 1
            self.update_result_set_score()
            self.check_end_set()

    def update_result_set_score(self):
        """
        Метод обновляет self.result_set_score
        :return: None
        """
        self.result_set_score = {"player_1": self.player_1_score, "player_2": self.player_2_score}

    def check_end_set(self):
        """
        Метод проверят завершился сет или нет
        :return: bool True - сет завершен, False - в противном случае
        """
        if self.player_1_score == 6 and self.player_2_score <= 4:
            self.player_1_win_set = True
            return True
        elif self.player_2_score == 6 and self.player_1_score <= 4:
            self.player_2_win_set = True
            return True
        elif self.player_1_score >= 5 and self.player_2_score == 7:
            self.player_2_win_set = True
            return True
        elif self.player_2_score >= 5 and self.player_1_score == 7:
            self.player_1_win_set = True
            return True
        else:
            return False

    def show_set_score(self):
        """
        Метод выводит в консоль текущий счёт сета
        :return: None
        """
        print("Это вывод результата сета")
        print(self.result_set_score)


# это строчки для запуска класса TennisSet и проведения одного сета!!!

# tennis_set = TennisSet()
# while not tennis_set.check_end_set():
#     tennis_set.show_set_score()
#     player = input("введите номер игрока 1 или 2: ")
#     tennis_set.add_point(player)
#
# tennis_set.show_set_score()
# print(f"Победил игрок_1: {tennis_set.player_1_win_set}")
# print(f"Победил игрок_2: {tennis_set.player_2_win_set}")