#!/usr/bin/python

#################
# NMAP SCAN TOOL#
#################

import os, sys
from MaltegoTransform import *

m_ent = MaltegoTransform();
m_ent.parseArguments(sys.argv);

ports = "20-25,80,6789" # ports of hosted HTTP index.html
victim = sys.argv[1] # ip address of victim 

file_name = victim;

# run nmap and pipe to cat
nmap_cmd_line_args = "nmap -oG " + file_name + " -sV -p" + ports + " " + victim + ">" + file_name + ".txt" # content not allowed in xml prolog...out here
os.system("rm " + file_name + ".txt")
os.system(nmap_cmd_line_args); 

# open output file of nmap
f = open(file_name)
for line in f:
    fields = line.split("\t")

    # port_dump now gives each port output
    for field in fields:
        the_field = field.split(": ");
        if (the_field[0] == "Ports"):
            port_dump = the_field[1].split(",");

            # go through port_dump and pick out each value
            for port in port_dump:
                port = port.replace("//", "/");
                port_vals = port.split("/");

                # parse the values block and put into relevant entities
                port_num = port_vals[0].strip();
                is_open = port_vals[1].strip();
                service = port_vals[4].strip();

                if (is_open == "closed"):
                    service = "N/A"

                # show them in maltego ui
                me_serv = m_ent.addEntity("Scanned_Ports", "PORT: " + port_num + " is " + is_open + "\n"  + " SERVICE: " + service);

f.close();
os.system("rm " + file_name)
m_ent.returnOutput();

