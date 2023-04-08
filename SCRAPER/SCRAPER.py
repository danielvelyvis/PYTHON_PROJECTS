import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to scrape
url = 'https://seekingalpha.com/symbol/AAPL'

# Send a request to the website and get the HTML response
response = requests.get(url)


html = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print (response.status_code)

"""
print(soup.prettify())

# Print the title of the website
print(soup.title.text)

# Print all the links in the website
for link in soup.find_all('a'):
    print(link.get('href'))
"""