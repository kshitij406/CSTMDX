# example 02 - get a page and find html tags in it
# uses requests library - import using pip or similar
# uses beautiful soup for parsing web pages - import bs4 in pip or similar


# the libraries to use:
import requests
from bs4 import BeautifulSoup


# get a web page! (alter as you wish)
page = requests.get("https://google.co.uk")


soup = BeautifulSoup(page.content, 'html.parser')

#find the first image on the page
#print(soup.find('img'))

#find all the images and place into a python list
print(soup.find_all('img'))

#find the first hyperlink on page
#print(soup.find('a href'))

#find all the hyperlinks on the page and place into a python list
#print(soup.find_all('a'))
