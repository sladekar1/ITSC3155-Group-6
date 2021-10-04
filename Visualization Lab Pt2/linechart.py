import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Note: I had to look at the panda docs for sort. This stumped me for HOURS.
new_df = df.groupby(by="month", sort=False)["actual_max_temp"].max().reset_index()

# Preparing data
data = [go.Scatter(x=new_df['month'], y=df['actual_max_temp'], mode='lines', name='Max Temperature')]

# Preparing layout
layout = go.Layout(title='Max Monthly Temperature from July 2014 to June 2015', xaxis_title="Month",
                   yaxis_title="Max Temperatrue")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')