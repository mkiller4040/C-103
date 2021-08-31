import pandas as pan
import plotly.express as plot

data = pan.read_csv("data.csv")

graph = plot.scatter(data, 
                     x = "date", 
                     y = "cases", 
                     color = "country", 
                     title = "Number of Covid Cases",
                     )

graph.show()