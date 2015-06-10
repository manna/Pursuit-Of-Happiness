
# coding: utf-8

# In[1]:

import MySQLdb
from alchemyapi import AlchemyAPI
#from hp import hp_sentiment
import hp


# In[ ]:

with open('aws.txt','r') as f:
        domain = f.readline().strip()
        user = f.readline().strip()
        pwd = f.readline().strip()
        db = f.readline().strip()    


# In[2]:

db = MySQLdb.connect(domain,user,pwd,db)cur= db.cursor()
#sql = "SELECT score FROM boston  WHERE( score = 1 )"
#sql = "UPDATE boston SET score = 0 WHERE score = 1"
#cur.execute(sql)
sql = "SELECT * FROM boston WHERE score = 1"
print "number of tweets: ", cur.execute(sql)
search = []
for x in cur.fetchall():
    search.append(x)
db.close()


# In[3]:

print search[0]


# In[4]:

def do_analysis(text):
    return 0


# In[15]:

score_values = []
n = 0
for x in search:
    #score_values.append([x[3], hp.hp_sentiment(x[4])])


# In[104]:

print (score_values)


# In[21]:

y =0
for x in score_values:
    if x[1] is not 1:
        #print x
        y += 1
print (len(score_values) -y )/float(len(score_values))


# In[2]:

import csv


# In[3]:

import pandas as pd


# In[4]:

df = pd.DataFrame.from_csv("hp_sentiments.csv")


# In[52]:

df = pd.DataFrame(score_values)#.to_csv("hp_sentiments.csv")


# In[1]:

df = df[df[1] != 1]


# In[8]:

print df.info()


# In[34]:

df.to_csv("hp_sentiments.csv")


# In[7]:

print x[3], x[4]


# In[2]:

print df


# In[3]:

db = MySQLdb.connect(domain,user,pwd,db)cur= db.cursor()
sql = "SELECT * FROM boston WHERE tweet_id= 607332003910926336"
cur.execute(sql)
print cur.fetchone()
db.close()


# In[9]:

print df['1']


# In[86]:

lister = []
#sql = "SELECT * FROM boston"# WHERE score = 1"
for row in df.iterrows():
    db = MySQLdb.connect(domain,user,pwd,db)    cur= db.cursor()
    sql = "SELECT latitude,longitude FROM boston WHERE tweet_id= " + str(int(row[1][0]))
    cur.execute(sql)
    x = cur.fetchone()
    try:
        lister.append([x])
    except:
        pass
    db.close()


# In[85]:

print lister


# In[4]:

df = pd.DataFrame.from_csv("big.csv", index_col=[3])# -71.193173,42.274069,-70.925261,42.445056


# In[5]:

print df.info()


# In[13]:

#refilter by long/lat to get Boston Proper tweets instead of greater boston area
#we did this because we needed more dense data
lf = df[df['longitude'] > -71.193173]
lf = lf[lf['longitude'] < -70.925261]
lf = lf[lf['latitude'] > 42.333069]
lf = lf[lf['latitude'] < 42.445056]


# In[14]:

print lf.info()


# In[15]:

lf.to_csv("large_set.csv")

