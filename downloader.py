import sys
import urllib, urllib2
import requests
from bs4 import BeautifulSoup
import subprocess
from time import gmtime, strftime, ctime
from datetime import datetime

# Getting the arguments for the subtitle.
arguments = sys.argv[1:]

# opener = urllib2.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
# urllib2.install_opener(opener)

# query = urllib.quote(arguments[0])
# url = 'http://subscene.com/subtitles/title?q=%s' % (query, page)
# url_response = urllib2.urlopen(url).read()
# print url_response 

results = requests.get("http://www.amazon.in/gp/product/B00QJDOEAO",  
              headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(results.text)
price = soup.find_all("div", id='price_feature_div')[0]
price_row = price.find_all("td")
price_actual = price_row[1].find_all("span")[0].text

message = "Kindle Price: " + price_actual

dealprice = price.find_all("tr", id='priceblock_dealprice_row')
if len(dealprice)>0:
	dealprice = dealprice[0]
	dprice =  dealprice.find_all("td")[1].find_all("span")[0].text
	message += "    Deal price: " + dprice;

subprocess.Popen(['notify-send', message])

cur_time = ctime()
message += " at " + cur_time + "\n"

with open("price.txt", "a") as myfile:
    myfile.write(message.encode('utf-8'))
# table_rows = soup.find_all("td")
# print table_rows
# lis = soup.find_all("li")
# for i in lis:
# 	a = i.find("div", class_="title")
# 	if(a!=None):
# 		print a.find('a').text


# url_response = urllib2.urlopen(url).read()
# print url_response
