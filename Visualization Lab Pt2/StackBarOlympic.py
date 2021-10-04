import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')


# Sorting values and select first 20 Country
new_df = df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data

gold=go.Bar(x=new_df["NOC"], y=new_df["Gold"], name="Gold", marker={"color":"#FFC512"})
silver=go.Bar(x=new_df["NOC"], y=new_df["Silver"], name="Silver", marker={"color":"#738595"})
bronze=go.Bar(x=new_df["NOC"], y=new_df["Bronze"], name="Bronze", marker={"color":"#b66325"})
data = [gold, silver, bronze]


# Preparing layout
layout = go.Layout(title='Total  Gold, Silver, Bronze medals of Olympic 2016',
                   xaxis_title="Country", yaxis_title="Total Medal", barmode="stack")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')
