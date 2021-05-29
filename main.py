import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
mean = df.groupby("level"), ["attempt"].mean()
figure = px.scatter(mean, x = "student_id", y = "level", size = "attempt", color="attempt")
figure.show()
