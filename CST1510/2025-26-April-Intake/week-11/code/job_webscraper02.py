# example 02 - get a page and find html tags in it
# uses requests library - import using pip or similar
# uses beautiful soup for parsing web pages - import bs4 in pip or similar


# the libraries to use:
import requests
from bs4 import BeautifulSoup


# get a web page! (alter as you wish)
page = requests.get("https://www.indeed.co.uk/jobs?q=python&l=London")


soup = BeautifulSoup(page.content, 'html.parser')

#find the first id attribut in table data tag
results = soup.find(id='resultsCol')
#print(results)

#find all cards
jobs =  results.find_all(class_='result')

print(jobs)



