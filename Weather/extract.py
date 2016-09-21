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




client = MongoClient('localhost', 27017)
db = client['weatherproject']  # make sure we create a new collection
wet = db['weather']
t = db.wet
a = rep_data.replace("$", "t")
b = json.loads(a)
print b
t.insert(b)