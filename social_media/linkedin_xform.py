import urllib
import os
import re
import sys
import csv
from MaltegoTransform import *

def LinkedIn(linkedinusername):
	from pygoogle import pygoogle
	g = pygoogle("linkedin "+linkedinusername)
	g.pages = 5
	g.get_result_count()
	myURLs = g.get_urls()
	return myURLs


def main(argv):
	myURLs = LinkedIn(sys.argv[1])

	mt = MaltegoTransform();
	for urls in myURLs:
		mt.addEntity("maltego.Alias", urls)

	mt.returnOutput()




if __name__ == "__main__": main(sys.argv)
