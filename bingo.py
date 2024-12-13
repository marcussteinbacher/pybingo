from jinja2 import Environment, FileSystemLoader
import api
import asyncio
from parser import html_card
import argparse
from spotipy.exceptions import SpotifyException
from urllib3.exceptions import HTTPError
import webbrowser

parser = argparse.ArgumentParser()
parser.add_argument("url",type=str,help="Spotify public playlist URL")
parser.add_argument("-s","--size",type=int,default=4,help="Bingo card size, e.g. --size 4 yields 4x4 cards. Default: size:int=4")
parser.add_argument("-p","--players",type=int,default=20,help="Number of players, i.e. the number of cards to be rendered. Default: players:int=20")
parser.add_argument("--how",type=str,choices=["artist","name"],default="artist",help="Decide whether to guess a songs artist or name. Default: how:str='artist'")

args = parser.parse_args()

#print(args)

environment = Environment(loader=FileSystemLoader("templates/"))
#template = environment.get_template("col_template.html")
template = environment.get_template("grid_template.html")

#TODO
try:
    playlist = asyncio.run(api.fetch(args.url))
except SpotifyException as se:
    raise se
except HTTPError as he:
    raise he
else:
    print("Playlist Fetched!")

size = args.size**2
players = args.players 
how = args.how 
cards = [html_card(playlist.sample(size),how=how) for _ in range(players)]

context = {
    "playlist": playlist,
    "cards": cards
}

with open("public/index.html", mode="w", encoding="utf-8") as file:
    file.write(template.render(context))

print("Finished! Created file 'public/index.html'!")

try:
    webbrowser.open("public/index.html")
except webbrowser.Error:
    print("Please navigate to public/index.html.")