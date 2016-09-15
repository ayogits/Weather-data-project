from twython import TwythonStreamer
import sys
import pyodbc
import json

cnx = pyodbc.connect('DSN=kubricksql')
cursor = cnx.cursor()

tweet=[]
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data['lang']== 'en':
            tweet.append(data)
            print 'recieved tweet #', len(tweet)


        if len(tweet) >= 2500:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()

stream = MyStreamer('NBELcJ0hNlJH4FImYclwgEALK', 'ucJsYSCsTlaJodnKgasmOlinYQAch8lgEydqAPMRyiMmRSOaWk', '775364853804466176-i99JIL2wHCwaVNHZPRXd9HjVWRbCokT', 'wWwdvtKS2gWMIv39LDtmkTp0xdOHPCJGeOAaXo4ByEYRv')
stream.statuses.filter(track='Liverpool sun')

for t in tweet:
    tweet = t
    insertcmd = "insert into dbo.Tweetdb (Tweet) values(?)"
    cursor.execute(insertcmd, json.dumps(tweet))

cnx.commit()