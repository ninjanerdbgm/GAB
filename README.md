Game Arbitrage Bot
===

This is the public source for my reddit pricing bot.

It scours whatever subreddit specified for the following text:

!GAB "GAME NAME"

When it finds that, it will search Amazon, Best Buy, and Gamestop for prices on GAME NAME, and generate a post listing its findings.

It is designed to help find arbitrage between the three major online game retailers.

It currently only supports those three sites (as I had to build the xpathing manually and I got bored), but in the future, I'd like to add gog, humblebundle, and steam.

Usage
===

!GAB "GAME NAME"
  searches amazon, best buy, and gamestop for prices on GAME NAME and generates a reply listing its findings.
  
!GAB -pm "GAME NAME"
  same as above, but sends a pm to the user instead of replying.

[[game_name|console]]

More info can be found on the wiki page here:
http://www.reddit.com/r/multiplayers/wiki/game_arbitrage_bot
  
