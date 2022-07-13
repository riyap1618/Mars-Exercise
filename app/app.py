import datetime

from flask import Flask, render_template, request, redirect, url_for
from app.http_client import HttpClient
from app.rover_model import RoverModel
from dateutil import parser

app = Flask(__name__)
client = HttpClient()


@app.route('/')
def index():
    return render_template('index.html', landing_image='https://via.placeholder.com/500')


@app.route('/mars/<rover_name>')
def mars(rover_name):
    query_date = request.args.get("date")
    rover = RoverModel.from_json(client.get_manifest(rover_name))

    rover_max_date = parser.parse(rover.max_date).strftime("%Y-%m-%d")

    date = query_date if query_date else rover_max_date

    response = client.get_images(rover_name, day=date, is_random=True)

    response_photos = response['photos']

    photos = [photo['img_src'] for photo in response_photos[0:3]]

    return render_template('mars.html', rover=RoverModel.from_json(client.get_manifest(rover_name)), photos = photos, date = date)


@app.route('/mars/<rover_name>', methods=["POST"])
def mars_submit(rover_name):
    date_form_str = request.form.get("date")
    date: datetime.datetime = parser.parse(date_form_str)

    date_nasa_str = date.strftime("%Y-%m-%d")

    return redirect(url_for("mars", rover_name = rover_name, date = date_nasa_str))
