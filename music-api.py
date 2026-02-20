from flask import Flask, jsonify

app = Flask(__name__)

songs = [
    {"id": 1, "title": "Imagine", "artist": "John Lennon", "album": "Imagine"},
    {"id": 2, "title": "Billie Jean", "artist": "Michael Jackson", "album": "Thriller"},
    {"id": 3, "title": "Bohemian Rhapsody", "artist": "Queen", "album": "A Night at the Opera"}
]

@app.route('/songs', methods=['GET'])
def get_songs():
    return jsonify(songs)

@app.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
    song = next((s for s in songs if s["id"] == song_id), None)
    return jsonify(song) if song else (jsonify({"error": "Canción no encontrada"}), 404)

@app.route('/artists', methods=['GET'])
def get_artists():
    artists = list(set([s["artist"] for s in songs]))
    return jsonify(artists)

@app.route('/albums', methods=['GET'])
def get_albums():
    albums = list(set([s["album"] for s in songs]))
    return jsonify(albums)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)