import pandas as pd
import requests

url = "https://www.ss.com/lv/real-estate/flats/riga/centre/hand_over/"

df = pd.read_html(url)[4]  # 5th table
df.to_csv("flats.csv")