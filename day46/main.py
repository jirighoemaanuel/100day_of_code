from spotipy.oauth2 import SpotifyOAuth
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os
import datetime
load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")


date = str(datetime.datetime.today() - datetime.timedelta(days=3)).split()[0]
# date = input(
#     "What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

# Use the complete class name in tag_class
tag_class = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

song_titles = []
for song_tag in soup.find_all(name="h3", class_=tag_class):
    song_titles.append(song_tag.getText().strip())

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://example.com",
                                               scope=scope))


songs_url = []
# print(sp.current_user()["id"])
for song in song_titles:
    query = f"track: {song} year: {date[0:4]}"
    results = sp.search(q=query, type="track")
    if results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        song_url = track["external_urls"]["spotify"]
        songs_url.append(song_url)
    else:
        print("Song not found.")


def create_and_add_songs_to_playlist(sp, playlist_name, song_urls):
    """Creates a playlist with the given name and adds songs from the provided URLs."""

    # Create the playlist
    playlist = sp.user_playlist_create(
        user=sp.current_user()["id"], name=playlist_name, public=True)
    playlist_id = playlist["id"]

    # Extract track IDs from URLs
    track_ids = [url.split("/")[-1] for url in song_urls]

    # Add songs to the playlist
    sp.playlist_add_items(playlist_id=playlist_id, items=track_ids)

    print(f"Playlist '{playlist_name}' created and songs added successfully!")


# Example usage
playlist_name = f"{date} Billboard 100"
create_and_add_songs_to_playlist(sp, playlist_name, songs_url)
