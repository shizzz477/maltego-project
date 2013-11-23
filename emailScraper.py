import urllib
import os
import re
import sys
import csv

#stolen from http://love-python.blogspot.com/2008/04/python-code-to-scrape-email-address.html
def collectAllEmail(htmlSource):
        "collects all possible email addresses from a string, but still it can miss some addresses"
        #example: t.s@d.com
        email_pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
        emails = re.findall(email_pattern, htmlSource)
        return emails
#ditto
def collectEmail( htmlSource):
    "collects all emails that starts with mailto: in the html source string"
    #example: <a href="mailto:t.s@d.com">
    email_pattern = re.compile("<a\s+href=\"mailto:([a-zA-Z0-9._@]*)\">", re.IGNORECASE)
    emails = re.findall(email_pattern, htmlSource)
    return emails


#set URL
url = "http://www.bu.edu/cs/people/directory/";
#grab html
html = urllib.urlopen(url).read()

emails = collectAllEmail(html) 

print emails

#write to csv file
myfile = open('emails.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(emails)
