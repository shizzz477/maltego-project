import oauth2 as oauth
import urllib2 as urllib
import json


# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "273567200-Da7TUKHxJW2s6onkVJ6JtJS6PmXmu389L5q5fIB6"
access_token_secret = "FG9DD586hkgQm10EcxZiq8K2WyO9dtCpFAae5uZc"

consumer_key = "IDwoLuRJwHHMLKGyhnaiOA"
consumer_secret = "bAG9MhjQ2xzPRP2vzJyZXYuFxo6vTfYBFZ9ckPiUGyU"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def searchUser(user, num=200):
	url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + user + "&count=" + str(num)
 	parameters = []
  	response = twitterreq(url, "GET", parameters)
  	tweets = []

 
  	for line in response:    
		tweet = (line.strip())
		tweets.append(tweet)
    
	p_tweets = json.loads(tweets[0])

	return p_tweets

def getFollowers(user):
	url = "https://api.twitter.com/1.1/followers/ids.json?cursor=-1&" + user + "=sitestreams&count=5000"
	parameters = []	
	response = twitterreq(url, "GET", parameters)
  	tweets = []

 
  	for line in response:    
		tweet = (line.strip())
		tweets.append(tweet)
    
	p_tweets = json.loads(tweets[0])

	return p_tweets	

def idToUsername(searchString):
  url = "https://api.twitter.com/1.1/users/lookup.json?user_id=" + searchString
  parameters = []	
  response = twitterreq(url, "GET", parameters)
  tweets = []

 
  for line in response:    
    tweet = (line.strip())
    tweets.append(tweet)
    
    p_tweets = json.loads(tweets[0])

    return p_tweets	


def search(topic, debug=False):
  url = "https://api.twitter.com/1.1/search/tweets.json?q="+topic
  print(url)
  parameters = []
  response = twitterreq(url, "GET", parameters)
  tweets = []

 
  for line in response:
	#print(line)    
	tweet = (line.strip())
	tweets.append(tweet)
    
  p_tweets = json.loads(tweets[0])

  return p_tweets


if __name__ =="__main__":
  tweets = searchUser('tab262')
  print(tweets[0]['text'])
       
