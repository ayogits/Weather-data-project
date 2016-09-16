import json
from pandas.io.json import json_normalize
from pandas import DataFrame, Series
import pyodbc

cnx = pyodbc.connect('DSN=Kubrick')
cursor = cnx.cursor()

cursor.execute('select * from [dbo].[weather]')
row = cursor.fetchall()
dates = []
info = []
#print len(rows)

weather =[]
n = 0
while n<=5:
    for i in row:
        row1 = i
        rowx = row1[1]
        r = json.loads(rowx)
        dataDate = r['SiteRep']['DV']['dataDate']
        dicts = (r['SiteRep']['DV']['Location']['Period'][0])['Rep']
        zic = dicts[n]
        weather.append(zic['W'])
        n = n + 1
  # tweet.append(r['text'])
  # dates.append(r['created_at'])
  # ids.append(r['id'])

Weather_code = {'NA':'Not available', 0:'Clear night', 1:'Sunny day', 2:'Partly cloudy(night)', 3:'Partly cloudy(day)', 4:'Not used', 5:'Mist', 6:'Fog', 7:'Cloudy', 8:'Overcast', 9:'Light rain shower(night', 10:'Light rain shower(day)', 11:'Drizzle', 12:'Light rain', 13:'Heavy rain shower(night)', 14:'Heavy rain shower(day)', 15:'Heavy rain', 16:'Sleet shower (night)', 17:'Sleet shower (day)', 18:'Sleet', 19:'Hail shower (night)', 20:'Hail shower (day)', 21:'Hail', 22:'Light snow shower (night)', 23:'Light snow shower (day)', 24:'Light snow', 25:'Heavy snow shower (night)', 26:'Heavy snow shower (day)', 27:'Heavy snow', 28:'Thunder shower', 29:'Thunder shower (day)', 30:'Thunder'}
#print Weather_code
weathercode2 = {'Na':['NA', 4], 'cloudy':[2, 3, 7, 8], 'sunny':[0, 1], 'rain':[9, 10, 11, 12, 13, 14, 15], 'foggy':[5, 6], 'sleet':[16, 17, 18], 'hail':[19, 20, 21], 'snow':[22, 23, 24, 25, 26, 27], 'storm':[28, 29, 30]}
weathercode3 = {'NA':'Na', '4': 'Na', '2':'cloudy', '3': 'cloudy', '7': 'cloudy', '8': 'cloudy', '9': 'rain', '10': 'rain', '11': 'rain', '12': 'rain', '13': 'rain', '14': 'rain', '15': 'rain', '5': 'foggy', '6': 'foggy', '16': 'sleet', '17': 'sleet', '18': 'sleet', '19':  'hail', '20': 'hail', '21': 'hail', '22': 'snow', '23': 'snow', '24': 'snow', '25': 'snow', '26': 'snow', '27' : 'snow', '28': 'storm', '29': 'storm', '30': 'storm' }
print weathercode3['7']

dd = str(dataDate)
ww = str()
forecasts = {}
weather2 = []

for i in weather:
    weather2.append(str(i))

weather3 = []
for i in weather2:
    weather3.append(weathercode3[i])

forecasts[dd] = weather3
print forecasts


#print forecasts






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

