from jinja2 import Template
from re import fullmatch
from urllib.parse import parse_qs, urlparse
from random import shuffle

from dao.dao_match_repository import DaoMatchRepository
from dao.dao_player_repository import DaoPlayerRepository



class MatchesHandler:
    """
    Класс обрабатывает GET запросы на странице '/matches'
    """

    def __call__(self, page=1, filter_by_player_name="all", REQUEST_URI="/matches"):
        """
        Метод для вызова объекта класса MatchesHandler
        :param page: номер страницы
        :param filter_by_player_name: имя игрока
        :return: возвращаем HTML страницу
        """
        dao_match_obj = DaoMatchRepository()

        if filter_by_player_name == "all":
            lst_matches = dao_match_obj.find_all()
        elif filter_by_player_name == "":
            error_message = "Ошибка: имя игрока не может быть пустым, попробуйте ввести заново"
            HTML = self.get_error_html_page(error_message)
            return HTML
        elif not self.is_correct_player_name(filter_by_player_name):
            error_message = f"Ошибка: имя игрока “{filter_by_player_name}“ введено некорректно, попробуйте ещё раз"
            HTML = self.get_error_html_page(error_message)
            return HTML
        else:
            lst_matches = dao_match_obj.find_by_name(filter_by_player_name)
            # если матчей не найдено - два сценария - 1 нет такого игрока. 2 - игрок есть, но нет ни одного матча
            if not lst_matches:
                dao_player_obj = DaoPlayerRepository()
                player = dao_player_obj.find_by_name(filter_by_player_name)
                if player is None:
                    error_message = f"Ошибка: имя игрока “{filter_by_player_name}“ введено некорректно - такого игрока не существует, попробуйте ещё раз"
                    HTML = self.get_error_html_page(error_message)
                    return HTML
                else:
                    error_message_1 = f"Ошибка: у игрока по имени “{filter_by_player_name}“ нет завершенных матчей, попробуйте ввести другое имя<br><br>"
                    lst_players_ID = dao_match_obj.get_all_players_ID_with_matches()
                    shuffle(lst_players_ID)
                    five_player_ID = lst_players_ID[:5]
                    dao_player_obj = DaoPlayerRepository()
                    five_player_names = [dao_player_obj.find_name_by_id(player_ID) for player_ID in five_player_ID]
                    n_1, n_2, n_3, n_4, n_5 = five_player_names[0], five_player_names[1], five_player_names[2], five_player_names[3], five_player_names[4]
                    error_message_2 = f"Попробуйте искать следующие имена игроков: <br><br> “{n_1}“, “{n_2}“, “{n_3}“, “{n_4}“, “{n_5}“"
                    error_message = error_message_1 + error_message_2
                    HTML = self.get_error_html_page(error_message)
                    return HTML

        maximum_matches_on_page = 5
        quantity_pages = ((len(lst_matches) // maximum_matches_on_page) + 1) if len(lst_matches) % maximum_matches_on_page != 0 else (len(lst_matches) // maximum_matches_on_page)

        pagination_sample = self.get_pagination_sample(quantity_pages=quantity_pages, REQUEST_URI=REQUEST_URI)

        html_matches_sample = ""

        if page == 1 and len(lst_matches) >= 5:
            for match in lst_matches[0:maximum_matches_on_page]:
                html_row_sample = self.get_html_sample(match)
                html_matches_sample += html_row_sample
        elif page == quantity_pages:
            for match in lst_matches[maximum_matches_on_page * (page - 1):]:
                html_row_sample = self.get_html_sample(match)
                html_matches_sample += html_row_sample
        else:
            for match in lst_matches[maximum_matches_on_page * (page - 1):maximum_matches_on_page * page]:
                html_row_sample = self.get_html_sample(match)
                html_matches_sample += html_row_sample

        with open("view/pages/matches.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
        tm = Template(HTML)
        HTML = tm.render(html_matches_sample=html_matches_sample,
                         pagination_sample=pagination_sample)
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

    def get_error_html_page(self, error_message):
        """
        Метод возвращает html страницу с сообщением об ошибке
        :param error_message: сообщение об ошибке
        :return: HTML страница
        """
        with open("view/pages/matches-incorrect.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
        tm = Template(HTML)
        HTML = tm.render(error_message=error_message)
        return HTML

    def is_correct_player_name(self, player_name: str) -> bool:
        """
        Метод проверяет имя игрока на коррекность
        :param player_name: имя игрока
        :return: bool True - если имя корректное, False - имя не корректное
        """
        return True if fullmatch(r"^[a-zA-Zа-яА-ЯёЁ ]+$", player_name) else False

    def get_pagination_sample(self, quantity_pages, REQUEST_URI):
        """
        Метод возвращает строки html кода с готовой пагинацией
        :param quantity_pages: количество страниц для изготовления пагинации
        :return: строка с кодом html
        """
        current_page_number = self.get_page_number(REQUEST_URI)

        html_pagination_sample_start = """
                            <br>
                  <div class="pagination" style="text-align: center; font-size: 24px;">
                      <a href="#">&NestedLessLess;</a>
                    """

        html_pagination_sample = ""

        html_pagination_sample += html_pagination_sample_start

        for i in range(1, quantity_pages + 1):
            if i == current_page_number:
                current_string = f'<a href="{REQUEST_URI}" class="active">{i}</a>'
            else:
                query_params = self.parse_request_uri(REQUEST_URI)

                if "page" in query_params and "filter_by_player_name" in query_params:
                    current_request_uri = f"matches?page={i}&filter_by_player_name={query_params["filter_by_player_name"]}"
                elif "page" in query_params and "filter_by_player_name" not in query_params:
                    current_request_uri = f"matches?page={i}"
                elif "page" not in query_params and "filter_by_player_name" in query_params:
                    current_request_uri = f"matches?page=1&filter_by_player_name={query_params["filter_by_player_name"]}"
                elif "page" not in query_params and "filter_by_player_name" not in query_params:
                    current_request_uri = f"matches?page={i}"

                current_string = f'<a href="{current_request_uri}">{i}</a>'

            html_pagination_sample += current_string

        html_pagination_sample_end = """<a href="#">&NestedGreaterGreater;</a>
          </div>
            <br>
            """

        html_pagination_sample += html_pagination_sample_end

        return html_pagination_sample

    def get_page_number(self, request_uri):
        """
        Метод для возвращения словаря с параметрами из url
        :param request_uri: url адрес
        :return: значение page из get запроса, если в словаре такого ключа нет, то возвращается число 1
        """
        parsed_url = urlparse(request_uri)
        query_params = parse_qs(parsed_url.query)
        query_params = {key: value[0] for key, value in query_params.items()}
        if "page" in query_params:
            return int(query_params["page"])
        else:
            return 1

    def parse_request_uri(self, request_uri):
        """
        Метод для возвращения словаря с параметрами из url
        :param request_uri: url адрес
        :return: словарь с параметрами get-запроса
        """
        parsed_url = urlparse(request_uri)
        query_params = parse_qs(parsed_url.query)
        query_params = {key: value[0] for key, value in query_params.items()}
        return query_params