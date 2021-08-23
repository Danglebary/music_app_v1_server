from api import app, genre_list, jsonify
from flask_cors import cross_origin

@app.route('/api', methods=["GET"])
def hello_world():
    return "Hello from the backend"

@app.route('/genres', methods=["GET"])
@cross_origin()
def genres():
    genres = jsonify(genres=genre_list)
    return genres