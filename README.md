# Link-Checking

This is an early version of a program to automate the process of link checking.

## Notes

A few different things happen when the command is run.
First,

```bash
python3 web_script_1.py
```

will run the first script, which prompts the user
for a link to a page they wish to link check, and prints out all of the URLs on that page.
Next,

```bash
grep "viewcontent\|author\|doi" > urls.txt
```

will filter out the output from the previous script, and write all of the links
containing content, author links, and DOI links to a file called urls.txt.

Finally,

```bash
python3 web_script2.py
```

will open all of the URLs that were written to urls.txt with a 3 second break between opening links.
By default, the link to the page the user wishes to check links for will be opened first. Then,
each subsequent link is either a content, author, or DOI link.

## Usage

```bash
python3 web_script_1.py | grep "viewcontent\|author\|doi" > urls.txt && python3 web_script2.py
```

## Testing

This link comes from Collaborative Librarianship Volume 13, Issue 2

https://digitalcommons.du.edu/collaborativelibrarianship/vol13/iss2/1

On a successful run of the program, the following links will be opened:  
https://digitalcommons.du.edu/do/search/?q=bp_author_id%3A%223fc779a5-783f-494a-acf7-94beabf6cec0%22%20OR%20%28author%3A%22Chris%20Robinson-Nkongola%22%20AND%20-bp_author_id%3A%5B%2A%20TO%20%2A%5D%29&start=0&context=7293930  
https://digitalcommons.du.edu/do/search/?q=bp_author_id%3A%228662aaeb-0c14-4c74-8511-857664523534%22%20OR%20%28author%3A%22Carrie%20L.%20Forbes%22%20AND%20-bp_author_id%3A%5B%2A%20TO%20%2A%5D%29&start=0&context=7293930  
https://digitalcommons.du.edu/cgi/viewcontent.cgi?article=1525&context=collaborativelibrarianship  
https://digitalcommons.du.edu/cgi/viewcontent.cgi?article=1525&context=collaborativelibrarianship
