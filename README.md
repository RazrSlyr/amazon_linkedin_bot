# Amazon Linked In Bot!

Hi, my name is Rohan Venkatapuram! I was recently at a virtual Amazon recruitment fair and made a google doc for everyone to put their linkedins. I decided to also create a bot that will automatically send a request to (almost) everyone on the doc.
To use this code, you will need to have the following installed;
- Python
- Selenium WebDriver (https://selenium-python.readthedocs.io/installation.html)
- Chrome
- ChromeDriver for your version of Chrome (https://sites.google.com/chromium.org/driver/downloads?authuser=0)

Once all of that is properly set up, fill in the information in the code (`webbrowse.py`) where it asks for you to add stuff (your linkedin username, password, message, and location to ChromeDriver) and then run it. At the moment it seems to skip some profiles (those with no Connect button and a select few with a Connect button). I will do my best to sort these out in the meantime. The `links.txt` has the links to all the linkedins at the time of posting this repo. I used a simple regex to grab them, and as a result it is very possible that there are some incorrect links in here, let me know if you find any. You will need `links.txt` in the same directory as `webbrowse.py` for the script to work.
