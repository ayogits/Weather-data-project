import json
import pyodbc
from pymongo import MongoClient


cnx = pyodbc.connect('DSN=Kubrick')
cursor = cnx.cursor()

cursor.execute('select * from [dbo].[weather]') # change the table name
row = cursor.fetchall()

weather_dic = []
lst= []
for i in row:
    line = str(i[1])
    line1 = line.replace('$', 't')
    weather_dic.append(line1)

client = MongoClient('localhost', 27017)
db = client['test']  # make sure we create a new collection
weather_table = db['weather_table']
w = db.weather_table

for x in weather_dic:
    w.insert(json.loads(x))



