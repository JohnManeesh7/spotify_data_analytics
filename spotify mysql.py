import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='149206559cba46f19c47665db8b2c01c',
    client_secret='2c4a4f533e514f84ac761b2ad6aa180e'
))

# MySQL Database Connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345$',
    'database': 'spotify'
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


artist_url = "https://open.spotify.com/artist/1Clwe5e4xyRasANUVlpcCf"

# Extract track ID directly from URL
artist_id = re.search(r'artist/([a-zA-Z0-9]+)', artist_url).group(1)

# Fetch track details
artist = sp.artist(artist_id)

# Extract metadata
artist_data = {
    'artist Name': artist['name'],
    'genres': artist['genres'][0],
    'Popularity': artist['popularity'],
    'followers': artist['followers']['total']
}

# Insert data into MySQL
insert_query = """
INSERT INTO spotify_artist (artist_name, genres, popularity, followers)
VALUES (%s, %s, %s, %s)
"""
cursor.execute(insert_query, (
    artist_data['artist Name'],
    artist_data['genres'],
    artist_data['Popularity'],
    artist_data['followers']
))
connection.commit()

print(f"artist '{artist_data['artist Name']}' by {artist_data['genres']} inserted into the database.")

# Close the connection
cursor.close()
connection.close()
