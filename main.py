from waitress import serve
from whitenoise import WhiteNoise
from urllib.parse import parse_qs

from handlers.index_handler import IndexHandler
from handlers.new_match_get_handler import NewMatchGetHandler
from handlers.new_match_post_handler import NewMatchPostHandler



def process_http_request(environ, start_response):
    status = "200 OK"

    if environ["PATH_INFO"] == "/" and environ["REQUEST_METHOD"] == "GET":
        handler = IndexHandler()
        HTML = handler()

    elif environ["PATH_INFO"] == "/new-match" and environ["REQUEST_METHOD"] == "GET":
        handler = NewMatchGetHandler()
        HTML = handler()

    elif environ["PATH_INFO"] == "/new-match" and environ["REQUEST_METHOD"] == "POST":
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        post_data = environ['wsgi.input'].read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)
        form_data = {key: value[0] for key, value in parsed_data.items()}

        # player_1_name, player_2_name = form_data["player_1_name"], form_data["player_2_name"]
        # handler = NewMatchPostHandler()
        # HTML = handler(player_1_name=player_1_name, player_2_name=player_2_name)
        # print(f"player_1_name={player_1_name}, player_2_name={player_2_name}")

        print(form_data)

        handler = NewMatchGetHandler()
        HTML = handler()

    elif environ["PATH_INFO"] == "/match-score":
        with open("view/pages/match-score.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
    else:
        status = "400"
        with open("view/pages/not_found.html", "r", encoding="UTF-8") as file:
            HTML = file.read()

    response_headers = [("Content-type", "text/html; charset=utf-8"), ]
    start_response(status, response_headers)

    print(environ)
    print(environ["PATH_INFO"])

    html_as_bytes = HTML.encode("utf-8")
    return [html_as_bytes]



if __name__ == "__main__":
    app = WhiteNoise(process_http_request, "view/static/")
    serve(app, host="localhost", port=8080)