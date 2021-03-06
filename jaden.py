import twitter
from random import shuffle
from datetime import datetime  
from sys import argv

script, botpath = argv


def main():
    myAcctData = getAcctData()

    tweet = twitter.Api(consumer_key = myAcctData['consumer_key'],
                      consumer_secret = myAcctData['consumer_secret'],
                      access_token_key = myAcctData['access_token_key'],
                      access_token_secret = myAcctData['access_token_secret'])

    Jaden = tweet.GetUserTimeline(262794965)

    startTime = datetime.now()

    new_tweets = 0
    tweet_list = []

    for status in reversed(Jaden[0:10]):
        
        time = parseTime(status, startTime)
        age = startTime - time
        print time, age, startTime
        if (age.seconds < 3600 and time.day == startTime.day):
            words = status.text.split(' ')
            words_to_use = [word for word in words if 'http' not in word]
            shuffle(words_to_use)
            new_status = ' '.join(words_to_use)
            jadens_genius = tweet.PostMedia(new_status, 'http://i.imgur.com/y0GDcOv.png')
            new_tweets += 1
            tweet_list.append(jadens_genius.text)
    
    LogTweets(startTime, new_tweets, tweet_list, time)

def getAcctData():
    # Get Oauth info from file
    keyfile = botpath + '/keyfile.txt'
    Odict = {}
    lines = [line.strip() for line in open(keyfile)]
    for line in lines:
        key, value = tuple(line.split('='))
        Odict[key] = value
    return Odict


def parseTime(tweet, startTime):
    # Take status and return datetime object
    strTime = ' '.join(
        tweet.created_at.split(' ')[:4]) + ' ' + str(startTime.year)
    return datetime.strptime(strTime, '%a %b %d %H:%M:%S %Y')

def LogTweets(runTime, tweets, tweet_list, orig_tweet_time):
    logfile = open(botpath + '/log.txt', 'a')
    logfile.write("Running at: %s\n" % runTime)
    logfile.write("Made %d new tweet(s):\n\n" % tweets)
    for tweet in tweet_list:
        tweet = tweet.encode('utf-8')
        logfile.write("\t%s\n" % tweet)
        logfile.write("\n\tOriginal status at %s\n\n" % orig_tweet_time)
    logfile.close()

                  



main()
    
