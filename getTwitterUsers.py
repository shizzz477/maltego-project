import twitterSearch
from MaltegoTransform import *
import sys
DEBUG = True

def main(argv):
	users = twitterSearch.getFollowers(argv[1]);
	print users

	ids =  users['ids']
	searchString = ''

	for id in ids:
		searchString += str(id) + ','

	
	if(DEBUG):print searchString[:-1]

	names = twitterSearch.idToUsername(searchString[:-1])
	namesList = []
	for name in names:
		namesList.append(name['screen_name'])

	if(DEBUG):print namesList

	mt = MaltegoTransform();
	for user_name in namesList:
		if(DEBUG):print user_name	
		mt.addEntity("maltego.Twit", user_name)
	
	
	mt.returnOutput()



if __name__=="__main__": main(sys.argv)
