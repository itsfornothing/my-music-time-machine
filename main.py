from datetime import datetime
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Replace with your actual client ID, client secret, and redirect URI
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
playlist_id = ""

# Set up the Spotify OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-private"))

input_time = input("what year you would like to travel to:")

Date = datetime.strptime(input_time, '%Y/%m/%d').date()
print(Date)
URL = "https://www.billboard.com/charts/hot-100"
response = requests.get(f"{URL}/{Date}")
response.raise_for_status()

billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")
music_title = soup.find_all(name="h3", class_="a-no-trucate")

music_list = [music.text.replace("\t", "").replace("\n", "") for music in music_title]


print(music_list)


##  Create the playlist
def create_playlist(username, playlist_name, description=""):
    playlist = sp.user_playlist_create(user=username, name=playlist_name, public=False, description=description)
    global playlist_id
    playlist_id = playlist["id"]
    return playlist


username = os.getenv("USERNAME")
playlist_name = f'{Date} Billboard 100'
description = 'This is a new playlist created using Spotipy.'

new_playlist = create_playlist(username, playlist_name, description)
print(f"Created playlist: {new_playlist['name']} - {new_playlist['external_urls']['spotify']}")
user_id = sp.current_user()["id"]


song_uris = []

for song in music_list:
    result = sp.search(q=f"track:{song} year:{2003}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Add tracks to the specified playlist
sp.playlist_add_items(playlist_id, song_uris, position=None)
