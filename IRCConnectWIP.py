import socket, ssl, os, time

class IRCConnect:
  """Improve the connection between the boat and IRC"""

  def __init__(self, host, port, nick, ident, realname):
    """str, int, str, str, str
    host: irc.pastafarai.me
    port: 1337
    nick: your nickname
    ident: your id
    realname: "Lastname Firstname"
    """
    self.host = host
    self.port = port
    self.nick = nick
    self.ident = ident
    self.realname = realname
    
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.stream_content = ''

  def ssl_connect(self):
    """Initialize the connect to IRC in SSL.
    """
    self.socket.connect((self.host, self.port))
    self.socket = ssl.wrap_socket(self.socket, keyfile=None,
      certfile=None, server_side=False,
      do_handshake_on_connect=False,
      suppress_ragged_eofs=True)
    self.send('NICK ' + self.nick )
    self.send('USER ' + self.ident + ' ' + self.host + ' ' + self.host + ' :' + self.realname ) # must be overlated

  def raw_irc_command(self, cmd): 
    """str -> str
    cmd: The command to send.
    """
    return str(cmd)+'\r\n'

  def send(self, cmd):
    """str
    cmd: The command rawed to send.
    """
    cmd = self.raw_irc_command(cmd)
    self.socket.send(cmd.encode('utf-8')) #change for p3.*
  
  def read_stream(self):
    """-> str
    Return the content of the current stream.
    """
    self.stream_content = ''
    self.stream_content = self.socket.recv(2040)
    if self.stream_content != '':
      self.stream_content = self.stream_content.split('\n')
      self.stream_content.pop()
      pass
    return self.stream_content

  def listen_input(self): #will go on IRCBoat
    """Read the stream content and do things in consequences.
    """
    lines = self.read_stream()
    if lines == '':
      return
    print(lines)
    for line in lines:
      msg = line.split(' ')
      if msg[0] == 'PING':
        self.send('PONG ' + msg[1].split(':')[1]) # must be overlated
