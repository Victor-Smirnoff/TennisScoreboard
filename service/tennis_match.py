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
        self.current_tennis_set = self.set_dict[1]
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
            self.check_end_match()
        elif int(player) == 2:
            self.player_2_score += 1
            self.update_result_match_score()
            self.check_end_match()

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