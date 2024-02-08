#!/usr/bin/env python
######################################################
## CREATED BY BARTOSZ CHMIELEWSKI                   ##
## bartosz.chmielewski@imperva.com                  ##
######################################################
#
# This script validates websites listed in the file (provided as argument). The file must contain a site FQDN
# in every line (and nothing else). 
#

import argparse
import os
import requests
from urllib3.exceptions import InsecureRequestWarning
import socket
from netaddr import IPNetwork, IPAddress

requests.packages.urllib3.disable_warnings()

def check_imperva_ip(ipaddress):

    match = False
    imperva_IPs = { 
        "199.83.128.0/21",
        "198.143.32.0/19",
        "149.126.72.0/21",
        "103.28.248.0/22",
        "185.11.124.0/22",
        "192.230.64.0/18",
        "45.64.64.0/22",
        "107.154.0.0/16",
        "45.60.0.0/16",
        "45.223.0.0/16",
        "131.125.128.0/17" }
        
    for range in imperva_IPs:
        if IPAddress(ipaddress) in IPNetwork(range):
            match = True
    
    return match


parser = argparse.ArgumentParser(description="BCHNotes")
parser.add_argument('inputfile', help="Input File")
parser.add_argument('outputfile',  help="Output File")
args = parser.parse_args()

inputfilename = args.inputfile
outputfile = args.outputfile

if( os.path.exists(inputfilename) ):

    with open(inputfilename) as f:
        inputlines = f.read().splitlines() 

    print('URL,Status Code,Status Description,Is Status Code OK?,Onboarded To Imperva?,Error Message')
    for line in inputlines:
        if( len(line) == 0): quit()
        
        url = 'https://' + str(line)
        response_error = ""
        
        try:
            r = requests.get(url=url,verify=False)
            response_status_code = str(r.status_code)
            response_status_code_ok = r.ok
            response_error='None'
            response_reason=r.reason
        except requests.ConnectionError as e:
            response_error = e.args[0]
            response_status_code = '000'
            response_status_code_ok = False
            response_reason = 'Unknown'
                      
        try:
            response_ip = socket.gethostbyname(line)
        except:
            response_ip = 'NoName'
            onboarded_to_imperva = 'Unknown'
        
        
        if ( response_ip != 'NoName' ):
            response_onboarded_to_imperva = check_imperva_ip(response_ip)
            
        s = ','
        outputline = url + s + response_status_code + s + response_reason + s + str(response_status_code_ok) + s + response_ip + s + str(response_onboarded_to_imperva) + s + str(response_error)
        
        print( outputline )
    
