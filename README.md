# latepeople

CEP Y3 end-of-year project. 

Used in RI 
System to Track students who 
- Are late for school
- Leave school early
Able to automatically send emails to form teachers of students for verification.   

# User's manual

## Installation:

1. Install python3 by searching on the internet "Download python3" and then choose either Python 3.7.0 or Python 3.6.1

2. Install the chrome extension CORS

3. Installing flask server and CSV libraries:
    
    Windows:
    1. Search "cmd" in search bar
    2. Right click "Command Prompt" and click "Run as Administrator"
    3. Type in _pip3 install pymongo pandas flask_

    Mac:
    1. Run terminal
    2. Type in _pip3 install pymongo pandas flask_

    A possible Error is ErrNo 61 of pymongo: in that case run "brew services start mongodb"

4. Installing Required Files:
    1. Download the files from github by clicking "Download ZIP"
    2. Extract the files into a new folder
    3. Drag the folder onto the desktop

## Running:

1. Open the file "index.html" in browser. 

2. Turn on CORS. 

3. Run the file "server.py" in the latepeople git folder using python launcher (3.7.0 or 3.6.1)
