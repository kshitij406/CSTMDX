# example 03 - weather extractor
# uses requests library - import using pip or similar
# uses beautiful soup for parsing web pages - import bs4 in pip or similar


# the libraries to use:
import requests
from bs4 import BeautifulSoup


# pick a weather website and location (San Francisco)
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")

# set the parser (an extractor of info)
soup = BeautifulSoup(page.content, 'html.parser')

# find the information!
# find a section in the html with seven-day-forecast
seven_day = soup.find(id="seven-day-forecast")

# find the items within that section
forecast_items = seven_day.find_all(class_="tombstone-container")

# get tonights in particular! (a list so get the first item)
tonight = forecast_items[0]


# break the found information up further according to the labels
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

# print it all!
print(period)
print(short_desc)
print(temp)