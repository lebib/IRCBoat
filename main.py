#from IrcConnect import *
#import sys
#import socket

#server = 'irc.pastafarai.me'
#channel = '#testbot'
#botnick = 'botty'

#irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#irc = ssl.wrap_socket(irc, keyfile=None,
#				certfile=None,server_side=False,
#				do_handshake_on_connect=False,
#				suppress_ragged_eofs=True)
#print "Connecting to:"+server
#irc.connect((server,1337))
#irc.send("USER "+ botnick + " " + botnick + " " + botnick +" :This is fun bot!\n")
#irc.send("NICK "+ botnick + "\n" )
#irc.send("JOIN "+ channel + "\n" )

#while 1:
#	text = irc.recv(2040)
#	print text
#
#	if text.find('PING') != -1:
#		irc.send('PONG ' + text.split()[1] + '\r\n')
from IrcConnect import *

irc = IRCConnect('irc.pastafarai.me',1337,'ircbot','ircbot','irc bot')
irc.ssl_connect()
irc.raw_irc_command('JOIN #testbot')
irc.raw_irc_command('PRIVMSG #testbot :Hello World')
while 1:
	irc.listen_input()
