a modular approach to rock paper scissors

write 2 python programs, a ref and a player

REF
rps-ref is a web app that exposes a REST api 

It allows people (or bots) to register as players or fans

BOT

rps-bot is a separate web-app that wraps an rpscontest bot
it has its own rest api for ref to post to
it posts to ref api 

REF
endpoints:
referee/register
POST to this with: 
	your status (player/fan)
	your name
	callback url 

returns:
    url to match (referee/match/<uuid>/)

referee/match/<uuid>/ready
POST to this with: 
	player name

returns:
   accepted 201

when both players have sent ready, ref will post to each bot with match uuid and a throw uuid (unique to each bot)
ref will also post to fans a match uuid to say match is beginning

match/<uuid>/throw/<uuid>
POST to this with:
     throw (rock, paper, scissors, forfeit)

returns:
	 accepted

once both bots have sent throws, ref will post to each bots callback url:
	matchresult (opponent throw, your throw, winner, opponent wins, ties, your wins)

ref will post matchresult to fans callback urls as well

This allows both bots and fans to control hardware with matchresults as they see fit.







some links:
http://www.bbc.com/news/technology-24803751
http://www.nytimes.com/interactive/science/rock-paper-scissors.html?_r=0
http://www.rpscontest.com/