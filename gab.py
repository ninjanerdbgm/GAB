# Import the world.
import urllib2
from scrapers import *
from getconsole import getConsole
import praw
import sys, time
from pytz import timezone
from datetime import datetime
from time import strftime
import re
import mmap
from collections import Counter
import os

"""
=====================================================================
Game Arbitrage Bot
by bgm

VERSION 0.101
Alpha, but less so than of my StoryAggregatorBot.

Anyway.

The wiki for this bot can be found here:
http://www.reddit.com/r/multiplayers/wiki/game_arbitrage_bot

Here's a quick rundown:

This bot responds to a command such as:
!GAB "final fantasy 7"

When it sees that, it will scour some sites and get prices 
for final fantasy 7.

It also responds to [[gamename|console]] to search
pricecharting.com

Flags right now include:

-pm 		: send a pm instead of reply to message

It will them make a post allllllllllll about it in reply.

Send an email to ninjanerdbgm at gmail dot com with any questions.
=====================================================================
"""

# Configure stuff

BOT_USERNAME="" 
BOT_PASSWORD=""

V_LOGS=False # Change to True for verbose logging.  If True, logs everything output to terminal.  If False, logs hits and errors.
TIMEZONE="US/Pacific-New" # This is for logging only.  Get your timezone string from here: http://stackoverflow.com/questions/13866926/python-pytz-list-of-timezones

"""
=====================================================================
For the following, put the subreddits you want the bot active in.  
It could be just one:

SUBREDDITS="gamedeals"

Or it could be in multireddit form:

SUBREDDITS="gamedeals+gameawesomedeals+100timesgamingdealswwwgamingdeals100timesforever"
=====================================================================
"""

SUBREDDITS=""

# That's all the configuration needed atm

"""
==================================================================
Let's make functions!
==================================================================
"""

def find_all(str, sub):
        start = 0
        while True:
                start = str.find(sub, start)
                if start == -1: return
                yield start
                start += len(sub)

def log(string):
        with open('gablog', 'a') as logfile:
		localtz = timezone(TIMEZONE)
		getlt = datetime.now(localtz)
		now = getlt.strftime("%Y/%m/%d %H:%M:%S")
                logfile.write("{} - {}\n".format(now,string))
                print(string)
        logfile.close()

"""
=================
"""

log("Game Arbitrage Bot is now running...")

"""
=====================================================================
User agent stuffs

It's good reddit practice to not hide that this is a bot.
=====================================================================
"""

r = praw.Reddit('GameCollecting Game Arbitrage Bot, v0.001'
		'Listing game prices from three major sites.'
		'by /u/ninjanerdbgm')

log("Attempting to connect to reddit...")

loggedin=0

while loggedin==0:
	try:
		r.login(BOT_USERNAME, BOT_PASSWORD)
		loggedin=1
	except:
		log("Unable to connect.  Reddit might be down.  Trying again in a few minutes...")
		time.sleep(300)
log("Success!") # Whoo hoo!

"""
===================================================================
Define flags
===================================================================
"""

pmindex = "-pm"

"""
========
"""

