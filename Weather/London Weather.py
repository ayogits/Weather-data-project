import json
import urllib2
from bs4 import BeautifulSoup
import pyodbc

api_key = 'f0f01451-af09-4943-a626-0dd57bcf533d'

weather = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/3772?res=3hourly&key=' + api_key
page = urllib2.urlopen(weather)
soup = BeautifulSoup((page), "lxml")
j_file = json.loads(str(soup.p.string))
rep_data = json.dumps(j_file)

database_name = 'Kubrick'
your_table = 'weather_london'

cnx = pyodbc.connect('DSN='+ database_name)
cursor = cnx.cursor()

insertcmd = "insert into dbo." + your_table + "(Info) values (?)"

cursor.execute(insertcmd, rep_data)
cnx.commit()