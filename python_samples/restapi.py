#!/usr/bin/env python
"""
restapi.py Learn REST API with Python script  
Usage: restapi.py [options] 

Options:
  -e --exer <number>            exercise number 
  -h                            this help

Mail bug reports and suggestion to : Larry Cai <larry.caiyu AT gmail.com>
"""

import getopt, sys, os, errno  
import getpass    
import requests
import json
from requests.auth import HTTPBasicAuth

# Reference:
# Understand REST API: http://www.restapitutorial.com/ 
# Requests python module: http://www.python-requests.org 
# Github developer API v3 http://developer.github.com/v3/
# Jenkins API https://wiki.jenkins-ci.org/display/JENKINS/Remote+access+API

# exer1 : use curl to access http://httpbin.org/get
# exer2 : use requests module in python interactive module
#
def exer3():
    """
    learn requests module 
    task:
        get data from the server and print out response data like status_code, text, headers
    """
    server = "http://httpbin.org/get"
    
# r = requests.get('https://github.com', verify=True)
# <Response [200]>
# r = requests.get('https://github.com', auth=HTTPBasicAuth(user,passwd))
#
def exer4():
    """
    learn https and authentication in requests
    learn real github example gist
    task:
       get your account's created date using authentication
    """
    server = "https://api.github.com"
    url = server + "/user"
    user = "larrycai"
    passwd = getpass.getpass('Password:')
    print "checking ", url, "using user:", user
    
#>>> import json
#>>> url = 'https://api.github.com/some/endpoint'
#>>> payload = {'some': 'data'}
#>>> headers = {'content-type': 'application/json'}
#>>> r = requests.post(url, data=json.dumps(payload), headers=headers)
#
# check http://developer.github.com/v3/gists/#create-a-gist
#
def exer5():
    """
    learn POST method in requests
    learn create gist
    task: 
        create the gist for this script with name "restapi.py" and description "CodingWithMe sample"
    """
    server = "https://api.github.com"
    url = server + "/gists"
    user = "larrycai"
    passwd = getpass.getpass('Password:')

    local_file = "restapi.py"
    with open(local_file) as fh:
        mydata = fh.read()

def exer6():
    # this is bonus exercise
    # 7.1 Implement for all gist API
    # 7.2 oauth to access github in python script
    # 7.3 Get all jenkins jobs in python script
    pass

def enable_debug():
    import logging

    # These two lines enable debugging at httplib level (requests->urllib3->httplib)
    # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # The only thing missing will be the response.body which is not logged.
    import httplib
    httplib.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig() 
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True           

def main(): 
    number = "3"
    try:
        cmdlineOptions, args= getopt.getopt(sys.argv[1:],'he:',["help","exer="])
    except getopt.GetoptError, e:
        raise "Error in a command-line option:\n\t" + str(e)

    for (optName,optValue) in cmdlineOptions:
        if  optName in ("-h","--help"):
            print __doc__
            sys.exit()
        elif optName in ("-e","--exer"):
            number = optValue
        else:
            errorHandler('Option %s not recognized' % optName)

    # mostly you don't need to understand below, focus on exercise 
    # Get it from globals and invoke `exerx()` method directly
    method_name = "exer" + number
    method_list = globals()
    if method_name in method_list:
        method_list[method_name]()
    else:
        print "the exericse %s is not ready, please create method `exer%s` directly" % (number, number )

if __name__ == "__main__": 
  main()

