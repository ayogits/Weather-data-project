import pyodbc
import json
import pandas
cnx = pyodbc.connect('DSN=Kubrick')
cursor = cnx.cursor()

cursor.execute("select * from [dbo].[tweets]")
rows = cursor.fetchall()
tweet=[]
dates = []
ids = []
for i in rows:
    row1 = i
    rowx = row1[1]
    r = json.loads(rowx)
    tweet.append(r['text'])
    dates.append(r['created_at'])
    ids.append(r['id'])

t1 = pandas.Series(tweet, name='tweet')
t2 = pandas.Series(dates, name='date')
t3 = pandas.Series(ids, name='id')
t4 = pandas.concat([s1, s2, s3], axis=1)  # s3 dataframe
print t4['tweet']


