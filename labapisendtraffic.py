#!/usr/bin/env python
######################################################
## CREATED BY BARTOSZ CHMIELEWSKI                   ##
## bartosz.chmielewski@thalesgroup.com              ##
######################################################
#
# The script send requests to API endpoints on lab.spm.pl host.  
# 
#


import requests 
import random
import string
import time
import datetime
import re
import math
import json
from urllib3.exceptions import InsecureRequestWarning


session1 = requests.session()
interval = 1
headers_get = {'Content-Type': 'application/json'}
headers_post = {'Accept': 'application/json', 'Content-Type': 'application/json'}
counter = int(1)

baseurl = "http://lab.spm.pl/api/"

def send_request(path, headers, data="", stateless=False, ):
    fullpath = "" + baseurl + path
    print("  ========")
    if data != "":
        print("\n  => POST QUERY:" + fullpath )
        print("     DATA:" + data + "\n")
        try:
            if stateless:
                response = requests.post(fullpath, headers=headers_post, data=data)
            else:
                response = session1.post(fullpath, headers=headers_post, data=data)
        except:
            print("Failed to send the request")
        else:
            print("  => RESPONSE CODE:", response.status_code)
            print("  => RESPONSE BODY:", response.text)
    
    else:
        print("\n  => GET QUERY:" + fullpath + "\n")
        try:
            response = session1.get(fullpath, headers=headers_get, verify=False)
        except:
            print("Failed to send the request")
        else:
            print("  => RESPONSE CODE:", response.status_code)
            print("  => RESPONSE BODY:", response.text)
    
    print("")         
    time.sleep(interval)


time_end  = time.time() + 60 * 58 


##################################
### START 
##################################

data = '{"username": "bartoszch", "password": "Test123123#"}'
send_request("login", headers_post, data)


while time.time() < time_end:
    
    int_now = datetime.datetime.now()
    int_midnight = datetime.datetime.combine(int_now.date(), datetime.time())
    int_seconds = (int_now - int_midnight).seconds
    
    interval = float(8.5) + 2 * (math.cos(((int_seconds / 86400) * 2) * math.pi))


    print("========================================================================")
    print("====== Repetition: " + str(counter) + ". Time left: " + str(int(time_end - time.time()))  + " Interval: " + str(interval))
    print("========================================================================")

    print("")

    send_request("GetSession", headers_get)


    a1 = str(random.randint(1,100))
    a2 = str(random.randint(1,100))
    data = "{\"arg1\":\"" + a1 + "\", \"arg2\":\"" + a2 + "\"}"
    send_request("GetSum", headers_post, data)


    send_request("GetProductOverview", headers_get)


    a1 = str(random.randint(1,10))
    a2 = str(random.randint(1,6))
    data = "{\"category\":\"" + a1 + "\", \"id\":\"" + a2 + "\"}"
    send_request("GetProduct", headers_post, data)


    a1 = str(random.randint(1,200))
    data = "{\"id\":\"" + a1 + "\"}"
    send_request("GetUserData", headers_post, data)


    send_request("GuestBook", headers_get)


    a1 = random.randint(1,20)
    if a1 == 10:  password_to_send = "TestXXX123#"
    else: password_to_send = "Test123123#"
    data = json.dumps({ "username": "bartoszch", "password": password_to_send })
    send_request("login", headers_post, data, True)


    print("\n\n")
    counter = counter + 1





