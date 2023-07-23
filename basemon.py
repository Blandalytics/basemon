import streamlit as st
import pandas as pd
import numpy as np
import urllib
from PIL import Image
header = Image.open(urllib.request.urlopen('https://github.com/Blandalytics/basemon/blob/main/basemon%20logo.png?raw=true'))
col1, col2, col3 = st.columns([0.1,0.8,0.1])
with col1:
    st.write(' ')

with col2:
    st.image(header)

with col3:
    st.write(' ')

generations = ['Gen2']
poke_gen = st.radio('Choose a generation of Pokémon:', generations)
@st.cache_data
def load_players():
    return list(pd.read_csv('https://github.com/Blandalytics/basemon/blob/main/data/baseball_pokemon_Gen2.csv?raw=true', encoding='latin1').sort_values('full_name')['full_name'].unique())
players = load_players()

# Player
default_ix = players.index('Dustin May')
player = st.selectbox('Select a player:', players, index=default_ix)

card_loc = f"https://github.com/Blandalytics/basemon/blob/main/basemon_cards/{poke_gen}/{player.replace(' ','%20')}-{poke_gen}.png?raw=true"
basemon_card = Image.open(urllib.request.urlopen(card_loc))
st.image(basemon_card)

st.write("Make sure to subscribe to [PitcherList Pro](https://www.pitcherlist.com/premium/) for more content like this!")
