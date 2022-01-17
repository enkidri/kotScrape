# kotScrape
A simple script written on python that checks if there is a new listing on this link: [KU Leuvens kotwijs](https://www.kotwijs.be/kamers-zoeken?prd_ads%5BsortBy%5D=prd_ads). If a new listing was found, then it will send an email from your own email to notify you about this change. The page is checked every 3 minutes but can be changed to be shorter or longer.

---

The script uses the selenium library and chrome as the browser for the checks. Some functions requires the latest version of chrome. As such, make sure that the chrome browser is at least version 97. If not then update the browser (3 dots on upper right -> help -> about chrome).

For people familiar with python, simply pip install the selenium library ("pip install selenium" in command prompt) and make sure you have chromedriver in your PATH ([[instructions](https://www.youtube.com/watch?v=dz59GsdvUF8)], [[download](https://sites.google.com/chromium.org/driver/)]). If your chrome version is v.97 then download ChromeDriver 97 (or any to match your browser). 

Before you run the script, make sure you have changed the email you want the notification to be sent to. Since you will be sending from your own email, you have to "log in" by writing your email adress and password also. This is somewhat unsafe since the script won't be encrypted, so I recommend setting up an temporary email adress to send from.

If you are not so familiar with python do the following:

1. Download and install python from their official page (google it) and make sure it python is added to PATH (there will be a choice to add it during the installation).
2. Open the command prompt (or terminal on mac) and write "pip install selenium".
3. Once the install finished, add chromedriver to your PATH (see above for instruction and download).
4. Run the script. It should start with "Monitoring (linkname)" if it works properly. My prefered method is to write "python3 kotScrape.py" in the command prompt. 
