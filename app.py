import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['POST'])
def post_albums():
    if(has_invalid_album_parameters(request.form)):
        return "You need to submit a title, release year and artist id",400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None,
                  request.form['title'],
                  request.form['release_year'],
                  request.form['artist_id'])
    repository.create(album)
    return '',200

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    #albums = repository.all()
    return "\n".join(
        f"{album}" for album in repository.all()
    )
def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form or \
        'artist_id' not in form


#For Artists.....
@app.route('/artists', methods=['POST'])
def post_artists():
    if 'name' not in request.form or 'genre' not in request.form:
        return "You need to submit a name, and genre",400
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None,
                  request.form['name'],
                  request.form['genre']
    )
    repository.create(artist)
    return '',200

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    #albums = repository.all()
    return "\n".join(
        f"{artist}" for artist in repository.all()
    )




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

