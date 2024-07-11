# Link-Checking

This is an early version of a program to automate the process of link checking.

## Notes

A few different things happen when the command is run.
First,

```bash
python3 web_script_1.py
```

will run the first script, which prints out all of the URLs.
Next,

```bash
grep "viewcontent\|author\|doi" > urls.txt
```

will filter out the output from the previous script, and write all of the links
containing content, author links, and DOI links to a file called

```bash
urls.txt
```

.

## Usage

```bash
python3 web_script_1.py | grep "viewcontent\|author\|doi" > urls.txt && python3 web_script2.py
```
