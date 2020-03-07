# Nicebirb - The Wholesome Tweets Bot

Python bot that uses tweepy api to respond to any mentions of my @NicestBirb twitter account and replies with one of three wholesome messages (Plan to add more in the future just wanted to get the POC down).

Used this as an opportunity to learn how to use tweepy and EC2 as well as to brush up on my Docker skills (IN THE MOST WHOLESOME WAY POSSIBLE).

## For own ref:

Running in Docker (Locally):
```
docker run -it -e CONSUMER_KEY= \
-e CONSUMER_SECRET= \
-e ACCESS_TOKEN= \
-e ACCESS_TOKEN_SECRET= \
nicebirb
```

Running in EC2:
```
docker run -d --restart always \
-e CONSUMER_KEY= \
-e CONSUMER_SECRET= \
-e ACCESS_TOKEN= \
-e ACCESS_TOKEN_SECRET= \
nicebirb
```
