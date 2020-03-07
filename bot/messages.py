import random

def makeTweetBank():
    tweetsFile = open("util/messages.txt", "r")
    tweetBank = [line.strip() for line in tweetsFile]
    return tweetBank

def generateTweet(tweetBank):
    random.seed()
    i = random.randint(0, len(tweetBank)-1)
    return tweetBank[i]