from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import time

def getUrls(url):
	page_content = urlopen(url)
	time.sleep(1)
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
	time.sleep(1)
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
			tuple[0] = titles[m].a.string.strip().lower()
			p = prices[n].string.strip().replace("\xa0$","")
			p = p.replace(",",".")
			tuple.append(p)
			#tuple = {titles[m].a.string.strip(), prices[n].string.strip().replace("\xa0$","")}  
			#.strip removes the stupid whitespace and \n
			#the .replace is to remove the weird "\xa0$"
			items.append(tuple)
			#print(titles[m].a.string)
			#print(prices[n].string)	
		except:
			pass
	
	return items

def parseFor(kItems,keyWords, priceMin, priceMax):
	#items is our tuple [name, price]
	#We will parse for our keyWord, and range of price to show only!
	
	goodItems = []
	
	for i in kItems:
		try:
			found = 0 #ensures if multiple key words in string it doesnt add it multiple times...
			for k in keyWords:
				if(i[0].find(k.lower()) != -1 and found == 0):  #using lower to ensure always lower case
					if(float(i[1]) <= priceMax and float(i[1])>= priceMin):
						goodItems.append(i)
						found = 1
			found = 0
		except:
			pass
	
	return goodItems

def runIt(url, keyWords, priceRange):
	print()
	print("Starting Search on......")
	print("Url: ",url)
	print("Key Words : ",keyWords)
	print("PriceRange: ",priceRange)
	print()
	allItems = []
	goodItems = []
	
	#Step 1 get first 7 pages of searched linked
	kLinks = getUrls(url)
	print("Got some pages")
	print()

	#step 2 Get all items on those pages in a tuple[name,price]
	for i in kLinks:
		x = getItems(i)
		allItems.append(x)
	print("Got all items")
	print()

	#step 3 parse all items for our keywords, and price range
	for i in range(len(allItems)):
		goodItems.append(parseFor(allItems[i],  keyWords, priceRange[0], priceRange[1]))
	print("Parsed items for keyWords")
	time.sleep(1)
	print()
		
	#step 4 print them out nicely to show hits and page#
	print("RESULTS: ")
	for m in range(len(goodItems)):
		print("Page #",m)
		for n in range(len(goodItems[m])):
			print(n," ",goodItems[m][n])
	
	print()
	print("Done")
	

class KijijiParser:
	def __init__(self,url,keyWords,priceRange):
		self.url = url
		self.keyWords = keyWords
		self.priceRange = priceRange
		
	def runParser(self):
		url = self.url
		keyWords = self.keyWords
		priceRange = self.priceRange
		print()
		print("Starting Search on......")
		print("Url: ",url)
		print("Key Words : ",keyWords)
		print("PriceRange: ",priceRange)
		print()
		allItems = []
		goodItems = []
		
		#Step 1 get first 7 pages of searched linked
		kLinks = getUrls(url)
		print("Got some pages")
		print()

		#step 2 Get all items on those pages in a tuple[name,price]
		for i in kLinks:
			x = getItems(i)
			allItems.append(x)
		print("Got all items")
		print()

		#step 3 parse all items for our keywords, and price range
		for i in range(len(allItems)):
			goodItems.append(parseFor(allItems[i],  keyWords, priceRange[0], priceRange[1]))
		print("Parsed items for keyWords")
		time.sleep(1)
		print()
			
		#step 4 print them out nicely to show hits and page#
		print("RESULTS: ")
		for m in range(len(goodItems)):
			print("Page #",m)
			for n in range(len(goodItems[m])):
				print(n," ",goodItems[m][n])
		
		print()
		print("Done")


		

