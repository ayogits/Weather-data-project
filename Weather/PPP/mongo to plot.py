from pandas.io.json import json_normalize
from pandas import DataFrame, Series
import numpy as np
import plotly.tools as tls
import cufflinks as cf
import pandas as pd
import plotly.plotly as py
import plotly
from pymongo import MongoClient

plot_api = 'il8uhkce0f'
plot_username = 'hemeshpatel91'
plotly.tools.set_credentials_file(username=plot_username, api_key=plot_api)

client = MongoClient()
db = client.project
cursor = db.weather.find()

date = []
weather_info = []
for document in cursor:
    d = document['SiteRep']['DV']['dataDate'][:10]
    date.append(d)
    i = document['SiteRep']['DV']['Location']['Period']
    weather_info.append(i)

result = json_normalize(weather_info[0], 'Rep', ['value'])

df2 = DataFrame(result, columns=['value', 'Pp'])
df2[['Pp']] = df2[['Pp']].astype(int)

#Below is a sample of the above data being represented in plotly

group = DataFrame(df2.groupby('value')['Pp'].mean())
print group
plot = py.iplot([{
   'x': group.index,
    'y':group[col],
    'name': col
}for col in group.columns], filename='basic-line')
#print plot #This saves the graph to my plotly account(hemesh)