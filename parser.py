from api import Track
import numpy as np 
import pandas as pd
import math as m
from dataclasses import asdict

def html_card(tracks:list[Track], how:str="artist")->str:
    """
    Generates a single bingo card as a html table of size: size x size.
    tracks: A list of api.Track instances
    size:int: Integer specifying the size of the bingo card, i.e. n x n. or str "auto" that automatically
    sets n depending on the number of api.Tracks.
    how:str["artist"|"name"]: String "artist" or "name" that specifies whether to create fields to 
    guess a tracks artist or its title "name".
    """
   
    size = int(m.sqrt(len(tracks)))

    df = pd.DataFrame(np.array([asdict(track)[how] for track in tracks]).reshape((size,size)))
    return df.to_html(header=False,index=False)