import socket, ssl, os, time

class IRCConnect:
  """Improve the connection between the bot and IRC
  """

  def __init__(self, host, port, nick, ident, realname):
    """str, int, str, str, str
    host: irc.pastafarai.me
    port: 1337
    nick: Your nickname.
    ident: Your id.
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
  
  def raw_irc_command(self, cmd):
    """str->str
    cmd: The command to send.
    """
    return str(cmd)+'\r\n'

  def send(self,cmd):
    """str
    cmd: The command rawed to send.
    """
    cmd = self.raw_irc_command(cmd)
    self.socket.send(cmd.encode('utf-8'))

  def read_stream(self):
    """->str
    Return the content of the current stream.
    """
    self.stream_content = ''
    self.stream_content = str(self.socket.recv(2040).decode('utf-8'))
    if self.stream_content != '':
      self.stream_content = self.stream_content.split('\n')
      self.stream_content.pop()
      pass
    return self.stream_content


