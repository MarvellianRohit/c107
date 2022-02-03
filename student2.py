import csv
import pandas as pd
import plotly.graph_objects as go

bf = pd.read_csv("data.csv")
studentdf = bf.loc[bf["student_id"]=="TRL_abc"]

fig  = go.Figure(go.Bar(
    x = studentdf.groupby("level")["attempt"].mean(),
    y = ["Level 1","Level 2","Level 3", "Level 4"],
    orientation = "h"
))

fig.show()