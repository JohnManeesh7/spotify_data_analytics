from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

# Set up Client Credentials
    client_id='149206559cba46f19c47665db8b2c01c',
    client_secret='2c4a4f533e514f84ac761b2ad6aa180e'
))

artist_url = "https://open.spotify.com/artist/1mYsTxnqsietFxj1OgoGbG"

# Extract track ID directly from URL using regex
artist_id = re.search(r'artist/([a-zA-Z0-9]+)', artist_url).group(1)
# Fetch track details
artist= sp.artist(artist_id)
print(artist)
# Extract metadata
artist_data = {
    'artist Name': artist['name'],
    'genres': artist['genres'][0],
    'Popularity': artist['popularity'],
    'followers': artist['followers']['total']
}

# Display metadata
print(f"\nartist Name: {artist_data['artist Name']}")
print(f"genres: {artist_data['genres']}")
print(f"Popularity: {artist_data['Popularity']}")
print(f"followers: {artist_data['followers']:.2f} ")

# Convert metadata to DataFrame
df = pd.DataFrame([artist_data])
print("\nartist Data as DataFrame:")
print(df)

# Save metadata to CSV
df.to_csv('spotify_artist_data.csv', index=False)

# Visualize track data
features = ['Popularity', 'followers']
values = [artist_data['Popularity'], artist_data['followers']]

plt.figure(figsize=(8, 5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"artist Metadata for '{artist_data['artist Name']}'")
plt.ylabel('Value')
plt.show()

# Fetch track details
artist = sp.artist(artist_id)
print(artist)
