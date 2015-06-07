
# coding: utf-8

# In[10]:

from flask import Flask, request
app = Flask(__name__, static_url_path='')

import MySQLdb
import csv
from happirithm import *

@app.route("/<s_lat>/<s_lon>/<t_lat>/<t_lon>")
def getPath(s_lat, s_lon, t_lat, t_lon):
    source = [float(s_lat), float(s_lon)]
    target = [float(t_lat), float(t_lon)]
    # db = MySQLdb.connect("pursuit-of-happiness.cwouww8djnhv.us-west-2.rds.amazonaws.com","root","h4ppiest", "pursuit_of_happiness" )
    # cur= db.cursor()
    # sql = "SELECT longitude,latitude, score FROM boston"# WHERE score = 1"
    #print "number of tweets: ", cur.execute(sql)
    # content = []
    # for x in cur.fetchall():
        # # content.append("{}, {}, {}".format(x[0],x[1],x[2]))
        # data.append([x[0], x[1], x[2]])
    data = []
    with open('cached_tweets.csv', 'rb') as csvfile:
        tweet_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in tweet_reader:
            try:
                data.append([float(row[0]),float(row[1]), float(row[5])])
            except IndexError:
                pass
            except ValueError:
                pass
    path = algo(source, target, data)
    #db.close()
    return str(path)

@app.rout("/")
def index():
    return app.send_static_file('home.html')

if __name__ == "__main__":
    app.run()