
# coding: utf-8

# In[10]:

from flask import Flask
app = Flask(__name__)

import MySQLdb
import csv
from happirithm import *

@app.route("/<s_lat>/<s_lon>/<t_lat>/<t_lon>")
def hello(s_lat, s_lon, t_lat, t_lon):
    source = [s_lat, s_lon]
    print "source ", source
    target = [t_lat, t_lon]
    print "target ", target
    db = MySQLdb.connect("pursuit-of-happiness.cwouww8djnhv.us-west-2.rds.amazonaws.com","root","h4ppiest", "pursuit_of_happiness" )
    print "db ",db
    cur= db.cursor()
    print "cur ",cur
    sql = "SELECT longitude,latitude, score FROM boston"# WHERE score = 1"
    print "sql ",sql
    #print "number of tweets: ", cur.execute(sql)
    # content = []
    # for x in cur.fetchall():
        # # content.append("{}, {}, {}".format(x[0],x[1],x[2]))
        # data.append([x[0], x[1], x[2]])
    data = []
    with open('cached_tweets.csv', 'rb') as csvfile:
        print "csvfile ",csvfile
        tweet_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        print "tweet_reader ",tweet_reader
        for row in tweet_reader:
            try:
                data.append([float(row[0]),float(row[1]), float(row[5])])
            except IndexError:
                pass
            except ValueError:
                pass
    print "path "
    path = algo(source, target, data)
    print "path ",path
    db.close()
    # return "\n".join(content)
    return " ".join(path)
if __name__ == "__main__":
    app.run()