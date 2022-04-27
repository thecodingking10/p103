import pandas as pd
import plotly.express as px

df = pd.read_csv("D:/DATA DESKTOP/Notes Of Code/Python/Homework/Pro-C103DataVisualization/covid-19.csv")
fig = px.scatter(df, x="date", y="cases", color="country")
fig.show()