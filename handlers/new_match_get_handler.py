class NewMatchGetHandler:
    """
    Класс для возвращения главной страницы приложения
    Создаем объект класса и вызываем его. В результате получаем HTML страницу
    """

    def __call__(self):
        """
        Метод ничего не принимает и возвращает index.html
        :return: HTML страница index.html
        """
        with open("view/pages/new-match.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
            return HTML