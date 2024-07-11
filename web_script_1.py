import requests
import webbrowser
from bs4 import BeautifulSoup

"""
A script to fetch and print out all links from a webpage
Author: Vincent Perez
Date: July 7th 2024
The code in this file is adapted from Geeks For Geeks
Source: https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
"""

url = str(input("Enter URL: "))
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
webbrowser.open(url)

# List of all URLs to be written to a file 
urls = []
# Find all links in the page
for link in soup.find_all('a'):
    print(link.get('href'))
