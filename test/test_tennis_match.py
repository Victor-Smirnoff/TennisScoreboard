import unittest
from service.tennis_match import TennisMatch


class Test_tennis_match(unittest.TestCase):
    """
    Класс для тестирования функций класса TennisMatch
    """

    def test_1_1(self):
        """
        Если игрок 1 выигрывает сет при счёте 1-1, то он выигрывает и матч
        """
        tennis_match = TennisMatch()
        tennis_match.add_point(1)
        tennis_match.add_point(2)
        tennis_match.update_result_match_score()
        self.assertEqual(tennis_match.check_end_match(), False)
        self.assertEqual(tennis_match.player_1_win_match, False)
        self.assertEqual(tennis_match.player_2_win_match, False)
        self.assertEqual({"player_1": 1, "player_2": 1}, tennis_match.result_match_score)
        tennis_match.add_point(1)
        tennis_match.update_result_match_score()
        self.assertEqual({"player_1": 2, "player_2": 1}, tennis_match.result_match_score)
        self.assertEqual(tennis_match.check_end_match(), True)
        self.assertEqual(tennis_match.player_1_win_match, True)