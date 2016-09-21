import json
import pyodbc
from pymongo import MongoClient



cnx = pyodbc.connect('DSN=Kubrick')
cursor = cnx.cursor()

cursor.execute('select * from [dbo].[weather_london]') # change the table name
row = cursor.fetchall()

client = MongoClient('localhost', 27017)
db = client['watherproject1']  # make sure we create a new collection
weather_table = db['weather']
w = db.weather

weather_dic = []
for i in row:
    line = str(i[1])
    line1 = line.replace('$', 't')
    w.insert(json.loads(line1))







