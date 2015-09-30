import twitter
from random import shuffle

api = twitter.Api(consumer_key = 'mFM3eWa7vYYak51hBoGEx4D86',
                  consumer_secret = '39xk2sZtT911PdGt75Q4CV9pytfgrKQa9EM2P2UhlUT9zPd52S',
                  access_token_key = '3587640499-dD0bW4njxkZBh6P8Pq69AywtiwQdmPwce86hNfg',
                  access_token_secret = 'SRRpR2YuBHSoRr2J1hk5L2OwcrFNZc2R98bRMHl0XHcVP')

Jaden = api.GetUserTimeline(262794965)

for status in Jaden:
    words = status.text.split(' ')
    words_to_use = [word for word in words if 'http' not in word]
    shuffle(words_to_use)
    new_status = ' '.join(words_to_use)
    jadens_genius = api.PostMedia(new_status, 'http://i.imgur.com/y0GDcOv.png')
    print jadens_genius
    break


    
