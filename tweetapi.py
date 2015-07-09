#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from bottle import route, run, template, request
from requests_oauthlib import OAuth1Session
import json
#import matplotlib


#localhost:8080
@route('/', name='static_file')
def index():
	return template('index')


#localhost:8080/weathernow.html
@route('/result.html', method = "POST")
def result():

    word = str(request.POST.get('place'))
    


    ### Constants
    oauth_key_dict = {"CK" : "ySUtyGS148TlPtPkIS0WgC2QJ", "CS" : "w3qVPhc47wuQOOmVK0Ta8GKTvPsuSI12LtvWGfzAAfmkHq43fd", "AT" : "215529596-DCDJv6JmIDGuUPi9dzTJeFmy25DgltI9o0LB0Jgd", "ATS" : "DHwhWbEZtFd9MpHBqfSsUaE7BdajhSb3BLFIqpgbxutpa"}

    ### Functions
    #def main(word):
    #	tweets = tweet_search(word, oauth_key_dict)
    #	for tweet in tweets["statuses"]:
    #       text = tweet[u'text']
    #        geo = tweet[u'geo']
    #        user_description = tweet[u'user'][u'description']
    #    return text, geo, user_description



    def create_oauth_session(oauth_key_dict):
    	oauth = OAuth1Session(
    		oauth_key_dict["CK"],
    		oauth_key_dict["CS"],
    		oauth_key_dict["AT"],
    		oauth_key_dict["ATS"]
    		)
    	return oauth


    def tweet_search(search_word, oauth_key_dict):
    	url = 'https://api.twitter.com/1.1/search/tweets.json'
    	params = {'q' : search_word,
    			  'lang' : 'ja',
                  'result_type' : 'recent',
    			  'count' : '200'
    			 }
    	oauth = create_oauth_session(oauth_key_dict)
    	req = oauth.get(url, params = params)
        tweets = json.loads(req.text)
        return tweets

    ### Execute
    html = []
    tweets = tweet_search(word, oauth_key_dict)

    for tweet in tweets["statuses"]:
        username = tweet[u'user'][u'screen_name']
        text = tweet[u'text']
        time = tweet[u'created_at']
        user_description = tweet[u'user'][u'description']
        html.append({'username' : username, 'text' : text, 'time' : time, 'u_des' : user_description})
        

    ### templateに返す
    return template('result.tpl', html = html)
    






run(host = 'localhost', port = 8080, debug = True, reloader = True)