import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by Month Column
new_df=df.groupby(['month'])

# Preparing data
data= [
    go.Scatter( x=new_df["average_max_temp"].mean(), y=new_df["average_min_temp"].mean(), text=df["month"].unique(),
               mode="markers",
               marker=dict(size=70, color=new_df["average_max_temp"].sum()/100,  showscale=True))
]


# Preparing layout
layout = go.Layout(title='Average Max, Min temperature of each month', xaxis_title="Max",
                   yaxis_title="Min", hovermode="closest")


# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubbleweather.html')

