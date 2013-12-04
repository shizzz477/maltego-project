#!/usr/bin/python

'''
Easy example of core functions 
Just dumps every single line of a text file into entities
'''
import os, sys, time
from MaltegoTransform import *
m_ent = MaltegoTransform();
m_ent.parseArguments(sys.argv);
# add logic here to pull from higher entities
site_array = "bu.edu" # take in multiple sites if one wants 
file_name = "site_listing.txt"
os_pass = ("nslookup " + site_array + ">>" + file_name)
os.system(os_pass)
count = 0;
f = open(file_name)
for line in f: 
    me_ip = m_ent.addEntity("the_ip", "IP: " + line.strip()) 
    me_ip = "DNS ADDRESS" # cascading logic...value that will be pulled by lower transforms
f.close()
#os.system("rm " + file_name)
m_ent.returnOutput();
