source = [43.141343, -71.13413]
target = [43.414314, -71.53114]

import csv
from happirithm import *

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
    print(str(path))