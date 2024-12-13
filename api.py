import spotipy
from spotipy.oauth2 import SpotifyOAuth
import asyncio
from dataclasses import dataclass, field
import random
import configparser

config = configparser.ConfigParser()
config.read(".config")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(**config["SETTINGS"]))

@dataclass
class Track:
    name: str
    __artists: list[dict] = field(repr=False)
    artist: str = field(init=False,repr=True)

    def __post_init__(self):
        self.artist = " & ".join([artist["name"] for artist in self.__artists])


@dataclass
class Playlist:
    url:str
    name:str
    tracks: list[Track] = field(repr=False)
    image:str = field(repr=False)

    def sample(self,k:int)->list[Track]:
        ''''
        Returns a k-sized sample of unique tracks in the playlist.

        params: k:int
        returns: list[Tracks]
        '''
        return random.sample(self.tracks,k)


async def fetch_title(url:str)->str:
    return sp.playlist(url,fields="name")["name"]


async def fetch_tracks(url:str)->list[Track]:
    items = sp.playlist_items(url,fields="items.track.name,items.track.artists.name")["items"]
    return [Track(item["track"]["name"],item["track"]["artists"]) for item in items]


async def fetch_image(url:str)-> str:
    '''
    Returns the url of the playlist image with the biggest size width*height
    '''
    images = sp.playlist(url, fields="images")["images"]
    max_width, max_height = max([image["width"] for image in images]),max([image["height"] for image in images])
    for image in images:
        if image["width"]*image["height"] == max_width*max_height:
            return image["url"]


async def fetch(url):
    '''
    Returns the playlist via concurrently fetching its title, tracks and image from the Spotify API.

    params: url:str
    returns: Playlist

    usage: var = asyncio.run(this(*args,**kwargs))
    '''
    #Fetch data concurrently
    title,tracks,image = await asyncio.gather(fetch_title(url), fetch_tracks(url), fetch_image(url))

    return Playlist(url,title,tracks,image)


if __name__ == "__main__":
    pass
    #url = "https://open.spotify.com/playlist/7lGXkwFp0fZAISz9ZhnRa8"
    #playlist = asyncio.run(fetch(url))
    #print(playlist)
