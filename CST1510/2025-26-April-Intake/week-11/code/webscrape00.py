# example 00 - get a webpage and print it out, messy!
# uses requests library - import using pip or similar
# 


# the library to use:
import requests


# get a web page!
page = requests.get("https://google.co.uk")

# can access the status code (200 means success!)
print(page.status_code)

# can access the actual html and JS, and print it
print(page.content)

