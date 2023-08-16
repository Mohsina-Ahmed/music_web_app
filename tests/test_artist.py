from lib.artist import Artist
'''
get an artist constructor
'''

def test_constructor():
    artist = Artist(1, "Test Artist", "Test genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test genre"

'''
Two Artist objects with same value 
should be same
'''
def test_equality():
    artist_1 = Artist(1, "Test Artist", "Test genre")
    artist_2 = Artist(1, "Test Artist", "Test genre") 
    assert artist_1 == artist_2


'''
To do the string representation of Artist
'''

def test_format():
    artist = Artist(1, "Test Artist", "Test genre")
    assert str(artist) == "Artist(1, Test Artist, Test genre)"