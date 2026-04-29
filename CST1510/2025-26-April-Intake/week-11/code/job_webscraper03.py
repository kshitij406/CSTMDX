# example 03 - weather extractor
# uses requests library - import using pip or similar
# uses beautiful soup for parsing web pages - import bs4 in pip or similar


# the libraries to use:
import requests
from bs4 import BeautifulSoup


import requests
from bs4 import BeautifulSoup


# get a web page! (alter as you wish)
page = requests.get("https://www.indeed.co.uk/jobs?q=python&l=London")


soup = BeautifulSoup(page.content, 'html.parser')

#find the first id attribut in table data tag
results = soup.find(id='resultsCol')
#print(results)

#find all cards
jobs =  results.find_all( class_='result')


# (a list so get the first item)
job = jobs[0]

title = job.find('h2')
title_link = job.find('a')

# print the number of jobs on the link
print('Number of jobs on the page:', len(jobs))

# or as a list comprehension
job_titles = [job.find('h2').find('a').text.strip() for job in jobs]
#print all titles!
print(job_titles)



# full description of a job
base_url = 'https://www.indeed.co.uk'

job_url = base_url +title_link['href']

print(job_url)
