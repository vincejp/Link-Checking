import requests
import webbrowser
from bs4 import BeautifulSoup

"""
A script to open all links on a web page
Author: Vincent Perez
Date: July 7th 2021
Source: The code in this file is adapted from Geeks For Geeks
Usage: python3 web_script_1.py | grep {}
"""

# User enters the URL. Text does not display in program
# but user is prompted anyways. 

url = str(input("Enter URL: "))
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
webbrowser.open(url)
# TODO: Find citation link in HTML

urls = []
# Find all links in the page
for link in soup.find_all('a'):
    print(link.get('href'))
