import twitter
from random import shuffle
import os

def main():
    myAcctData = getAcctData()

    tweet = twitter.Api(consumer_key = myAcctData['consumer_key'],
                      consumer_secret = myAcctData['consumer_secret'],
                      access_token_key = myAcctData['access_token_key'],
                      access_token_secret = myAcctData['access_token_secret'])

    Jaden = tweet.GetUserTimeline(262794965)

    for status in Jaden:
        words = status.text.split(' ')
        words_to_use = [word for word in words if 'http' not in word]
        shuffle(words_to_use)
        new_status = ' '.join(words_to_use)
        jadens_genius = tweet.PostMedia(new_status, 'http://i.imgur.com/y0GDcOv.png')
        break

def getAcctData():
    # Get Oauth info from file
    keyfile = os.environ.get('BOTPATH') + '/keyfile.txt'
    Odict = {}
    lines = [line.strip() for line in open(keyfile)]
    for line in lines:
        key, value = tuple(line.split('='))
        Odict[key] = value
        print "%s: %s" % (key, value)
    return Odict

main()
    
