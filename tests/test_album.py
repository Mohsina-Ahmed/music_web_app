from lib.album import Album
'''
Construct with id, title, release year and artist id
'''

def test_constructor():
    album = Album(1, "Test Album", 2001, 1)
    assert album.id ==1
    assert album.title == "Test Album"
    assert album.release_year == 2001
    assert album.artist_id == 1

'''
Albums with equal contents are equal
'''

def test_compares():
    album_1 = Album(1, "Test Title", 2000, 1)
    album_2 = Album(1, "Test Title", 2000, 1)
    assert album_1 == album_2

'''
Albums can be represented as strings
'''

def test_stringifying():
    album_1 = Album(1, "Test Title", 2000, 1)
    assert str(album_1) == "Album(1, Test Title, 2000, 1)"