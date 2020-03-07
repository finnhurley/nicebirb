#!/usr/bin/env python
import tweepy
import logging
from config import create_api
import messages
import time
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#Where the magic happens
def beWholesome(api, tweetBank, keywords, since_id):
    logger.info("Seeing who needs some love...")
    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"{tweet.user.name} needs some god dam lovin...")
            wholesome_tweet = messages.generateTweet(tweetBank)
            if not tweet.favorited:
                try:
                    tweet.favorite()
                except Exception as e:
                    logger.error("Error on fav", exc_info=True)
            api.update_status(wholesome_tweet, tweet.id)
    return new_since_id

def main():
    tweetBank = messages.makeTweetBank()
    wholesomeKeywords = ["wholesome", "I need some love rn", "need some love rn"]
    api = create_api()
    since_id = 1
    while True:
        since_id = beWholesome(api, tweetBank, wholesomeKeywords, since_id)
        logger.info("Still lookin...")
        time.sleep(20)

if __name__ == "__main__":
    main()