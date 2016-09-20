import pyodbc
import json
import pandas
import pymongo
from pymongo import MongoClient

cnx = pyodbc.connect('DSN=Kubrick')
cursor = cnx.cursor()

cursor.execute("select * from [dbo].[twitter]")
rows = cursor.fetchall()
tweets = []
for row in rows:
    tweets.append(json.loads(row[1]))
print type(tweets[0])# check item in the list


client = MongoClient('localhost', 27017)
db = client['test']
tweet_table = db['tweet_table']
print tweet_table# check the table is created
t = db.tweet_table
for i in tweets:#reads through tweets and inserts each one
    t.insert(i)

#tweet=[]
##dates = []
#ids = []
#for i in rows:
#    row1 = i
#    rowx = row1[1]
#    r = json.loads(rowx)
#    tweet.append(r['text'])
#    dates.append(r['created_at'])
#    ids.append(r['id'])

#t1 = pandas.Series(tweet, name='tweet')
#t2 = pandas.Series(dates, name='date')
#t3 = pandas.Series(ids, name='id')
#t4 = pandas.concat([t1, t2, t3], axis=1)  # s3 dataframe
#print t4['tweet']


