# Tests for your routes go here
'''
When I call #get album
I get list of album back
'''
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ""\
        "Album(1, The Cold Nose, 2008, 1)"

'''
When I call POST/albums with albums info
That album is now in the list of GET/ albums
'''
def test_post_submit(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'In Ear Park',
        'release_year': '2008',
        'artist_id': '1'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ""\
        "Album(1, The Cold Nose, 2008, 1)\n"\
        "Album(2, In Ear Park, 2008, 1)"

'''
When I call POST/albums with no data
I get error
'''
def test_post_submit(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == ""\
        "You need to submit a title, release year and artist id"
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ""\
        "Album(1, The Cold Nose, 2008, 1)"


'''
When I call #get artist
I get list of artist back
'''
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ""\
        "Artist(1, Pixies, Rock)\n"\
        "Artist(2, ABBA, Pop)\n"\
        "Artist(3, Taylor Swift, Jazz)\n"\
        "Artist(4, Nina simone, Jazz)"

'''
When I call POST/artists with artists info
That album is now in the list of GET/ artists
'''
def test_post_submit_artist(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/artists", data={
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ""\
        "Artist(1, Pixies, Rock)\n"\
        "Artist(2, ABBA, Pop)\n"\
        "Artist(3, Taylor Swift, Jazz)\n"\
        "Artist(4, Nina simone, Jazz)\n"\
        "Artist(5, Wild nothing, Indie)"
    
'''
When I call POST/artists with no data
I get error
'''
def test_post_submit(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/artists")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == ""\
        "You need to submit a name, and genre"
    
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ""\
        "Artist(1, Pixies, Rock)\n"\
        "Artist(2, ABBA, Pop)\n"\
        "Artist(3, Taylor Swift, Jazz)\n"\
        "Artist(4, Nina simone, Jazz)"\
        
       
    
