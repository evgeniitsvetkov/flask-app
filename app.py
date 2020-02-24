from random import sample
from flask import Flask, render_template, request
import data

app = Flask(__name__)


@app.route('/')
def index():

    # choose six random tours
    sample_tours = sample(data.tours.items(), 6)

    output = render_template("index.html",
                             title=data.title,
                             departures=data.departures,
                             subtitle=data.subtitle,
                             description=data.description,
                             sample_tours=sample_tours)
    return output


@app.route('/from/<direction>')
def directions(direction):

    tours_from_direction = {}
    for tour_id, tour in data.tours.items():
        if tour['departure'] == direction:
            tours_from_direction[tour_id] = tour

    output = render_template("direction.html",
                             title=data.title,
                             departures=data.departures,
                             direction=direction,
                             tours_from_direction=tours_from_direction)   # только туры по направлению
    return output


@app.route('/tours/<int:tour_id>')
def tours(tour_id):
    output = render_template("tour.html",
                             title=data.title,
                             departures=data.departures,
                             tour=data.tours[tour_id])
    return output


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def server_error(e):
    return "Что-то не так, но мы все починим"


if __name__ == '__main__':
    app.run()
