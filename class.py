import csv
import pandas as pd
import plotly.graph_objects as go

bf = pd.read_csv("data.csv")
print(bf.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = bf.groupby("level")["attempt"].mean(),
    y = ["Level 1","Level 2","Level 3","Level 4"],
    orientation = "h"
))

fig.show()