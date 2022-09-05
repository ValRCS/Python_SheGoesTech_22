import pandas as pd
import numpy as np
import random

df = pd.read_excel("tieto_evry_participants.xlsx")
df = df[df["Surname"] != "Imbrass"]
print(df.shape)
participants = df.values.tolist()
print(participants)
# pure python shuffle
random.seed(221021)  # removing this will create a random shuffle
random.shuffle(participants)  # IN PLACE !!!
print(participants)

np.random.seed(221021)  # if we comment out this line we will get random every time
# pandas way
df = df.sample(frac=1).reset_index(drop=True)
df.to_excel("tieto_team_pairs.xlsx")
print(df.to_string())