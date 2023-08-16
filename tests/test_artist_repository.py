from lib.artist_repository import ArtistRepository
from lib.artist import Artist
'''
when I call #all for artist
I should see all of the artists
'''
def test_artist_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Jazz"),
        Artist(4, "Nina simone", "Jazz")
    ]

'''
When I create a new artist
and I call #all 
I see all the artists with new artist entry
'''

def test_create_artist(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "Test artist2", "test genre")
    assert repository.create(artist) == None
    assert repository.all() == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Jazz"),
        Artist(4, "Nina simone", "Jazz"),
        Artist(5, "Test artist2", "test genre")
    ]