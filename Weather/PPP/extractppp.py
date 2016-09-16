import json
from pandas.io.json import json_normalize
from pandas import DataFrame, Series
import pyodbc
import numpy as np

cnx = pyodbc.connect('DSN=Kubrick')
cursor = cnx.cursor()

cursor.execute('select * from [dbo].[weather]')
row = cursor.fetchall()

date = []
data = []
for i in row:
    row1 = i
    rowx = row1[1]
    r = json.loads(rowx)
    data.append(r)
    date.append(r['SiteRep']['DV']['dataDate'][:10])#  This extracts the date of when the information was collected

extraction_date = date[0]
path = data[0]['SiteRep']['DV']['Location']['Period']#  This is the path to the dates, times and weather info in a list format. Each element in list is a different day.

result = json_normalize(path, 'Rep', ['value'])


#df2 = DataFrame(result, columns=['$', 'Pp', 'value'])
#print df2


df2 = DataFrame(result, columns=['value', 'Pp'])
df2[['Pp']] = df2[['Pp']].astype(int)
print df2
#Trying to change the data type of pp to int
#df3 = DataFrame(df2['value'], df2['Pp'].astype(int))
#print df3[['Pp', 'value']]

group = df2.groupby('value')['Pp'].mean()
print group
#Done