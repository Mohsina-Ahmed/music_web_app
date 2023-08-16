# Single Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of albums' release years.
```

```
Nouns:

album, title, release year, artist, id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                         |
| --------------------- | -----------------------------------|
| album                 | id, title, release year, artist_id |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`, `artist_id`, `id`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);

```

## 5. Create the table

```bash
psql -h 127.0.0.1 record_store < albums_table.sql
```

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```

# Submit message route
POST /albums
  title: string
  release_year: number (str)
  artist_id: number (str)

# Submit message route
POST /artists
  name: string
  genre: string

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# Scenario 1
"""
I am going to create an album entry
"""

    # POST /albums
    #  Parameters:
    #    title: "In Ear Park"
    #    release_year: 2008
    #    artist_id: 1
    #  Expected response (200 OK):
    """
    (no content)
    """

    # GET /albums
    #  Parameters: none
    #  Expected response (200 OK):
    """
    Album (1, The Cold Nose, 2008, 1)
    Album (2, In Ear Park, 2008, 1)
    """

# Scenario 1
"""
I am going to create an artist entry
"""

    # POST /artists
    #  Parameters:
    #    name: "Wild nothing"
    #    genre: Indie
    #  Expected response (200 OK):
    """
    (no content)
    """

    # GET /artists
    #  Parameters: none
    #  Expected response (200 OK):
    """
    Artist (1, Pixies, Rock)
    Artist (2, ABBA, Pop)
    Artist (3, Taylor Swift, Jazz)
    Artist (4, Nina simone, Jazz)
    Artist (5, Wild nothing, Indie)
    """

# Scenario 2
"""
I am going to send an empty album entry
"""

    # POST /albums
    #  Expected response (400 Bad Request):
    """
    You need to submit a title, release_year and artist_id
    """

    # GET /albums
    #  Parameters: none
    #  Expected response (200 OK):
    """
    Album (1, The Cold Nose, 2008, 1)
    """

# Scenario 2
"""
I am going to send an empty artist entry
"""

    # POST /artists
    #  Expected response (400 Bad Request):
    """
    You need to submit a name, and genre
    """

    # GET /artists
    #  Parameters: none
    #  Expected response (200 OK):
    """
    Artist (1, Pixies, Rock)
    Artist (2, ABBA, Pop)
    Artist (3, Taylor Swift, Jazz)
    Artist (4, Nina simone, Jazz)
    """
```




## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->