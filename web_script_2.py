import webbrowser
import time
"""
Script to all of the URLs
URLs will be read from a file and opened using the webbrowser module
Author: Vincent Perez
Date: July 7th 2024
"""
# Open URL file for reading
url_file = open("urls.txt", "r")
for line in url_file:
    # Open the URL in the URL file
    webbrowser.open(line.strip())
    # Pause for 3 seconds before opening the next link
    time.sleep(3)
