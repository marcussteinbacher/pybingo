# Pybingo
*Create randomized bingo cards from your spotify playlist*

![Single Card](assets/card.png)

## What 
Create a html with a specified number of music bingo cards from a public spotify playlist to easily print and play on paper.

## Setup

>This application depends on the fantastic [spotipy](https://github.com/spotipy-dev/spotipy) package, a light-weight library for the Spotify Web API.

Interacting with the Spotify Web API requires to set up a Spotify developer account and initialize a project. Follow the [Spotipy Tutorial](https://github.com/spotipy-dev/spotipy/blob/2.22.1/TUTORIAL.md), i.e.

- [1] Create Spotify developer account
- [2] Add a new application on your Spotify developer dashboard
- [3] Navigate to the application settings and enter a 'Redirect URI', e.g. http://localhost:8080
- [4] Create a .config file in the root directory, i.e. where your `bingo.py` is located at,

```bash
cd bingo 
touch .config
```

Open `.config` and add the section `[SETTINGS]` with your Spotify Credentials,

```
[SETTINGS]
CLIENT_ID = your_client_id
CLIENT_SECRET = your_client_secret
REDIRECT_URI = https://localhost:8080
SCOPE = user-library-read
```

## Usage
cd into the root directory and run `bingo.py`,

```bash
cd bingo 
python bingo.py --help
```
to see all options.

## Example
Creating 30 bingo cards, each consiting of 4x4 songs, guessing the artist,

```bash
python bingo.py "url" --players 30 --size 4 --how artist
```

![Usage](assets/usage.gif)

This will create the file `public/index.html` that can be printed using your browsers print context menu.

> The first execution might ask you to authenticate your app with your Spotify developer account. Open the link that was generated in your preferred browser and copy the URL that it was redirected to into the terminal when asked.