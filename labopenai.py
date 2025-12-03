#!/usr/bin/env python
######################################################
## CREATED BY BARTOSZ CHMIELEWSKI                   ##
## bartosz.chmielewski@thalesgroup.com              ##
######################################################
#


import os
from openai import OpenAI

while True:
    data = input("Do you want to talk Directly (1) or via Imperva AI Firewall (2)? ")
    if data == '1':
        direct = True
        break
    elif data == '2':
        direct = False
        break

query=""

if direct:
    client = OpenAI()
    while True:
        query = input("\nWhat do you want to send to AI? (or type exit)\n  # ")
        if query == "exit": break
        response = client.responses.create(
        model="gpt-5-nano",
        input=query
        )
        print("\n========= The Response: =============\n", response.output_text)
        print("===================================== ")


else:
    client = OpenAI(base_url="https://ai-firewall.aifw-gw.service.imperva.com",
                    default_headers={"x-imperva-api-key": os.getenv("AIFIREWALL_API_KEY"),
                                    "x-target-url": os.getenv("ORIGINAL_LLM_PROVIDER_URL")})
    
    while True:
        query = input("\nWhat do you want to send to AI? (or type exit)\n  # ")
        if query == "exit": break            
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[{"role": "user", "content": query}],
        )
        print("\n========= The Response: =============\n", response.choices[0].message.content)
        print("===================================== ")



