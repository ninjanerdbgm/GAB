from webscraping import download, xpath
import urllib2
import itertools
import random
import re

"""
===============================================
Web Scrapers
by bgm

Using webscraping (easy_install webscraping),
I fetch search results and then eek out info
using weird proprietary regex.

URL to webscraping docs:
http://docs.webscraping.com/

Looks odd, but it kind of works tho
===============================================
"""

"""
==============================================
Set user agent for mobile searches:
==============================================
"""

chrome = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"

nopc = noamazon = nobb = nogs = 0

def scrapeAmazon(gamename):
	AMA = download.Download(user_agent=None)

	search = gamename
	search = search.replace(" ","+")
	
	html = AMA.fetch("http://www.amazon.com/gp/search/ref=sr_il_ti_videogames?rh=n%3A468642%2Ck%3A{}&keywords={}&ie=UTF8&qid=1407988315&lo=videogames".format(search,search))
	if not html:
		noamazon=1
		print("Couldn't connect to Amazon's servers.")
		return noamazon

	gametitle = xpath.search(html, '//div[@class="ilt3"]//a//span[@class="lrg bold"]')
	productlinks = xpath.search(html, '//div[@class="ilt3"]//a/@href')
	gameprice = xpath.search(html, '//div[@class="ill3"]//span[@class="red bld"]')

	return (gametitle, productlinks, gameprice)

def scrapeBB(gamename):
	BB = download.Download(user_agent=None)

	search = gamename
	search = search.replace(" ","+")
	
	html = BB.fetch("http://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&type=page&ks=960&st={}&sc=Global&cp=1&sp=&qp=category_facet%3DVideo+Games~abcat0700000&list=y&usc=All+Categories&nrp=15&iht=n&seeAll=".format(search))
	if not html:
		nobb=1
		print("Couldn't connect to Best Buy's servers.")
		return nobb

	gametitle = xpath.search(html, '//h3[@itemprop="name"]//a')
	productlinks = xpath.search(html, '//h3[@itemprop="name"]//a/@href')
	gameprice = xpath.search(html, '//span[@itemprop="price"]')

	return (gametitle, productlinks, gameprice)

def scrapeGamestop(gamename):
	GS = download.Download()

	search = gamename
	search = search.replace(" ","+")
	
	html = GS.fetch("http://www.gamestop.com/browse?nav=16k-3-{},28zu0".format(search))
	if not html:
		nogs=1
		print("Couldn't connect to Gamestop's servers.")
		return nogs
	
	gametitle = xpath.search(html, '//div[@class="product_info grid_12"]//a[1]')
	productlinks = xpath.search(html, '//div[@class="product_info grid_12"]//a[1]/@href')
	gameprice = xpath.search(html, '//p[@class="pricing"]')

	return (gametitle, productlinks, gameprice)

def scrapePC(gamename, con=None):
	search = gamename
	search = search.replace(" ", "+")
	search = search.lower()

	if con:
		console = con
#		console = console.replace("{}".format(console),"\"{}\"".format(console))
	else:
		console = None
	
        PC = urllib2.Request("https://www.duckduckgo.com/html/?q=!ducky+{}+site%3Apricecharting.com+t%3A{}+prices".format(console, search))
		
	url = urllib2.urlopen(PC)
	infopage = url.read()
	redir = url.geturl()

	if "duckduckgo" in redir:
		nopc=1
		print("No results were found for {}!".format(gamename))
		return nopc
	
	gamedata = []

        gameinfo = xpath.get(infopage, '//h1[@id="product_name"') # Get the game's title
	gametitle = gameinfo.strip("Prices")
	gametitle = gametitle.strip(" \t\n\r")
	print("GAMEINFO: {}".format(gametitle))
        gamedata.append(gametitle)
        gamedata.append(redir) 
        release = xpath.get(infopage, '//span[@class="date"]') # Get the game's release date
        release = release.strip(" \t\n\r")
        gamedata.append(release)
        upc = xpath.get(infopage, '//span[@class="attribute"]/span') # Get the UPC code
	upc = upc.strip(" \t\n\r")
        gamedata.append(upc)
        lp = xpath.get(infopage, '//td[@id="used_price"]/span') # Get the loose price
        lp = lp.strip(" \t\n\r")
        gamedata.append(lp)
        cib = xpath.get(infopage, '//td[@id="complete_price"]/span') # Get the CIB price
        cib = cib.strip(" \t\n\r")
        gamedata.append(cib)
        np = xpath.get(infopage, '//td[@id="new_price"]/span') # get the New price
        np = np.strip(" \t\n\r")
        gamedata.append(np)
	c = xpath.get(infopage, '//h2[@class="chart_title"]/a') # get the formatted console name
	c = c.strip(" \t\n\r")
	gamedata.append(c)

	return gamedata


	


