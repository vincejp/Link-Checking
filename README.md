# Link-Checking

## Usage

1. **Run the first script to extract data:**

   ```bash
   python3 web_script_1.py | grep "viewcontent\|author\|doi" > urls.txt && python3 web_script2.py
   ```

   This command will execute `web_script_1.py` and filter the output to include only lines containing `viewcontent`, `author`, or `doi`, saving the result to `urls.txt`.
   Then, once it is running, copy and paste the link you want to check.
