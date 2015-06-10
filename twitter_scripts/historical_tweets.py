
# coding: utf-8

# In[1]:

from alchemyapi import AlchemyAPI
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy
import MySQLdb
import datetime

import hp 


# In[2]:

def run_sentiment(text):
    #print text
    return hp.hp_sentiment(text)


# In[4]:

def save_to_db(payload):
    
    with open('aws.txt','r') as f:
        domain = f.readline().strip()
        user = f.readline().strip()
        pwd = f.readline().strip()
        db = f.readline().strip()
    
    
    # Open database connection
    db = MySQLdb.connect(domain,user,pwd,db)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO boston(LONGITUDE, LATITUDE, CREATED_AT, TWEET_ID, TEXT, SCORE) VALUES (" + str(payload)[1:-1] + ")" 
    print sql
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
        db.close()
        return 1

    # disconnect from server
    db.close()


# In[5]:

def send_data(response):
    query = []
    try:
        query.append(response.coordinates['coordinates'][0])
        query.append(response.coordinates['coordinates'][1])
        query.append(str(response.created_at))
        query.append(response.id)
        query.append(response.text)
        query.append(run_sentiment(response.text))

        payload = [str(x.encode('ascii', 'ignore')).replace("\"","\'").replace('u\'','').replace('None','0') if type(x) is unicode or type(x) is str else str(x).replace("\"","\'").replace('u\'','') for x in query ]
        #payload = str(query)
        #print payload
        save_to_db(payload)
        return "good"
    except:
        return "error"
      #  pass
    #error = save_to_db(payload)
    #if error:
    #    print payload


# In[ ]:

#need to have a file keys.txt with the Twitter API keys/info
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

with open('keys.txt','r') as f:
    consumer_key = f.readline().strip()
    consumer_secret = f.readline().strip()
    access_token = f.readline().strip()
    access_token_secret = f.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search,q="",count=2000, geocode="42.303772,-71.08507,5mi").items():
    print tweet.text
    print send_data(tweet)


# In[ ]:

print tweet.id


# In[ ]:



