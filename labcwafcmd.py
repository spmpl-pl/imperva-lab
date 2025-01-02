#!/usr/bin/env python
#################################################################################################
#################################################################################################
##  CWAFCMD - command line interface for CWAF
##
##  Author: Bartosz Chmielewski
#################################################################################################
#################################################################################################
import argparse
import json
import os
import requests
from rich import print_json

##Parsing arguments
parser = argparse.ArgumentParser(description="CWAF CLI interface")
parser.add_argument('action', choices=['accountstatus', 'listsites', 'listrules', 'listsubaccounts', 'sitestatus', 'getvisits'], help="Provide action from the list. ")
parser.add_argument('-s', nargs="?", help="Site ID",)
parser.add_argument('-ip', nargs="?", help="IP Address for filtering")
args = parser.parse_args()

##Getting authorization information from the env variables.
IMPV_ACCOUNT_ID=os.getenv('IMPV_ACCOUNT_ID')
IMPV_API_ID=os.getenv('IMPV_API_ID')
IMPV_API_KEY=os.getenv('IMPV_API_KEY')

BASEURL="https://my.imperva.com/api/"

## building headers for the request
headers ={
	"x-API-Id": IMPV_API_ID,
	"x-API-Key": IMPV_API_KEY,
	"Accept": "application/json"
}

if args.action == 'accountstatus':
    url = BASEURL + "prov/v1/account"
    urlparams = { 'account_id': IMPV_ACCOUNT_ID }
    response = requests.post(url, data='', headers=headers, params=urlparams ).json()
    del response['account']
    print_json(json.dumps(response), indent=3)
    quit()

elif args.action == 'listsites':
    url = BASEURL + "prov/v1/sites/list"
    urlparams = { 'account_id': IMPV_ACCOUNT_ID }
    response = requests.post(url, data='', headers=headers, params=urlparams ).json()
#
    for i in response["sites"]:
        print("{0:<15} {1:<25} {2:<25} {3:<25}".format(i["site_id"], i["status"] , i["domain"],i["ips"][0]))
    quit()

elif args.action == 'listrules':
    if args.s:
        url = BASEURL + "prov/v1/sites/incapRules/list"
        urlparams = { 'site_id': args.s }
        response = requests.post(url, data='', headers=headers, params=urlparams ).json()
        print_json(json.dumps(response), indent=3)

    else:
        print("Missing -s argument. Please provide a site ID...")
        quit()

elif args.action == 'listsubaccounts':
    url= BASEURL + "prov/v1/accounts/listSubAccounts" 
    urlparams = { 'account_id': IMPV_ACCOUNT_ID }
    response = requests.post(url, data='', headers=headers, params=urlparams ).json()
    print_json(json.dumps(response), indent=3)

elif args.action == 'sitestatus':
    if args.s:
        url = BASEURL + "prov/v1/sites/status"
        urlparams = { 'site_id': args.s }
        response = requests.post(url, data='', headers=headers, params=urlparams ).json()
        del response['incap_rules']
        del response['security']
        print_json(json.dumps(response), indent=3)
        quit()
    else:
        print("Missing -s argument. Please provide a site ID...")
        quit()

elif args.action == 'getvisits':
    url = BASEURL + "visits/v1"
    if args.s:
        urlparams = { 'page_size': '5', 'site_id': args.s }
        if args.ip:
            urlparams = { 'page_size': '5', 'site_id': args.s, 'ip': args.ip }
        response = requests.post(url, data='', headers=headers, params=urlparams ).json()
        print_json(json.dumps(response), indent=3)
    else:
        print("Missing -s argument. Please provide a site ID...")
        quit()

else:
	print('Wrong or missing argument.')
	quit()




