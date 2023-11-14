from tennis_set import TennisSet


class TennisMatch:
    """
    Класс описывает сущность теннисного матча
    """
    def __init__(self):
        self.set_dict = {tennis_set: TennisSet() for tennis_set in range(1, 4)}
        self.player_1_win_match = False
        self.player_2_win_match = False
        self.player_1_score = 0
        self.player_2_score = 0
        self.result_match_score = {"player_1": 0, "player_2": 0}

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
        :return: bool True - сет завершен, False - в противном случае
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
        print(self.result_match_score)


# это строчки для теста класса TennisMatch !!!

# tennis_match = TennisMatch()
# while not tennis_match.check_end_match():
#     tennis_match.show_match_score()
#     player = input("введите номер игрока 1 или 2: ")
#     tennis_match.add_point(player)
#
# tennis_match.show_match_score()
# print(f"Победил игрок_1: {tennis_match.player_1_win_match}")
# print(f"Победил игрок_2: {tennis_match.player_2_win_match}")