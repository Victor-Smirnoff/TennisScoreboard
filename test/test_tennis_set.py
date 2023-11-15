import unittest
from service.tennis_set import TennisSet
from service.tennis_game import TennisGameTieBreak


class Test_tennis_set(unittest.TestCase):
    """
    Класс для тестирования функций класса TennisSet
    """

    def test_6_6(self):
        """
        При счёте 6-6 начинается тайбрейк вместо обычного гейма
        """
        tennis_set = TennisSet()
        [tennis_set.add_point(1) for _ in range(6)]
        [tennis_set.add_point(2) for _ in range(6)]
        tennis_set.update_result_set_score()
        self.assertEqual({"player_1": 6, "player_2": 6}, tennis_set.result_set_score)
        self.assertEqual(type(tennis_set.game_dict[13]), TennisGameTieBreak)