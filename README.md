<h1 align="center">Finding Out My Musical Taste</h1>
<h3 align="center">Retrieving the release date of songs in my Spotify playlist and putting them in a bar chart</h3>
<br>

<!--Introduction-->
<h4>Introduction</h4>
While on a long drive overseas, I played my Spotify playlist via bluetooth in the car and it started to feel like many of the songs seemingly come from a similar era. To find the answer, and with the aid of Python, I queried Spotify's API for the release dates of the songs in the playlist and put them into a bar chart.

Studies indicate that music tastes are generally formed during the teenage years. The results will be an interesting comparison to see what time period the majority of my songs in the playlist come from.
<br>
<br>
<!--Built With: Language and Packages-->
<h4>Built With</h4>
**Language:** Python
<br>
**Packages:** Spotipy, Matplotlib
<br>
<br>
<!--Methodology Issues-->
<h4>Further Details & Caveats</h4>
1. Spotify API does not directly provide the release date of the song, but rather the release date of the album the song belongs to and may not be the release year of the song itself. The song's release year and album release year can be different due to the following reasons:
     - The song was released before the album was released (and in different year)
     - The song in the playlist may be attached to later compilation albums, data was not cleaned to ensure that the album attached to the song is the original album
2. In my execution of the script, only my chinese language playlist was included in the test. Therefore, the results can only be indicative of my music taste with regards to chinese (and dialects) music.
3. The number of songs from each year only acts as a proxy for musical taste. One can also take into account proportion of playtime to further improve accuracy.
4. Musical taste in this execution is sorted by release year rather than genre.
<br>
<br>
<!--Results-->
<h4>Results</h4>
*Results as of 29 October 2022:*

![bar_chart_20221029](https://user-images.githubusercontent.com/60059807/198825858-33f7c544-ac9b-4d32-ae13-e51c24a5e74d.png)


Most songs are found to be released from year 2004 to 2016, with the highest peak in 2013 and 2014. Year 2004 to 2016 correspond to significant landmark events in my life:
- 2004 being the last year of primary school, with 2005 being the first year in secondary school, with significantly more freedom afforded. It is possible that songs from the previous year were more in-the-mind during that period
- 2016 is the last year before entering the workforce. Presumably after entering the workforce one has less time to be in tune with the latest music
- 2013 and 2014 correspond to age 21 and 22, which is slightly different from the oft-quoted teenage years of 13-16 (for males)
