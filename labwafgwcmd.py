#!/usr/bin/env python
#################################################################################################
#################################################################################################
##  WAFGWCMD - command line interface for WAF Gateway.
##  
##  Author: Bartosz Chmielewski
#################################################################################################
#################################################################################################
import argparse
import json
import os
import requests
from rich import print_json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

##Getting authorization information from the env variables. 
WAFGW_USERNAME=str(os.getenv('WAFGW_USERNAME', default=None))
WAFGW_PASSWORD=str(os.getenv('WAFGW_PASSWORD', default=None))
WAFGW_HOST=str(os.getenv('WAFGW_HOST', default=None))
WAFGW_PORT=str(os.getenv('WAFGW_PORT', default=None))

if (not WAFGW_USERNAME and WAFGW_PASSWORD and WAFGW_HOST and WAFGW_PORT):
    print("The enviromental variables are not set properly...")
    quit()

BASEURL= "https://" + WAFGW_HOST + ":" + WAFGW_PORT + "/"

session = requests.Session()

headers ={
	"Accept": "application/json"
}

def log_in():
    print("Staring authentication...")
    session.auth = (WAFGW_USERNAME, WAFGW_PASSWORD)
    url = BASEURL + "SecureSphere/api/v1/auth/session"
    r = session.post(url, headers=headers, verify=False)
    if (r.status_code==200):
         print("Auth OK. Got code", r.status_code, "and the session ID is", r.cookies['JSESSIONID'])
    else:
         print("Authentication failed with a code:", r.status_code)
         quit()
    session.auth = None

def log_out():
    url = BASEURL + "SecureSphere/api/v1/auth/session"
    r = session.delete(url, headers=headers)
    if (r.status_code==200):
         print("Successfully deleted session...")
    else:
         print("Error in deleting session. Got status code:", r.status_code)    

##Parsing arguments
parser = argparse.ArgumentParser(description="CWAF CLI interface")
parser.add_argument('action', choices=['getviolations', 'getlicense', 'listsites', 'listwebservices', 'listcustompolicies', 'getcustompolicy', 'listdictionaries' ,'getsignature'], help="Provide action from the list. ")
parser.add_argument('-d', nargs="?", help="Search scope in days",)
parser.add_argument('-p', nargs="?", help="Policy name.",)
parser.add_argument('-s', nargs="?", help="Signature name.",)
args = parser.parse_args()

log_in()

if args.action == 'getviolations':
    if args.d:
        url = BASEURL + "SecureSphere/api/v1/monitor/violations/" 
        urlparams = {'lastFewDays': args.d }
        r = session.get(url, headers=headers, params=urlparams)
        print_json(json.dumps(r.json()), indent=3)
    else:
        print("Missing -d argument. Please provide a time range...")

elif args.action == 'getlicense':
    url = BASEURL + "SecureSphere/api/v1/administration/license" 
    r = session.get(url, headers=headers)
    print_json(json.dumps(r.json()), indent=3)

elif args.action == 'listsites':
    url = BASEURL + "SecureSphere/api/v1/conf/sites" 
    r = session.get(url, headers=headers)
    print_json(json.dumps(r.json()), indent=3)

elif args.action == 'listwebservices':
    url = BASEURL + "SecureSphere/api/v1/conf/webServices/LocalLab/BCH Server Group" 
    r = session.get(url, headers=headers)
    print_json(json.dumps(r.json()), indent=3)

elif args.action == 'listcustompolicies':
    url = BASEURL + "SecureSphere/api/v1/conf/policies/security/webServiceCustomPolicies" 
    r = session.get(url, headers=headers)
    print_json(json.dumps(r.json()), indent=3)

elif args.action == 'getcustompolicy':
    if args.p:
        url = BASEURL + "SecureSphere/api/v1/conf/policies/security/webServiceCustomPolicies/" + args.p
        r = session.get(url, headers=headers)
        print_json(json.dumps(r.json()), indent=3)
    else:
        print("Missing -p argument. Please provide a policy name...")

elif args.action == 'listdictionaries':
    url = BASEURL + "SecureSphere/api/v1/conf/dictionaries" 
    r = session.get(url, headers=headers)
    print_json(json.dumps(r.json()), indent=3)        

elif args.action == 'getsignature':
    if args.s:
        url = BASEURL + "SecureSphere/api/v1/conf/signatures/predefinedDictionaries/All Signatures for Web Applications/" + args.s
        r = session.get(url, headers=headers)
        print_json(json.dumps(r.json()), indent=3)  
    else:
        print("Missing -s argument. Please provide a signature name...")

else:
	print('Wrong or missing argument.')

log_out()
