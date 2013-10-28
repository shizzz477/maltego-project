#!/usr/bin/python

###### NOT WORKING PROPERLY 

import os, sys, time
from MaltegoTransform import *

m_ent = MaltegoTransform();
m_ent.parseArguments(sys.argv);

site_array = ["bu.edu", "emerson.edu", "google.com"]

file_name = "site_listing.txt"

for site_name in site_array:
    os_pass = ("nslookup " + site_name + " | tail -2 | awk -F \":\" \'{print $2}\'" + ">>" + file_name)

os.system(os_pass)

count = 0;

f = open(file_name)
for line in f: 
    me_ip = m_ent.addEntity("the_ip", "IP: " + line) 
    me_ip = None 

f.close()

#os.system("rm " + file_name)
m_ent.returnOutput();
