from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Datos de ejemplo
songs = ["Song A", "Song B", "Song C"]
artists = ["Artist 1", "Artist 2"]
albums = ["Album X", "Album Y"]

# Página principal con HTML dinámico
@app.route("/")
def home():
    return render_template("index.html", songs=songs, artists=artists, albums=albums)

# Endpoints JSON opcionales
@app.route("/songs")
def get_songs():
    return jsonify(songs)

@app.route("/artists")
def get_artists():
    return jsonify(artists)

@app.route("/albums")
def get_albums():
    return jsonify(albums)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)