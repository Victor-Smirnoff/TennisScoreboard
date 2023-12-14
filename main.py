from waitress import serve
from whitenoise import WhiteNoise
from urllib.parse import parse_qs, urlparse
from webob import Response
from re import findall

from handlers.index_handler import IndexHandler
from handlers.matches_handler import MatchesHandler
from handlers.new_match_get_handler import NewMatchGetHandler
from handlers.new_match_post_handler import NewMatchPostHandler
from handlers.match_score_get_handler import MatchScoreGetHandler
from handlers.match_score_post_handler import MatchScorePostHandler



class MainApp:
    """
    Главный класс веб-сервер
    """

    CURRENT_MATCHES = {}  # Коллекция текущих матчей. Сюда будем складывать объекты класса TennisMatch

    def process_http_request(self, environ, start_response):
        status = "200 OK"

        if "tennis/" in environ["PATH_INFO"]:
            environ["PATH_INFO"].replace("tennis/", "")

        if environ["PATH_INFO"] == "/" and environ["REQUEST_METHOD"] == "GET":
            handler = IndexHandler()
            HTML = handler()

        elif environ["PATH_INFO"] == "/new-match" and environ["REQUEST_METHOD"] == "GET":
            handler = NewMatchGetHandler()
            HTML = handler()

        elif environ["PATH_INFO"] == "/new-match" and environ["REQUEST_METHOD"] == "POST":
            handler = NewMatchPostHandler()

            form_data = self.get_form_data(environ)
            player_1_name, player_2_name = handler.get_players_name_form_data(form_data)

            if not handler.is_correct_player_name(player_1_name) or not handler.is_correct_player_name(player_2_name) or player_1_name == player_2_name:
                HTML = handler(player_1_name=player_1_name, player_2_name=player_2_name)
            else:
                tennis_match = handler(player_1_name=player_1_name, player_2_name=player_2_name)
                uuid = tennis_match.match_uuid
                match_url = "/match-score?uuid=" + uuid
                self.CURRENT_MATCHES[uuid] = tennis_match

                response = Response(status=303)
                response.location = match_url
                return response(environ, start_response)

        elif environ["PATH_INFO"] == "/match-score" and environ["REQUEST_METHOD"] == "GET":
            regex = r"(?<=/match-score\?uuid=).+"
            REQUEST_URI = environ["REQUEST_URI"]
            uuid_from_REQUEST_URI = findall(regex, REQUEST_URI)[0]

            tennis_match = self.CURRENT_MATCHES[uuid_from_REQUEST_URI]
            handler = MatchScoreGetHandler(tennis_match)
            HTML = handler()

        elif environ["PATH_INFO"] == "/match-score" and environ["REQUEST_METHOD"] == "POST":
            regex = r"(?<=/match-score\?uuid=).+"
            REQUEST_URI = environ["REQUEST_URI"]
            uuid_from_REQUEST_URI = findall(regex, REQUEST_URI)[0]
            tennis_match = self.CURRENT_MATCHES[uuid_from_REQUEST_URI]

            handler = MatchScorePostHandler(tennis_match)

            form_data = self.get_form_data(environ)
            player_win_game = int(form_data["player_win_game"])

            HTML = handler(player_win_game)

            if tennis_match.check_end_match():
                if uuid_from_REQUEST_URI in self.CURRENT_MATCHES:
                    del self.CURRENT_MATCHES[uuid_from_REQUEST_URI]

        elif environ["PATH_INFO"] == "/matches" and environ["REQUEST_METHOD"] == "GET":
            handler = MatchesHandler()
            REQUEST_URI = environ["REQUEST_URI"]
            form_data = self.parse_request_uri(REQUEST_URI)

            if len(form_data) == 0:
                HTML = handler()
            else:
                if "page" in form_data and "filter_by_player_name" in form_data:
                    HTML = handler(page=int(form_data["page"]),
                                   filter_by_player_name=form_data["filter_by_player_name"],
                                   REQUEST_URI=REQUEST_URI
                                   )
                elif "page" not in form_data and "filter_by_player_name" in form_data:
                    HTML = handler(page=1,
                                   filter_by_player_name=form_data["filter_by_player_name"],
                                   REQUEST_URI=REQUEST_URI
                                   )
                elif "page" in form_data and "filter_by_player_name" not in form_data:
                    HTML = handler(page=int(form_data["page"]),
                                   filter_by_player_name="",
                                   REQUEST_URI=REQUEST_URI
                                   )

        else:
            status = "400"
            with open("view/pages/not_found.html", "r", encoding="UTF-8") as file:
                HTML = file.read()

        response_headers = [("Content-type", "text/html; charset=utf-8"), ]
        start_response(status, response_headers)

        html_as_bytes = HTML.encode("utf-8")
        return [html_as_bytes]

    def get_form_data(self, environ):
        """
        Метод для получения данных форм
        :param environ: окружение
        :return: словарь с данными форм
        """
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        post_data = environ['wsgi.input'].read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)
        form_data = {key: value[0] for key, value in parsed_data.items()}
        return form_data

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



if __name__ == "__main__":
    main_app = MainApp()
    app = WhiteNoise(main_app.process_http_request, "view/static/")
    serve(app, host="127.0.0.1", port=8888)