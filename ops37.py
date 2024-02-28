#!/usr/bin/env python

import requests

# Set the URL of the target website
I CANT FIND THE DEMO SCRIPT......

# Define the user agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# Define headers with user agent
headers = {
    'User-Agent': user_agent
}

# Send a GET request to the website
response = requests.get(url, headers=headers)

# Capture the cookie from the response headers
cookie = response.cookies.get_dict()

# Print the captured cookie
print("Captured Cookie:", cookie)

# Send a GET request with the captured cookie
response_with_cookie = requests.get(url, headers=headers, cookies=cookie)

# Print the HTTP text of the response with the captured cookie
print("Response with Captured Cookie:", response_with_cookie.text)



resource-chatgpt 

I can't find the demo script that we used for class today.. i will find it tomorrow morning.....
