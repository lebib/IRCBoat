import socket, ssl
import os, time

class IRCConnect:
	def __init__(self, host, port, nick, ident, realname):
		self.host = host
		self.port = port
		self.nick = nick
		self.ident = ident
		self.realname = realname

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.buffer = ''
		
	def ssl_connect(self):
		self.socket.connect((self.host, self.port))
		self.socket = ssl.wrap_socket(self.socket, keyfile=None,
				certfile=None,server_side=False,
				do_handshake_on_connect=False,
				suppress_ragged_eofs=True)
		self.raw_irc_command('NICK ' + self.nick )
		self.raw_irc_command('USER ' + self.ident + ' ' + self.host + ' ' + self.host +
				' :' + self.realname )

	def raw_irc_command(self, cmd):
		self.send(str(cmd)+'\r\n')
	
	def send(self, data):
		self.socket.send(data.encode('utf-8'))

	def read_stream(self): #Rework that.
		self.buffer = ''
		self.buffer = self.socket.recv(2040)
		print self.buffer
		if self.buffer != '':
			self.buffer = self.buffer.split("\n")
			self.buffer.pop()
			pass
		return self.buffer

	def listen_input(self):
		lines = self.read_stream()
		if lines == '':
			return
		for line in lines:
			msg = line.split(' ')
			if msg[0] == 'PING':
				self.raw_irc_command('PONG ' + msg[1].split(":")[1])
			if msg[1] == 'PRIVMSG':
				self.raw_irc_command('PRIVMSG #testbot :msg send by' + msg[0])


