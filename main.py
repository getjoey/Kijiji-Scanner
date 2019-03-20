import kijiji
from kijiji import KijijiParser

#SEARCH FOR SOMETHING AND PUT THE URL YOU WANT HERE.
#This is an example for search (PS4).
url = 'https://www.kijiji.ca/b-ville-de-montreal/ps4/k0l1700281?dc=true'

#HERE WE PUT keyWords and price range
keyWords = ["ps4","playstation", "4", "station", "console"]  #as long as 1 key word shows up itll be a hit!
priceRange = [250,500] 

#Create the object
k = KijijiParser(url,keyWords,priceRange)
k.runParser() #Run the search

Print("done")

#Here is some sample output 
#------------------------
#------------------------

"""
Starting Search on......
Url:  https://www.kijiji.ca/b-ville-de-montreal/ps4/k0l1700281?dc=true
Key Words :  ['ps4', 'playstation', '4', 'station', 'console']
PriceRange:  [150, 500]

Done Scanning for Kijiji Page Links
Got some pages

Got all items

Parsed items for keyWords

RESULTS:
Page # 0
0   ['console ps4 comme neuve / playstation 4 console like new', '280.00']
1   ['ps4 slim à vendre', '400.00']
2   ['ps4 1tb spider-man bundle (neuve) facture pour garantie', '380.00']
3   ['ps4 pro comme neuve!', '450.00']
4   ['ps4 pro 1500 gb', '450.00']
5   ['ps4 slim 1tb', '350.00']
Page # 1
0   ['console ps4 comme neuve / playstation 4 console like new', '280.00']
1   ['écouteur avec micro headphone astro a40 neuf pour ps4 et autre', '250.00']
Page # 2
0   ['console ps4 comme neuve / playstation 4 console like new', '280.00']
1   ['ps4 pro 1to neuf scellé', '500.00']
2   ['sony playstation 4', '360.00']
3   ['playstation 4 pro - 1tb - like new', '400.00']
4   ['recherché :billets de kiss à échanger contre ps4', '280.00']
Page # 3
0   ['console ps4 comme neuve / playstation 4 console like new', '280.00']
1   ['ps4 noir de jais 1to', '330.00']
2   ['jeux de ps4', '250.00']
Page # 4
0   ['console ps4 comme neuve / playstation 4 console like new', '280.00']
1   ['ps4 pro brand new avec battlefied 5', '460.00']
2   ['ps 4 - 1tb slim - spider-man bundle', '395.00']
Page # 5
0   ['console ps4 comme neuve / playstation 4 console like new', '280.00']
1   ['ps4 pro', '500.00']
2   ['console ps4 slim 1tb avec spider-man et red dead redemption 2', '350.00']
3   ['ps4', '300.00']
4   ['ps4 for sale.', '250.00']
Page # 6
0   ['console ps4 comme neuve / playstation 4 console like new', '280.00']
1   ['playstation 4 + 2 manettes +1 jeu', '350.00']
Page # 7
0   ['console ps4 comme neuve / playstation 4 console like new', '280.00']
1   ['ps4 a vendre', '280.00']
2   ['recherché :ps4 dans la boîte a vendre', '350.00']
3   ['console ps4 comme neuve / playstation 4 console like new', '280.00']
4   ['ps4 500gb + 5 games and tv', '400.00']
5   ['ps4 slim brand new for 440$ negotiable with fifa 2018 & nhl 2018', '440.00']

Done
"""
