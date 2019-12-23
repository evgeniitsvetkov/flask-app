from flask import Flask, render_template
from flask import request
import data

app = Flask(__name__)


@app.route('/')
def hello():
    output = render_template("index.html", title=data.title, departures=data.departures)
    return output


@app.route('/from/<direction>')
def directions(direction):
    output = render_template("direction.html",
                             title=data.title,
                             departures=data.departures,
                             direction={"msk": "Из Москвы", "spb": "Из Петербурга", "nsk": "Из Новосибирска",
                                        "ekb": "Из Екатеринбурга", "kazan": "Из Казани"})
    return output


@app.route('/tours/<id>')
def tours(id):
    output = render_template("tour.html",
                             title=data.title,
                             departures=data.departures,
                             id={1: {"title": "Marina Lake Hotel & Spa", "departure": "nsk"},
                                 2: {"title": "Baroque Hotel", "departure": "ekb"}})
    return output


# роут с дополнительными параметрами, типа ?key=value
@app.route('/search/')
def search():
    return "Выполняем поиск по строке " + request.values.get("s")


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def server_error(e):
    return "Что-то не так, но мы все починим"


app.run('0.0.0.0', 8000)
