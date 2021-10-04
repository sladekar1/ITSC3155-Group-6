import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# No filtering necessary
# Removing empty spaces from first column to prevent errors
# Note: Removing this does nothing right now, but I'm still too scared to do so
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of Total medals group by NOC Column
new_df = df.groupby(['NOC'])['Total'].sum().reset_index()

# Sorting values and select first 20 NOCs
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Preparing layout
layout = go.Layout(title='Rio 2016 Olympics Medals by Nation/Country', xaxis_title="Nations/Countries",
                   yaxis_title="Olympic Medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
