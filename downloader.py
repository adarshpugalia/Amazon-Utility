import sys
import urllib, urllib2
import requests
from bs4 import BeautifulSoup
import subprocess
from time import gmtime, strftime, ctime
from datetime import datetime

# Getting the arguments for the subtitle.
arguments = sys.argv[1:]
product = arguments[1]
code = arguments[0]

# opener = urllib2.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
# urllib2.install_opener(opener)

# query = urllib.quote(arguments[0])
# url = 'http://subscene.com/subtitles/title?q=%s' % (query, page)
# url_response = urllib2.urlopen(url).read()
# print url_response 

results = requests.get("http://www.amazon.in/"+product+"/dp/"+code,  
              headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(results.text)
price = soup.find_all("div", id='price_feature_div')[0]
price_row = price.find_all("td", class_="a-span12 a-color-secondary a-size-base a-text-strike")[0].text
message = product + " Price: " + ' '.join(price_row.split()[0:])

dealprice = price.find_all("span", id='priceblock_saleprice')
if len(dealprice)>0:
	dealprice = dealprice[0].text
	message += " Sale: " + ' '.join(dealprice.split()[0:])

disocunt = price.find_all("tr", id='regularprice_savings')
if len(disocunt)>0:
	disocunt = disocunt[0]
	dprice =  disocunt.find_all("td", class_="a-span12 a-color-price a-size-base")[0].text
	message += " Disocunt: " + ' '.join(dprice.split()[1:])

subprocess.Popen(['notify-send', message])

cur_time = ctime()
message += " at " + cur_time + "\n"

with open("/home/achiever202/Work/Amazon-Utility/price.txt", "a") as myfile:
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
