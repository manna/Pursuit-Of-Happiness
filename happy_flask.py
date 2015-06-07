
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
    target = [t_lat, t_lon]
    db = MySQLdb.connect("pursuit-of-happiness.cwouww8djnhv.us-west-2.rds.amazonaws.com","root","h4ppiest", "pursuit_of_happiness" )
    cur= db.cursor()
    sql = "SELECT longitude,latitude, score FROM boston"# WHERE score = 1"
    print "number of tweets: ", cur.execute(sql)
    # content = []
    data = []
    # for x in cur.fetchall():
        # # content.append("{}, {}, {}".format(x[0],x[1],x[2]))
        # data.append([x[0], x[1], x[2]])
    with open('cached_tweets.csv', 'rb') as csvfile:
        tweet_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in tweet_reader:
            print row
            # data.append(row)
    path = algo(source, target, data)
    db.close()
    # return "\n".join(content)
    return " ".join(path)
if __name__ == "__main__":
    app.run()