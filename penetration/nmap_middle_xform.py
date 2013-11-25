#!/usr/bin/python

#################
# NMAP SCAN TOOL#
#################

import os, sys, re
from MaltegoTransform import *

m_ent = MaltegoTransform();
m_ent.parseArguments(sys.argv);
m_ent.getValue();


ports = "20-25,80,6789"
victim = sys.argv[1] # ip address of victim  
file_name = victim

nmap_cmd_line_args = "nmap -oG " + file_name + " -sV -p" + ports + " " + victim + ">" + file_name + ".txt"

os.system(nmap_cmd_line_args)

# open output file of nmap
f = open(file_name)
for line in f:
    cut_host = re.sub(r'Host(.*)\t', '', line)
    if cut_host[:5] == "Ports":
        cut_ports = re.sub(r'Ports: ', '', cut_host)
        fields = cut_ports.split(", ")
        for field in fields:
            kill_slash = field.replace("//", "/")
            port_vals = kill_slash.split("/")

            port_num = port_vals[0].strip()
            is_open = port_vals[1].strip()
            protocol = port_vals[2].strip()
            service = port_vals[3].strip()
            banner = port_vals[4].strip()

            if is_open == "closed":
                service = "N/A"

            # show them in maltego ui
            me_serv = m_ent.addEntity("jf.SuperFunTransforms", "PORT: " + port_num + " is " + is_open + "\n"  + " SERVICE: " + service);
            me_serv.setType("jf.SuperFunTransforms")
            me_serv.addAdditionalFields("port", "Port", None, port_num) 
            me_serv.addAdditionalFields("protocol", "Protocol", None, protocol)
            me_serv.addAdditionalFields("service",  "Service", None, service)
            me_serv.addAdditionalFields("banner", "Banner", None, banner)
            me_serv.addAdditionalFields("opening", "Open?", None, is_open)

f.close();
os.system("rm " + file_name)
os.system("rm " + file_name + ".txt")
m_ent.returnOutput();
