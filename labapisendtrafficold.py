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
from urllib3.exceptions import InsecureRequestWarning


session1 = requests.session()
interval = 1
headers1 = {'Accept': 'application/json', 'auth': 'Bartosz123:)'}
headers2 = {'Accept': 'application/json', 'auth': 'Bartosz123:)', 'Content-Type': 'application/json'}
headers2_na = {'Accept': 'application/json', 'Content-Type': 'application/json'}
headers3 = {'bchtags': 'BYPASS-ABP', 'Content-Type': 'application/x-www-form-urlencoded'}   
counter = int(1)


baseurl = "http://lab.spm.pl/api/"

def send_request(path, headers, data=""):
    fullpath = "" + baseurl + path
    print("  ========")
    if data != "":
        print("\n  => POST QUERY:" + fullpath)
        print("     DATA:" + data + "\n")
        try:
            response = session1.post(fullpath, headers=headers2, data=data)
        except:
            print("Failed to send the request")
        else:
            print("  => RESPONSE:", response.text)
    else:

        print("\n  => GET QUERY:" + fullpath + "\n")
        try:
            response = session1.get(fullpath, headers=headers1, verify=False)
        except:
            print("Failed to send the request")
        else:
             print("  => RESPONSE:", response.text)
    
    print("")         
    time.sleep(interval)

def send_login(password):
    fullpath = "https://lab.spm.pl/login.php"
    data = 'username=bartoszch&password=' + password + '&login='
    print("  ========")
    print("\n  => Sending LOGIN request to: " + fullpath + " with password " + password)
    try:
        response = requests.post(fullpath, headers=headers3, data=data).text
    except:
        print("  => FAILED to send the login request.")
    else:
        print("  => Successfully sent the login request")
        if "You have a valid session" in response:
            print("  => Login Successful!!!")
            cc = re.findall(r'\d\d\d\d \d\d\d\d \d\d\d\d \d\d\d\d', response)
            print("  => CC Number:", cc[0])
        elif "Wrong username or password" in response:
            print("  => Login Failed...")
        else:
            print("  => Result unknown...")
    print("\n========\n")
    time.sleep(interval)

time_end  = time.time() + 60 * 58 


while time.time() < time_end:
    
    int_now = datetime.datetime.now()
    int_midnight = datetime.datetime.combine(int_now.date(), datetime.time())
    int_seconds = (int_now - int_midnight).seconds
    
    interval = float(8.5) + 2 * (math.cos(((int_seconds / 86400) * 2) * math.pi))

    # interval = 0.1
    print("========================================================================")
    print("====== Repetition: " + str(counter) + ". Time left: " + str(int(time_end - time.time()))  + " Interval: " + str(interval))
    print("========================================================================")

    print("")

    send_request("GetTime", headers1)

    send_request("GetDayOfWeek", headers1)

    a1 = str(random.randint(1,100))
    a2 = str(random.randint(1,100))
    data = "{\"arg1\":\"" + a1 + "\", \"arg2\":\"" + a2 + "\"}"

    send_request("GetSum", headers2, data)

    # send_request("GetSum-Shadow", headers2, data)

    # send_request("GetSum-NoAuth", headers2_na, data)

    a1 = str(random.randint(1,10))
    a2 = str(random.randint(1,6))
    data = "{\"category\":\"" + a1 + "\", \"id\":\"" + a2 + "\"}"
    send_request("GetProduct", headers2, data)

    a1 = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(15))
    data = "{\"input\":\"" + a1 + "\"}"
    send_request("ReflectInput", headers2, data)

    a1 = str(random.randint(1,200))
    data = "{\"id\":\"" + a1 + "\"}"
    send_request("GetUserData", headers2, data)
    send_request("GetUserData-NoAuth", headers2_na, data)
    send_request("GetUserData-Shadow", headers2, data)

    # send_request("GetUserData-All", headers2, data)

    a1 = random.randint(1,20)
    if a1 == 10:
        password_to_send = "TestXXX123%23"
    else:
        password_to_send = "Test123123%23"
    
    send_login(password_to_send)

    print("\n\n")
    counter = counter + 1





