import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt


# set client credentials flow - environmental variable SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=auth_manager)
# Playlist URI as environmental variable
PLAYLIST_URI = os.environ["spotify_playlist"]
SPOTIPY_MAX_LIMIT = 100


playlist_songs_offset = 0
all_songs_collected = False
unsorted_year_dict = {}

while all_songs_collected is False:
    # Query songs (tracks) in playlist with max limit of 100
    playlist_response = spotify.playlist_items(PLAYLIST_URI, limit=SPOTIPY_MAX_LIMIT, offset=playlist_songs_offset)
    # Increment offset by max limit to collect tracks not yet queried
    playlist_songs_offset += SPOTIPY_MAX_LIMIT

    # If all tracks have been queried, returned response will be empty (no songs)
    if len(playlist_response["items"]) == 0:
        # end query
        all_songs_collected = True
    # response contains songs
    else:
        for track in playlist_response["items"]:
            # Release date of album the track belongs to found in track["track"]["album"]["release_date"]
            # Date exists as string (eg 2005 or 2005-10-19)-> get the first 4 characters for year
            song_year = track["track"]["album"]["release_date"][0:4]
            # track number of songs from each year via unsorted_year_dict. Increment of value. {"year": number_of_songs}
            # Disregard songs with song_year 0000 -> missing data
            if song_year in unsorted_year_dict and song_year != "0000":
                unsorted_year_dict[song_year] += 1
            else:
                unsorted_year_dict[song_year] = 1

# Sort resultant dictionary for the first time
year_dict = {}
for key in sorted(unsorted_year_dict):
    year_dict[key] = unsorted_year_dict[key]


# Gather list of years to see what years are missing (no songs from that year)
year_list = list(year_dict.keys())
# Fill in years without songs - number of songs: 0
first_year = year_list[0]
last_year = year_list[len(year_list)-1]
for x in range(int(first_year), int(last_year) + 1):
    if str(x) not in year_dict:
        year_dict[str(x)] = 0

# Re-sort after adding missing years
song_numbers = {}
for key in sorted(year_dict):
    song_numbers[key] = year_dict[key]
# Separate keys and values into two list for plotting with matplotlib bar chart
year_list = list(song_numbers.keys())
number_list = list(song_numbers.values())


# Draw Bar Chart - Number of songs by release year
# Spotify colour: "#1DB954"
plt.figure(figsize=[12, 6])
plt.style.use('dark_background')
plt.bar(x=year_list, height=number_list, color="#1DB954")
plt.xlabel("Year")
plt.xticks(rotation=45)
plt.ylabel("Number of Songs")
plt.title("Number of Songs By Release Year In Playlist")
plt.show()