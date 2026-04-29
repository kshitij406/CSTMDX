# example 01 - download a page and print it in a structured way
# uses requests library - import using pip or similar
# uses beautiful soup for parsing web pages


# the libraries to use:
import requests
from bs4 import BeautifulSoup


# get a web page!
page = requests.get("https://google.co.uk")

# we need a parser (a thing which splits info up!)
soup = BeautifulSoup(page.content, 'html.parser')

# print it out so a human can just about understand it
print(soup.prettify())
