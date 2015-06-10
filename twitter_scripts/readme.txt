Need the following files:
HP_IDOL_OnDemand_API_Key > api_key.txt
AWS IP, user, password, database > aws.txt (each componet separted by newlines)
TWITTER_API_KEYS_AND_TOKENS > keys.txt

Use 'iPython Notebook *.ipynb' in shell to open the Notebook. We used the notebooks to prototype and adapted the historical_tweets.py to run on a Linode to actively collect tweets. 

You will need to make sure a AWS database is setup and your IP address is included as "allowed" in order to save to a database. 

Use MySQL Workbench to make your life generally better.

To setup the same structure for the database run the following SQL command:

"

CREATE TABLE IF NOT EXISTS `boston` (
  `longitude` decimal(10,8) NOT NULL,
  `latitude` float(10,8) NOT NULL,
  `created_at` datetime NOT NULL,
  `tweet_id` decimal(30,0) NOT NULL, 
  `text` text NOT NULL,
  `score` decimal(5, 4) NOT NULL,
  UNIQUE KEY `tweet_id` (`tweet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

"

BONUS SAMPLE INSERT STATEMENT:

"
INSERT INTO `boston` (`longitude`,`latitude`,`created_at`,`tweet_id`,`text`,`score`) VALUES (-71.13174550,42.35285568,'2015-06-04 23:46:43',606608046983401472,'In honor of @krisstil \'Scholarship program\' competition this weekend and the first 512 reunion since https://t.co/bzxxmHg3rQ',1.64452253049000);


"