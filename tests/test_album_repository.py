from lib.album_repository import AlbumRepository
from lib.album import Album
'''
When I call #all
I get all the albums in the album table
'''
def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [
        Album(1, "The Cold Nose", 2008, 1)
    ]
'''
When I call #create
I create an album in the database
and I see it in #all
'''
def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test album", 2000, 2)
    repository.create(album)
    result = repository.all()
    assert result == [
        Album(1, "The Cold Nose", 2008, 1),
        Album (2, "Test album", 2000, 2)
    ]

 