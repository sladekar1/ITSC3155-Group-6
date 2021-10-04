import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Getting data for max/min/mean
max_df = df.groupby(by="month", sort=False)["actual_max_temp"].max().reset_index()
min_df = df.groupby(by="month", sort=False)["actual_min_temp"].min().reset_index()
mean_df = df.groupby(by="month", sort=False)["actual_mean_temp"].mean().reset_index()

# Preparing data
trace1 = go.Scatter(x=max_df['month'], y=max_df['actual_max_temp'], mode='lines', name='Max Temperature')
trace2 = go.Scatter(x=min_df['month'], y=min_df['actual_min_temp'], mode='lines', name='Min Temperature')
trace3 = go.Scatter(x=mean_df['month'], y=mean_df['actual_mean_temp'], mode='lines', name='Mean Temperature')
data = [trace1, trace2, trace3]


# Preparing layout
layout = go.Layout(title='Max, Min, and Monthly Temperature from July 2014 to June 2015', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')