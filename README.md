# kotScrape
A simple script on python that checks if there is a new listing on this link: [KU Leuvens kotwijs](https://www.kotwijs.be/kamers-zoeken?prd_ads%5BsortBy%5D=prd_ads). If a new listing was found, then it will send an email from your own email to notify you about this change. 

---

The script uses the selenium library and chrome as the browser for the checks. Some functions requires the latest version of chrome. As such, make sure that the chrome browser is at least version 97. If not then update the browser (3 dots on upper right -> help -> about chrome).

For people familiar with python, simply pip install the selenium library ("pip install selenium" in command prompt) and make sure you have chromedriver in your PATH ([[instructions](https://www.youtube.com/watch?v=dz59GsdvUF8)], [[download](https://sites.google.com/chromium.org/driver/)]). If your chrome version is v.97 then download ChromeDriver 97 (or any to match your browser). 

Before you run the script, make sure you have changed the email you want the notification to be sent to. Since you will be sending from your own email, you have to "log in" by writing your email adress and password also. This is somewhat unsafe since the script won't be encrypted, so I recommend setting up an temporary email adress to send from.

