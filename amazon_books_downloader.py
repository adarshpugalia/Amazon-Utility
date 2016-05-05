import sys
import urllib, urllib2
import requests
from bs4 import BeautifulSoup
import subprocess
from time import gmtime, strftime, ctime
from datetime import datetime
import re

# Getting the arguments for the subtitle.
arguments = sys.argv[1:]
book_id = sys.argv[1]
book = sys.argv[2]

results = requests.get("http://www.amazon.in/" + book + "/dp/" + book_id,  
              headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(results.text)
price = soup.find_all("div", id='buybox')[0]
#price_row = price.find_all("td")
price_actual = price.find_all("span", class_='a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P')[0].text
message = book + ": " + price_actual

discount = price.find_all("span", class_='a-size-base a-color-secondary')
if len(discount) > 0:
	message += "\t Discount: " + ' '.join(discount[0].text.split()[2:])

subprocess.Popen(['notify-send', message])

cur_time = ctime()
message += " at " + cur_time + "\n"

with open("/home/achiever202/Work/Amazon-Utility/price.txt", "a") as myfile:
    myfile.write(message.encode('utf-8'))