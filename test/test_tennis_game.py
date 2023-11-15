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

    def test_40_40_plus(self):
        """
        Если игрок 1 выигрывает очко при счёте 40-40, гейм не заканчивается
        Если игрок 2 выигрывает очко при счёте больше-меньше, гейм не заканчивается, становится ровно
        Если игрок 2 выигрывает очко при счёте ровно-ровно, гейм не заканчивается, становится меньше-больше
        Если игрок 2 выигрывает очко при счёте меньше-больше, то он выигрывает и гейм
        """
        tennis_game = TennisGame()
        [tennis_game.add_point(1) for _ in range(3)]
        [tennis_game.add_point(2) for _ in range(3)]
        tennis_game.add_point(1)
        self.assertEqual(tennis_game.check_end_game(), False)
        tennis_game.add_point(2)
        tennis_game.set_game_score()
        self.assertEqual(tennis_game.check_end_game(), False)
        self.assertEqual(tennis_game.result_game_score["player_2"], "ровно")
        tennis_game.add_point(2)
        tennis_game.set_game_score()
        self.assertEqual(tennis_game.check_end_game(), False)
        self.assertEqual(tennis_game.player_2_win_game, False)
        self.assertEqual(tennis_game.result_game_score["player_2"], "больше")
        tennis_game.add_point(2)
        tennis_game.set_game_score()
        self.assertEqual(tennis_game.check_end_game(), True)
        self.assertEqual(tennis_game.player_2_win_game, True)
        self.assertEqual(tennis_game.result_game_score["player_2"], "гейм")

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

    def test_tie_break_6_6(self):
        """
        Если игрок 1 выигрывает очко при счёте 6-6, гейм тай-брейк не заканчивается
        """
        tennis_game = TennisGameTieBreak()
        [tennis_game.add_point(1) for _ in range(6)]
        [tennis_game.add_point(2) for _ in range(6)]
        tennis_game.add_point(1)
        self.assertEqual(tennis_game.check_end_game(), False)
        tennis_game.add_point(1)
        self.assertEqual(tennis_game.check_end_game(), True)
        self.assertEqual(tennis_game.player_1_win_game, True)

    def test_tie_break_6_0(self):
        """
        Если игрок 1 выигрывает очко при счёте 6-0, то он выигрывает и гейм тай-брейк
        """
        tennis_game = TennisGameTieBreak()
        [tennis_game.add_point(1) for _ in range(6)]
        tennis_game.add_point(1)
        self.assertEqual(tennis_game.check_end_game(), True)
        self.assertEqual(tennis_game.player_1_win_game, True)



if __name__ == "__main__":
    unittest.main()