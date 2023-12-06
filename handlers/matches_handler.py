from jinja2 import Template
from dao.dao_match_repository import DaoMatchRepository



class MatchesHandler:
    """
    Класс обрабатывает GET запросы на странице '/matches'
    """

    def __call__(self, page=1, filter_by_player_name=""):
        """
        Метод для вызова объекта класса MatchesHandler
        :param page: номер страницы
        :param filter_by_player_name: имя игрока
        :return: возвращаем HTML страницу
        """
        dao_obj = DaoMatchRepository()

        if filter_by_player_name == "":
            lst_matches = dao_obj.find_all()
        else:
            lst_matches = dao_obj.find_by_name(filter_by_player_name)

        # with open("view/pages/matches.html", "r", encoding="UTF-8") as file:
        #     HTML = file.read()
        # tm = Template(HTML)
        # HTML = tm.render(lst_matches=lst_matches)
        # return HTML
        return lst_matches


handler = MatchesHandler()
res = handler(filter_by_player_name="васа")
print(res)