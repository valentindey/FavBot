# -*- coding: utf-8 -*-

# set credentials in credentials.py
from credentials import (
    API_KEY,
    API_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)

import sys
import tweepy
import json

class FavListener(tweepy.streaming.StreamListener):
    ''' A listener handles tweets received from the stream.
    This is a basic listener that just favs received tweets.
    '''

    def on_data(self, data):
        data = json.loads(data)  # load json response
        try:
            api.create_favorite(data['id'])  # fav the tweet with 'id'
            print 'Just faved', data['user']['screen_name'] + 's tweet:', data['text']
        except:
            pass  # errors are not handled yet
        return True

    def on_error(self, status):
        print(status) #see https://dev.twitter.com/overview/api/response-codes
    
listener = FavListener()

# authenticate and load API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# run the bot to fav all tweets containing a command line argument
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print 'Usage:', sys.argv[0], 'TRACKED_WORD'
        print '(word starting with "#" must be escaped with "\\")'
        sys.exit(0)

    print 'Streaming data and faving all tweets with', sys.argv[1], 'from now on...'
    stream = tweepy.Stream(auth, listener) #TODO: handle rate limiting
    stream.filter(track=[sys.argv[1]])
