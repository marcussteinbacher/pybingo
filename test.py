import api
import asyncio
from parser import html_card

url = "https://open.spotify.com/playlist/7lGXkwFp0fZAISz9ZhnRa8?si=EyFGZXTcQ--W-KQOPZOgHA"

playlist = asyncio.run(api.fetch(url))

#print(playlist.name)
#print(playlist.tracks[0].name,playlist.tracks[0].artist)
#print(playlist.sample(16))

#print(pd.DataFrame(np.array([track.name for track in playlist.sample(16)]).reshape((4,4))))

print(html_card(playlist.sample(16)))

cards = [html_card(playlist.sample(16)) for _ in range(10)]

# from jinja2 import Environment, FileSystemLoader

# environment = Environment(loader=FileSystemLoader("templates/"))
# template = environment.get_template("template.html")

# context = {
#     "playlist": playlist,
#     "cards": cards
# }

# with open("public/index.html", mode="w", encoding="utf-8") as file:
#     file.write(template.render(context))