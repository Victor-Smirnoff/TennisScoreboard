import unittest
from service.tennis_game import TennisGame, TennisGameTieBreak


class Test_tennis_game(unittest.TestCase):
    """
    Класс для тестирования функций класса TennisGame и TennisGameTieBreak
    """

    def test_40_40(self):
        """
        Если игрок 1 выигрывает очко при счёте 40-40, гейм не заканчивается
        """
        tennis_game = TennisGame()
        [tennis_game.add_point(1) for _ in range(3)]
        [tennis_game.add_point(2) for _ in range(3)]
        tennis_game.add_point(1)
        self.assertEqual(tennis_game.check_end_game(), False)

    def test_40_0(self):
        """
        Если игрок 1 выигрывает очко при счёте 40-0, то он выигрывает и гейм
        """
        tennis_game = TennisGame()
        [tennis_game.add_point(1) for _ in range(3)]
        tennis_game.add_point(1)
        self.assertEqual(tennis_game.check_end_game(), True)
        self.assertEqual(tennis_game.player_1_win_game, True)

    def test_0_40(self):
        """
        Если игрок 2 выигрывает очко при счёте 0-40, то он выигрывает и гейм
        """
        tennis_game = TennisGame()
        [tennis_game.add_point(2) for _ in range(3)]
        tennis_game.add_point(2)
        self.assertEqual(tennis_game.check_end_game(), True)
        self.assertEqual(tennis_game.player_2_win_game, True)