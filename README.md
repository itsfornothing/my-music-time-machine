# my-music-time-machine

Billboard to Spotify Playlist Creator
This Python script allows you to create a Spotify playlist of the Billboard Hot 100 songs for a specified date. It scrapes the Billboard website for the top 100 songs on the given date and adds them to a new Spotify playlist.

Prerequisites
Before running this script, you need to have the following:

Python 3.x installed on your system.
A Spotify account.
Spotify Developer credentials (Client ID and Client Secret).
Libraries Used
The script uses the following libraries:

requests: For making HTTP requests to fetch the Billboard webpage.
beautifulsoup4: For parsing the HTML content of the Billboard webpage.
spotipy: For interacting with the Spotify API.
datetime: For handling date inputs.

Setup
Install Required Libraries

Run the following command to install the required libraries:

bash
Copy code
pip install requests beautifulsoup4 spotipy
Spotify Developer Credentials

Obtain your Spotify Developer credentials by creating an application on the Spotify Developer Dashboard. Note down the Client ID, Client Secret, and set the Redirect URI to http://my-example.com.

Update the Script

Replace the placeholders in the script with your actual Spotify credentials:

python
Copy code
client_id = "YOUR_SPOTIFY_CLIENT_ID"
client_secret = "YOUR_SPOTIFY_CLIENT_SECRET"
redirect_uri = "http://my-example.com"
username = 'YOUR_SPOTIFY_USERNAME'
Usage
Run the Script

Run the script using Python:

bash
Copy code
python billboard_to_spotify.py
Input the Date

When prompted, input the date for which you want to fetch the Billboard Hot 100 songs. The date format should be YYYY/MM/DD.

Playlist Creation

The script will:

Fetch the top 100 songs from Billboard for the specified date.
Create a new private playlist on your Spotify account with the name YYYY-MM-DD Billboard 100.
Add the fetched songs to the created playlist.
Example
Here's an example of running the script:

bash
Copy code
$ python billboard_to_spotify.py
What year would you like to travel to: 2003/08/15
2003-08-15
['Officially Missing You', 'Crazy in Love', 'Right Thurr', ...]
Created playlist: 2003-08-15 Billboard 100 - https://open.spotify.com/playlist/3C68tlYO1pg9FS4gNO4gQF
YOUR_SPOTIFY_USER_ID
Error Handling
If a song from the Billboard list is not found on Spotify, it will be skipped, and a message will be printed.
