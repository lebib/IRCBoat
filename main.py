from IRCConnect import *
from IRCBoat import *
irc = IRCConnect('irc.pastafarai.me',1337,'ircbot','ircbot','irc bot')
#irc.ssl_connect()
#irc.send('JOIN #testbot2')
#irc.send('PRIVMSG #testbot2 :Hello World')
boat = IRCBoat(irc)
