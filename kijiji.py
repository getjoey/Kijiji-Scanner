from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import time

#SEARCH FOR SOMETHING AND PUT THE URL YOU WANT HERE.
#This is an example for search (PS4).
url = 'https://www.kijiji.ca/b-ville-de-montreal/ps4/k0l1700281?dc=true'

def getUrls(url):
	page_content = urlopen(url)
	time.sleep(3)
	soup = BeautifulSoup(page_content.read(), "html.parser")
	#get next page link
	next_pages = soup.find_all("span", class_="page-link")
	kijijiLinks = []
	for j in next_pages:
		kijijiLinks.append("https://www.kijiji.ca"+j.get("data-href"))
		
	print("Done Scanning for Kijiji Page Links")
		
	return kijijiLinks

def getItems(url):
	page_content = urlopen(url)
	time.sleep(3)
	#data = data.read()

	soup = BeautifulSoup(page_content.read(), "html.parser")

	titles = soup.find_all("div", class_="title")
	#for t in titles:
	#	print(t.a.string)

	#print(titles[0].find_all('a')[0].string)

	#for t in titles:	
	#	print(t.string)

	prices = soup.find_all("div", class_="price")
	#for p in prices:	
		#print(p.string)
		
	#lets make an array with tupples
	items = []
	for m, n in zip(range(len(titles)), range(len(prices))):
		try:
			tuple = [2]
			tuple[0] = titles[m].a.string.strip()
			tuple.append(prices[n].string.strip().replace("\xa0$",""))
			#tuple = {titles[m].a.string.strip(), prices[n].string.strip().replace("\xa0$","")}  
			#.strip removes the stupid whitespace and \n
			#the .replace is to remove the weird "\xa0$"
			items.append(tuple)
			#print(titles[m].a.string)
			#print(prices[n].string)	
		except:
			pass
			
	for a in items:
		print(a)


#main code
kLinks = getUrls(url)
print(kLinks)

for i in range(len(kLinks)):	
	print()
	print("i = ",i)
	getItems(kLinks[i])
	print("done ",i)
	print()


	

print("done")
