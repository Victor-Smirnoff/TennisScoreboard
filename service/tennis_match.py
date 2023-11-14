from tennis_set import TennisSet


class TennisMatch:
    """
    Класс описывает сущность теннисного матча
    """
    def __init__(self):
        self.set_dict = {tennis_set: TennisSet() for tennis_set in range(1, 4)}