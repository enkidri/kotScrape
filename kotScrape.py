from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

def sendMail(email):
	msg = MIMEMultipart('alternative')
	msg['From'] = formataddr((str(Header('Tai Ta', 'utf-8')), 'lawliet@hotmail.se'))
	msg['Subject'] = "NEW LISTING ON KOTWIJS"
	msg['To'] = email

	html = "Number of detected listing is now: " + text + ". Click link to see the change<br><br> https://www.kotwijs.be/kamers-zoeken?prd_ads%5BsortBy%5D=prd_ads_last_updated"

	# Record the MIME types of text/html.
	msg.attach(MIMEText(html, 'html'))

	#Start connection with smtp server
	smtpObj = smtplib.SMTP('smtp-mail.outlook.com',587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login("lawliet@hotmail.se", "1987leviathan")
	smtpObj.sendmail("lawliet@hotmail.se", email, msg.as_string())
	smtpObj.quit()  

adress = "https://www.kotwijs.be/kamers-zoeken?prd_ads%5BsortBy%5D=prd_ads"
print("Monitoring started of", adress)

options = Options()
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

isStart = True
currText = ""
totalAmount = 0
while True:
	browser = webdriver.Chrome(options=options)
	currentTime = datetime.datetime.now().time();
	browser.get(adress)
	time.sleep(15)

	if isStart:
		currText = browser.find_element("css selector", "div.col-lg-2:nth-child(3)").text
		totalAmount = int(currText.split()[0])
		isStart = False
		continue
	try:
		text = browser.find_element("css selector", "div.col-lg-2:nth-child(3)").text
	except:
		print("An error occured this iteration")
	
	print(currentTime, end="")
	if text == currText:
		print(f": Nothing changed ({text})")
	else:
		print(f": Change occured ({text})")
		currText = text
		currentAmount = int(currText.split()[0])
		if currentAmount > totalAmount:
			print(f"{currentAmount - totalAmount} NEW LISTING DETECTED")
			sendMail("lawliet@hotmail.se")
			sendMail("elisa519@student.liu.se")
		totalAmount = currentAmount

	browser.close()
	time.sleep(60*3)


