from jinja2 import Template
from dao.dao_match_repository import DaoMatchRepository
from dao.dao_player_repository import DaoPlayerRepository



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
        dao_match_obj = DaoMatchRepository()

        if filter_by_player_name == "":
            lst_matches = dao_match_obj.find_all()
        else:
            lst_matches = dao_match_obj.find_by_name(filter_by_player_name)

        html_matches_sample = ""

        for match in lst_matches:
            html_row_sample = self.get_html_sample(match)

            html_matches_sample += html_row_sample

        with open("view/pages/matches.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
        tm = Template(HTML)
        HTML = tm.render(html_matches_sample=html_matches_sample)
        return HTML

    def get_html_sample(self, match):
        """
        Метод возвращает строку html таблицы с данными по одному завершенному матчу
        :param match: объект класса TennisMatch
        :return: строка с тегами html с данными по одному завершенному матчу
        """
        dao_player_obj = DaoPlayerRepository()

        match_ID = match.ID
        player_1_ID = match.player1
        player_2_ID = match.player2
        winner_ID = match.winner
        player_1_name = dao_player_obj.find_name_by_id(player_1_ID)
        player_2_name = dao_player_obj.find_name_by_id(player_2_ID)
        winner_name = dao_player_obj.find_name_by_id(winner_ID)

        html_row_sample = f"""
                        <div class="row">
                          <div class="cell_10"><h4>{match_ID}</h4></div>
                          <div class="cell"><h4>{player_1_name}</h4></div>
                          <div class="cell"><h4>{player_2_name}</h4></div>
                          <div class="cell"><h4>{winner_name}</h4></div>
                        </div>

                        """
        return html_row_sample