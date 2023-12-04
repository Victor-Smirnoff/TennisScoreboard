class MatchScoreGetHandler:
    """
    Класс для возвращения страницы счета матча
    Создаем объект класса и вызываем его. В результате получаем HTML страницу
    """

    def __call__(self):
        """
        Метод ничего не принимает и возвращает match-score.html
        :return: HTML страница new-match.html
        """
        with open("view/pages/match-score.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
            return HTML