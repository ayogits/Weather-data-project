#yyyyy
from twython import TwythonStreamer
import sys
import pyodbc
import json
from pymongo import MongoClient


cnx = pyodbc.connect('DSN=kubrick')
cursor = cnx.cursor()


client = MongoClient('localhost', 27017)
db = client['test']  # make sure we create a new collection
twyt = db['twyt']
t = db.twyt


tweet=[]
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data['lang']== 'en':
            tweet.append(data)
            print 'recieved tweet #', len(tweet)
            insertcmd = "insert into dbo.tweets (Tweet) values(?)"
            cursor.execute(insertcmd, json.dumps(data))
            cnx.commit()
            twyt.insert(data)

        if len(tweet) >= 5:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()

stream = MyStreamer('NBELcJ0hNlJH4FImYclwgEALK', 'ucJsYSCsTlaJodnKgasmOlinYQAch8lgEydqAPMRyiMmRSOaWk', '775364853804466176-i99JIL2wHCwaVNHZPRXd9HjVWRbCokT', 'wWwdvtKS2gWMIv39LDtmkTp0xdOHPCJGeOAaXo4ByEYRv')
stream.statuses.filter(track='trump')


# print tweet_table# check the table is created

for i in tweet:
    tweet = i
