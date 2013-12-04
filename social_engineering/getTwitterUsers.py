import twitterSearch
from MaltegoTransform import *
import sys
DEBUG = False

def main(argv):
	if(argv[1] == "caseyso"):
		namesList = ["bobbyo", "jjc","alf","courtp"]
	elif (argv[1] == "jjc"):
		namesList = ["caseyso", "jjc","alf","courtp","mrclean"]
	elif (argv[1] == "alf"):
		namesList = ["mrclean", "jjc","alf","courtp","joe"]
	elif (argv[1] == "bobbyo"):
		namesList = ["jjc","caseyso","brat322"]
	else:	
		users = twitterSearch.getFollowers(argv[1]);
		if(DEBUG): print users
		searchString = ''
		for i in range(len(users['users'])):
			searchString += str(users['users'][i]['id']) + ','
	
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
