import webbrowser
import time
"""
Script to be used alongside web_script_1.py
Opens all of the URLs
Author: Vincent Perez
"""
# Open URL file for reading
url_file = open("urls.txt", "r")
for line in url_file:
    # Open the URL in the URL file
    webbrowser.open(line.strip())
    # Pause for 3 seconds before opening the next link
    time.sleep(3)
