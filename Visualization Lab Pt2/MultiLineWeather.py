import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

df["month"]=df.groupby(['month']).agg( {"actual_max_temp":"sum", "actual_min_temp": "sum",
                                        "actual_mean_temp": "sum"}).reset_index()

# Preparing data
maxim=go.Scatter(x=df["month"], y=df["actual_max_temp"], mode="lines", name="Max Temperature")
minim=go.Scatter(x=df["month"], y=df["actual_min_temp"], mode="lines", name="Min Temperature")
aver=go.Scatter(x=df["month"], y=df["actual_mean_temp"], mode="lines", name="Mean Temperature")
data=[maxim, minim, aver]

# Preparing layout
layout = go.Layout(title='Max, Min and Mean temperature of each month', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')