while True:

	try:

		foundpostcount=0 # initialize a few counters to be used later
		cmdsreplied=0
		cmdsfailed=0
		hatedposts=0
	
		elipses="" # This is for a sweet animation later.
		
		""" 
		=====================================================================
		Open and read our replyids file to get the latest
		list of comments we've replied to.
		
		Previously, I had this outside of the loop and, man..
		Things got ugly.  That's all I'm saying.
		=====================================================================
		"""
		ids = open('replyids', 'r')
		cids = mmap.mmap(ids.fileno(), 0, access=mmap.ACCESS_READ)
		ids.close()
		upclibs = open('upclibrary', 'r')
		upcsn = mmap.mmap(upclibs.fileno(), 0, access=mmap.ACCESS_READ)
		upclibs.close()
	
		whatsubs = SUBREDDITS.split("+")
		whatsubs = [x if x.startswith("/r/") else "/r/" + x for x in whatsubs] # This is just to make the terminal output nice.
		
		if V_LOGS:	
			log("Searching {} posts for bot requests...".format(", ".join(whatsubs)))
		else:
			print("Searching {} posts for bot requests...".format(", ".join(whatsubs)))

		searchred = 0
	
		subreddit = r.get_subreddit(SUBREDDITS)
		getsubpostnew = subreddit.get_new(limit=100)
		getsubposthot = subreddit.get_hot(limit=200)	
		
		for submission in (getsubpostnew and getsubposthot):

			if "[[IGNORE]]" in submission.selftext or "[[IGNORE]]" in submission.title: # Should the bot specifically ignore this post?
				continue

			"""
			Check self posts for pricecharting requests
			"""
			
			if submission.selftext <> "":
				if "[[" in submission.selftext:
					if cids.find(submission.name) == -1:
						reply = "# &nbsp;\n"
		
			                        author = submission.author
			                        if author.name == BOT_USERNAME: # If, for some reason, this bot makes a selfpost with a command in it.
			                        	continue
			                        y = list(find_all(submission.selftext, "[["))
			                        z = list(find_all(submission.selftext, "]]"))
			
			                        numgames = len(y) # How many commands were posted?
			                        if numgames > 4:
			                        	numgames = 5
			
			                        i = 0
					
			                        while i < numgames:
			                        	search, game, console = "","",""
			                                x = y[i]+2
			                                consearch = 0
			
			                                while x < z[i]:
			                                	search += submission.selftext[x]
			                                        x+=1
			
			                                if "|" in search:
			                                	search = search.split("|")
			                                        game = search[0]
			                                        console = search[1]
			                                        if game:
			                                        	log("Found a selftext Price Chart request for {} on {}!".format(game,console))
			                                        else:
			                                                consearch = 1
			                                                log("Found a selftext Price Chart request for a console!")
							else:
			                                	game = search
			                                        console = ""
			                                        log("Found a selftext Price Chart request for {}!".format(game))
			
							print(console)
			                                game,console = getConsole(game,console)
			                                time.sleep(1)
			                                gamedata = scrapePC(game,console)
			                                time.sleep(1)
			
			                                if gamedata == 1:       # No search results.
			                                	"""
			                                        PLACEHOLDER!  How should we handle missing results?  I don't want to clog
			                                        up the post with "not found, sorry" messages.
			                                        """
								log("Couldn't find any results for {}!".format(game))
			                                        i+=1
			                                        continue
			
			
			                                """
			                                gamedata comes back as a list filled with info about the game.
			                                The order of the info in the list is:
			                                Game Name, Link URL, Release Date, UPC Code, Loose Price, CIB Price, and New Price.
			 
			                                Let's build our reply.
			                                """
			                                if consearch == 0:
			                                	reply += "###Prices for [{}]({}), released for {} on {}:\n".format(gamedata[0],gamedata[1],gamedata[7],gamedata[2])
			                                else:
			                                        reply += "###Prices for [{}]({}), released on {}:\n".format(gamedata[0],gamedata[1],gamedata[2])
			
			                                reply += " - Loose: **{}** | CIB: **{}** | New: **{}**\n\n".format(gamedata[4],gamedata[5],gamedata[6])
			
			                                log("    | Game Title: {}".format(gamedata[0]))
			                                log("    | Release Date: {}".format(gamedata[2]))
			                                log("    | UPC: {}".format(gamedata[3]))
			                                log("    | Loose Price: {}".format(gamedata[4]))
			                                log("    | CIB Price: {}".format(gamedata[5]))
			                                log("    | New Price: {}".format(gamedata[6]))
			                                log("    | URL to game: {}".format(gamedata[1]))
			                                log("    | Console: {}".format(gamedata[7]))
	
							if upcsn.find(gamedata[3]) == -1:
								with open("upclibrary", "a") as ids:
	                                                		ids.write("{}|{}|{}\n".format(gamedata[0],gamedata[7],gamedata[3]))
								ids.close()
			
			                                i+=1
			
			                        reply += "---\n"
			                        reply += "^I ^am ^a ^bot ^and ^this ^was ^done ^automatically. ^Please ^downvote ^this ^post ^if ^you ^want ^it ^removed.\n\n"
			                        reply += "[^View ^wiki ^to ^learn ^how ^to ^use ^this ^bot](http://www.reddit.com/r/multiplayers/wiki/game_arbitrage_bot) ^| [^What ^is ^a ^bot?](http://www.reddit.com/r/botwatch/wiki/faq) ^|                                                        [^Did ^this ^bot ^mess ^up?  ^Let ^me ^know!](http://www.reddit.com/message/compose/?to=ninjanerdbgm) ^| [^Source ^Code](https://github.com/ninjanerdbgm/GAB)"
			
			                        if "CIB" in reply:
			                        	try:
			                                	submission.add_comment(reply) # Post our built reply.
			                                        with open("replyids", "a") as ids:
			                                        	ids.write("{}\n".format(submission.name))
			                                                ids.write("{}\n".format(submission.id))
			                                                cmdsreplied+=1
			                                        ids.close()
			                                        log("    | Posted a reply.  The comment can be found here: {}".format(submission.short_link))
			                                except praw.errors.RateLimitExceeded:
			                                        log("    | Error posting reply.  Rate limit is in effect.")
			                                        cmdsfailed+=1
			                                        pass
	
				"""
				Done checking self posts, check comments
				"""
					
			submission.replace_more_comments(limit=None)
	
			for comment in praw.helpers.flatten_tree(submission.comments): # This flattens the comment tree.  This makes it so we can reply to comments no matter what level they are on.
			
				if cids.find(comment.id) == -1:
	
					if (cids.find(submission.id)) <> -1:
						subs = Counter()
						with open('replyids', 'r') as sc:
							for thing in sc:
								subs.update(re.findall(r'{}'.format(submission.id),thing))
						if subs[submission.id] > 20:
							log("I've already replied to this one topic too much.  Ignoring...")
							continue
						
					
					if "!GAB" in comment.body:
						author = comment.author
						if author.name == BOT_USERNAME: # Are we detecting our own post?  !GAB "GAME NAME" is in our post.  Let's skip it if so.
							continue
						log("Found a request!")
						ispm = comment.body
						pmflag = ispm.find(pmindex)
	
						reply = "Hello, /u/{}!  I am an arbitrage bot designed to help you find prices for games on some popular sites.\
	                                        	       \n^I'm ^in ^super ^beta, ^so ^expect ^bugs.".format(author.name)
	
						
						gamesearch = re.findall(r'"(.*?)"', comment.body) # Get all words between quotes after !GAB
						test=False
						x=0
						
						"""
						=============================================================
						The following block is for validating the commands received.
						=============================================================
						"""
						while not test:
							if isinstance(gamesearch,list) and len(gamesearch) > 1: # Did we find more than one instance of !GAB?
								gamesearch[x] = str(gamesearch[x]).strip('[]') # Strip python list markers
								gamesearch[x] = str(gamesearch[x]).strip("u'") # Strip some weird "u" character that appears for some reason.  Hell if I know why, but it's gone now.
								gamesearch[x] = str(gamesearch[x]).strip("'") # Strip quotes that surround each entry in the array.
							
								if len(gamesearch[x]) < 2 or not re.search('[A-Za-z0-9]{2,65}', gamesearch[x]): # Added regex here to stop my buddy from sending injections.  Thanks Chen.
									del gamesearch[x] # REMOVE THE HEATHENOUS ENTRY!
								else:
									test = True
									log("    | Hmm, someone made multiple requests in one post.  Let's just grab the first valid one.")
									reply += "\n\nI've detected a few requests in your comment.  Due to post length limitations, I only ran a search for the first valid one.".format(author.name)
									gamesearch = gamesearch[x]
	
	                                                else: # Did we only find one instance?  I guess if we keep deleting instances then we'll end up here.
								gamesearch = str(gamesearch).strip('[]')
	                                                        gamesearch = str(gamesearch).strip("u'")
	                                                        gamesearch = str(gamesearch).strip("'")
		
								if len(gamesearch) < 2 or not re.search('[A-Za-z0-9]{2,65}', gamesearch):
									log("    | Ooops, syntax was weird on this one.")
									log("    | Here's what I'm seeing: {}".format(gamesearch))
									log("    | Maybe it's an error, maybe it's on purpose.  Let's skip it and see if they edit their post.")
									break # Explained below.
								else:
									test = True                                                      
	
						if not test: # This is a catch-all.  Without the break above, you get an infinite loop.  But with it there, the parent loop continues to iterate with an unset variable (gamesearch).  
							continue  # This ensures the loop ends here.  It's a hasty fix, but it gets the job done. (I've been saying that a lot lately...)
						
						log("    | {} requested prices for {}".format(author.name, gamesearch))
	
						reply += "\n\nSearching prices for: **{}**".format(gamesearch)
						try:
							amtitles, amlinks, amprices = scrapeAmazon(gamesearch)
							bbtitles, bblinks, bbprices = scrapeBB(gamesearch)
							gstitles, gslinks, gsprices = scrapeGamestop(gamesearch)
						except:
							log("ERROR: Error connecting to servers.  Let's try again later.")
							continue # Just skip this post for now and get to it next go-around.
	
						x=0
	
						if len(amtitles) >= 10: # Did we get more than 10 results?  If so, post only the first ten.  If not, post what we have.
							lim = 10
						else:
							lim = len(amtitles)
	
						reply += "\n\n\n - **Amazon prices:**"
	
						if lim == 0:
	                                                reply += "\n\n    - **No results found!**\n\n    - *Either there was an issue connecting to Amazon's servers, or there were no search results.  Sorry!*"
						else:
							reply += "\n\n Game Listing | Price\n--- | ---"
	
	
						while x < lim:
							prices = amprices[x].strip()
							titles = amtitles[x].replace("|","/") # Again, weird proprietary characters.  These hasty fixes work super well, tho.
		
							reply += "\n[{}]({}) | {}".format(titles,amlinks[x],prices) # Build our result in reddit table format.
							x+=1
	
						if len(bbtitles) >= 10:
						        lim = 10
						else:
						        lim = len(bbtitles)
	
						x=0
	                  			reply += "\n\n\n - **Best Buy prices:**"
	
						if lim == 0:
	                                               reply += "\n\n    - **No results found!**\n\n    - *Either there was an issue connecting to Best Buy's servers, or there were no search results.  Sorry!*"
						else:
		                                       reply += "\n\n Game Listing | Price\n--- | ---"
	
	
						while x < lim:
							prices = bbprices[x].strip()
							titles = bbtitles[x].strip()
	
						        reply += "\n[{}](http://www.bestbuy.com{}) | {}".format(titles,bblinks[x],prices) # Best Buy and Gamestop only link local dirs.  We need to add the domain manually.
						        x+=1
	
						if len(gstitles) > 10:
						        lim = 10
						else:
						        lim = len(gstitles)
	
						x=0
						reply += "\n\n\n - **Gamestop prices:**"
	
						if lim == 0:
	                                                reply += "\n\n    - **No results found!**\n\n    - *Either there was an issue connecting to Gamestop's servers, or there were no search results.  Sorry!*"
						else:
		                                        reply += "\n\n Game Listing | Price\n--- | ---"
	
						
						while x < lim:
							prices = gsprices[x].strip()
	
						        reply += "\n[{}](http://www.gamestop.com{}) | {}".format(gstitles[x],gslinks[x],prices)
						        x+=1
	
						"""
						======================================================================
	
						Obligatory Footer
	
						======================================================================
						"""
						reply += "\n\nDo you want to give me a shot?  Simply type:\
							\n\n     !GAB \"GAME NAME\"\n\nYes, the quotes are important.  If you'd prefer a pm to a comment reply, try:\
							\n\n     !GAB -pm \"GAME NAME\""
						reply += "\n\n[^Send ^message ^to ^creator](http://www.reddit.com/message/compose/?to=ninjanerdbgm) ^| [^What ^is ^a ^bot?](http://www.reddit.com/r/botwatch/wiki/faq) ^|\
	                                                        [^Did ^this ^bot ^mess ^up?  ^Let ^me ^know!](http://www.reddit.com/message/compose/?to=ninjanerdbgm) ^| [^Source ^Code](https://github.com/ninjanerdbgm/GAB)"
		
						if pmflag > 1: # Do they want a pm?
							try:
								r.send_message(author.name, 'Your price request from {}!'.format(BOT_USERNAME), reply) # SEND THEM A PM!  
														# (tho if our bot has low link karma, I think this will send me a capcha request.)
								with open("replyids", "a") as ids:
									ids.write("{}\n".format(comment.id)) # Add this comment id to our list of things we never want to see again.
									ids.write("{}\n".format(submission.id)) # Add the submission ID as well.
									cmdsreplied+=1 # For later.
								ids.close()
								log("    | Sent a message to {} with his pricing request!".format(author.name))
							except:
								log("    | Error sending message.")
								cmdsfailed+=1 # For later.
								pass
						else:
							try:
								comment.reply(reply) # Post our built reply.
								with open("replyids", "a") as ids:
	                                                                ids.write("{}\n".format(comment.id))
									ids.write("{}\n".format(submission.id))
									cmdsreplied+=1
	                                                        ids.close()
								log("    | Posted a reply.  The comment can be found here: {}".format(comment.permalink))
							except praw.errors.RateLimitExceeded:
								log("    | Error posting reply.  Rate limit is in effect.")
								cmdsfailed+=1
								pass
				
					elif "[[" in comment.body: # Let's look for a pricecharting request.
						reply = "# &nbsp;\n"
	
						if "[[" in comment.body:
							what = comment
						else:
							what = submission
	
						author = what.author
						if author.name == BOT_USERNAME: # This bot's output doesn't usually make pricecharting requests of its own, but in case it gains sapience, let's ignore it.
							continue
						y = list(find_all(what.body, "[[")) # Find all instances of '[['
						z = list(find_all(what.body, "]]")) # Find all instances of ']]'
						
						numgames = len(y) # How many commands were posted?
						if numgames > 4:
							numgames = 5
	
						i = 0
				
						while i < numgames:
							search, game, console = "","",""
							x = y[i]+2	# So, we're getting the next instance of '[[' and grabbing the first character after the second [
							consearch = 0
		
							while x < z[i]:
								search += what.body[x]	# So let's grab everything between '[[' and ']]'
								x+=1
	
							if "|" in search:
								search = search.split("|") # Did the user specify a console?
								game = search[0]
								console = search[1]
								if game:
									log("Found a Price Chart request for {} on {}!".format(game,console))
								else:
									consearch = 1 # Did the user ONLY specify a console?
									log("Found a Price Chart request for a console!")
							else:
								game = search
								console = ""
								log("Found a Price Chart request for {}!".format(game))
	
							game,console = getConsole(game,console)
							time.sleep(1)
							gamedata = scrapePC(game,console)
							time.sleep(1)
	
							if gamedata == 1:	# No search results.
								"""
								PLACEHOLDER!  How should we handle missing results?  I don't want to clog
								up the post with "not found, sorry" messages.
								"""
								log("Couldn't find any results for {}!".format(game))
								i+=1
								continue
					
	
							"""
							gamedata comes back as a list filled with info about the game.
							The order of the info in the list is:
							Game Name, Link URL, Release Date, UPC Code, Loose Price, CIB Price, and New Price.
	
							Let's build our reply.
							"""
							if consearch == 0:
								reply += "###Prices for [{}]({}), released for {} on {}:\n".format(gamedata[0],gamedata[1],gamedata[7],gamedata[2])
							else:
	                                                        reply += "###Prices for [{}]({}), released on {}:\n".format(gamedata[0],gamedata[1],gamedata[2])
	
							reply += " - Loose: **{}** | CIB: **{}** | New: **{}**\n\n".format(gamedata[4],gamedata[5],gamedata[6])
	
							log("    | Game Title: {}".format(gamedata[0]))
							log("    | Release Date: {}".format(gamedata[2]))
							log("    | UPC: {}".format(gamedata[3]))
							log("    | Loose Price: {}".format(gamedata[4]))
							log("    | CIB Price: {}".format(gamedata[5]))
							log("    | New Price: {}".format(gamedata[6]))
							log("    | URL to game: {}".format(gamedata[1]))
							log("    | Console: {}".format(gamedata[7]))
		
							"""
							====================================
							Let's build a library of UPCs.  This might mitigate searching later.
							====================================
							"""
							if upcsn.find(gamedata[3]) == -1:
								with open("upclibrary", "a") as ids:
                                                                        ids.write("{}|{}|{}\n".format(gamedata[0],gamedata[7],gamedata[3]))
								ids.close()
							i+=1
	
						reply += "---\n"
						reply += "^I ^am ^a ^bot ^and ^this ^was ^done ^automatically. ^Please ^downvote ^this ^post ^if ^you ^want ^it ^removed.\n\n"
						reply += "[^View ^wiki ^to ^learn ^how ^to ^use ^this ^bot](http://www.reddit.com/r/multiplayers/wiki/game_arbitrage_bot) ^| [^What ^is ^a ^bot?](http://www.reddit.com/r/botwatch/wiki/faq) ^|                                                        [^Did ^this ^bot ^mess ^up?  ^Let ^me ^know!](http://www.reddit.com/message/compose/?to=ninjanerdbgm) ^| [^Source ^Code](https://github.com/ninjanerdbgm/GAB)"
						
						if "CIB" in reply:
							try:
		                                        	comment.reply(reply) # Post our built reply.
			                                        with open("replyids", "a") as ids:
				                                        ids.write("{}\n".format(comment.id))
		        		                                ids.write("{}\n".format(submission.id))
				                                        cmdsreplied+=1
			                                        ids.close()
			                                        log("    | Posted a reply.  The comment can be found here: {}".format(comment.permalink))
		                                        except praw.errors.RateLimitExceeded:
			                                        log("    | Error posting reply.  Rate limit is in effect.")
			                                        cmdsfailed+=1
			                                        pass
				else:
					foundpostcount+=1
			elipses += "." # Ooo yea grrl.  Get that sweet, sweet text animation grrl.
			sys.stdout.write("Working{}\r".format(elipses)) # THOSE ELIPSES ARE SO DYNAMIC
			sys.stdout.flush()
	
	        if V_LOGS:
			log("\nLooking for unpopular bot posts...")
		else:
			print("\nLooking for unpopular bot posts...")

	        user = r.get_redditor(BOT_USERNAME) # We wanna find our own posts.
	        for i in user.get_comments(limit=500):      # The limit here can be changed, but 500 posts is sufficient history for what we're trying to do.
	                
			if i.score <= 0: # Did some asshole downvote my bot to oblivion?
				log("        | Comment to post: \"{0}\" with an id of {1} currently has a score of {2}\n         ---> Post can be found here: {3}".format(i.submission.title,i.id,i.score,i.permalink))
	                        log("         ---> Ouch, it has a pretty low score.  Let's delete it.")
				hatedposts += 1
	#                        with open("replyids", "a") as ids:
	#				ids.write("{}".format(i.submission.id))
	                        i.delete() # Appease the assholes.
	
	        """ ======================== """
	
	
		if V_LOGS:
		        log("\nAll done for this round!  Here are some stats:\n========================================")
			time.sleep(1) # For reasons.
			log("Commands found and replied to: {}".format(cmdsreplied))
			log("Commands found, but couldn't reply to: {}".format(cmdsfailed))
			log("Commands already replied to: {}\n".format(foundpostcount))
			log("Own Posts Deleted: {}\n".format(hatedposts))
		else:
			print("\nAll done for this round!  Here are some stats:\n========================================")
                        time.sleep(1) # For reasons.
                        print("Commands found and replied to: {}".format(cmdsreplied))
                        print("Commands found, but couldn't reply to: {}".format(cmdsfailed))
                        print("Commands already replied to: {}\n".format(foundpostcount))
                        print("Own Posts Deleted: {}\n".format(hatedposts))
	
		time.sleep(1) # Again.
	        i=30 # I had this at 600, but this bot is ok running every 30 seconds instead of 10 minutes.  
			# You can always change it to whatever.  5 minutes should be ok tho.
	
	        """
	        ==========================================================================
	
	        Alright, all done.  Now we'll sleep for i/60 minutes and try again.
	        This can be modified, just change the variable i, above, to however
	        many seconds you want to wait.
	
	
	        The following bit of code counts down one second at a time, and outputs
	        the remaining time in mm:ss format.
	
	        ==========================================================================
	        """
	
	        while i > 0:
	#               os.system('clear') # This is old.  This cleared the screen, but I've removed it in favor of stdout.write and .flush to make it look better.
	                sys.stdout.write("This round of scouring is over!  {0:0>2}:{1:0>2} until the next round!\r".format((i/60),(i%60)))
	                sys.stdout.flush()
	                time.sleep(1)
	                i-=1 # Cizz-ount dizz-own.
	
	        print("\n-------------------------------------------\n")

		"""
		======================================
		Error handling stuff.
		======================================
		"""
		

	except urllib2.HTTPError, e: # Do we have an error connecting to reddit?
		if e.code in [429, 500, 502, 503, 504]: # If these are the error codes returned, then yes.
			log("Can't search reddit ({}).  It might be down.  Trying again in 30 seconds...".format(e.code))
			time.sleep(30)
			pass
		else:
			raise

	except (KeyboardInterrupt, SystemExit): # User hit CTRL+C
		log("The bot has been manually stopped.")
		raise

	except Exception, e: # I'm not entirely sure what the error is, but let's catch it anyway.
		log("I AM ERROR.  UNABLE TO REDDIT. --> {}".format(str(e)))
		time.sleep(60)
		pass
	
	"""
	"""
	
		
			
