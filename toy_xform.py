#!/usr/bin/python

### just dumps the info from ns lookup straight out ###
### needs code to format data, accept more sites ###
import os, sys, time
from MaltegoTransform import *

m_ent = MaltegoTransform();
m_ent.parseArguments(sys.argv);

site_array = "bu.edu" # eventually take in multiple sites perhaps 

file_name = "site_listing.txt"

os_pass = ("nslookup " + site_array + ">>" + file_name)

os.system(os_pass)

count = 0;

f = open(file_name)
for line in f: 
    me_ip = m_ent.addEntity("the_ip", "IP: " + line.strip()) 
    me_ip = None 

f.close()

#os.system("rm " + file_name)
m_ent.returnOutput();
