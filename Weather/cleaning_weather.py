import json
from pandas.io.json import json_normalize
from pandas import DataFrame, Series
import pyodbc

cnx = pyodbc.connect('DSN=Kubrick')
cursor = cnx.cursor()

cursor.execute('select * from [dbo].[weather]')
row = cursor.fetchall()
print type(row)

info = []
for i in row:
    r = json.loads(i)
    info.append(r)
print type(info)



#t1 = Series(info, name='SiteRep')
#print t1
#for i in row:
#    print i
#    with open('outputfilename.json', 'wb') as outfile:
#        json.dump(i, outfile)

#weather_file = 'outputfilename.json'
#with open(weather_file) as fhand:
#    data = json.load(fhand)
#    print type(dict(data))
#print dict(data)
#print type(data)
#path = data['SiteRep']['DV']['Location']['Period'] # This is the path to the dates, times and weather info in a list format. Each element in list is a different day.
#print path
#result = json_normalize(path, 'Rep', ['value'])
#print result

#day = path[0]['Rep'][0]['$'] # This gives weather info on the whole day
#print day

#print type(result)
#df2 = DataFrame(result, columns =['$','Pp', 'W', 'value'])
#df2['index'] = range(1,len(df2)+1)
#print df2
#df3 = df2.set_index('index').T.to_dict('list')
#print df3

#df4 = DataFrame(result, columns =['$', 'W', 'value'])
#df4['index'] = range(1,len(df2)+1)
#print df4





