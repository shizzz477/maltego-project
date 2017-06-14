#!/usr/bin/env python

#################
# NMAP VULN TOOL#
#################

import os, sys
from MaltegoTransform import *

m_ent = MaltegoTransform()
m_ent.parseArguments(sys.argv)

banner_grab = m_ent.getVar("banner") 
open_grab = m_ent.getVar("opening") 

if open_grab  == "open":
    me_add = m_ent.addEntity("Banner", banner_grab)
    me_add.setType("jf.SuperFunTransforms")

m_ent.returnOutput();
