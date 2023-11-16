from waitress import serve
from whitenoise import WhiteNoise


def process_http_request(environ, start_response):
    status = "200 OK"

    if environ["PATH_INFO"] == "/":
        with open("view/pages/index.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
    elif environ["PATH_INFO"] == "/new-match":
        with open("view/pages/new-match.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
    elif environ["PATH_INFO"] == "/flex":
        with open("view/pages/index_flex.html", "r", encoding="UTF-8") as file:
            HTML = file.read()
    else:
        status = "400"
        HTML = "Страница не найдена"

    response_headers = [("Content-type", "text/html; charset=utf-8"), ]
    start_response(status, response_headers)

    print(environ)
    print(environ["PATH_INFO"])

    html_as_bytes = HTML.encode("utf-8")
    return [html_as_bytes]



if __name__ == "__main__":
    app = WhiteNoise(process_http_request, "view/static/")
    serve(app, host="localhost", port=8080)