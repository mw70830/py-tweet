#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, datetime
import time
from keys import * # keys에 토큰과 키, user_name을 선언한다.

def api_login():
    print("Now login...")
    auth = tweepy.OAuthHandler(keys['API_KEY'], keys['API_SECRET_KEY'])
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    user = api.get_user(user_name)
    print("login process end.")

    return auth, api, user

def write_tweet(api, comment):
    api.update_status(comment)

def delete_tweets(api):
    print("[Delete] process start...")

    print("Get timeline...")
    #tweets = api.user_timeline(user_name, tweet_mode='extended', count=100)
    tweets = api.user_timeline(user_name)
    timeline = tweepy.Cursor(api.user_timeline).items()

    for tweet in timeline:
        print("트윗 한 사람 : ")
        print(" " + tweet._json["user"]["name"] + tweet._json["user"]["screen_name"])
        if tweet._json["in_reply_to_screen_name"] != None:
            print(tweet._json["in_reply_to_screen_name"] + "에게 한 답멘")
        print("내용 : ")
        print(" " + tweet._json["text"])

        print("Delete? (y:delete,exit:exit, else any key:pass)")
        do_delete = input("> ")
        if do_delete.lower() == "y":
            api.destroy_status(tweet.id_str)
        if do_delete.lower() == "exit":
            break

def main():
    print("process start...")
    auth, api, user = api_login()

    #write_tweet(api, "test tweet!!.")

    delete_tweets(api)


if __name__ == '__main__':
    main()
