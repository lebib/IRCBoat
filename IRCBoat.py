from IRCConnect import IRCConnect

class IRCBoat:
  def __init__(self, irc_stream):
    """IRCConnect
    """
    self.irc_stream = irc_stream
    self.nick(self.irc_stream.nick)
    self.user(self.irc_stream.ident, self.irc_stream.host, self.irc_stream.realname)

  
  def listen_input(self):
  """Get the content of the stream.
  """
    lines = self.irc_stream.read_stream()
    if lines != '':
      print(stream)
      for line in lines:
        msg = line.split(' ')
        # insert analytics functions.

  ################################
  # BASIC IRC'S COMMANDS         #
  ################################
  def nick(self, nick):
    """str
    Set the nick of the bot.
    """
    self.irc_stream.send('NICK ' + nick)

  def user(self, ident, host, realname ):
    """str, str, str,
    Authing on the IRC server.
    """
    self.irc_stream.send('USER ' + ident + ' ' + host + ' ' 
      + host + ' :' + realname)

  def pong(self, ping):
    """str
    Address of the server.
    """
    self.irc_stream.send('')

  def join(self, chan):
    """str
    Join chan.
    """
    self.irc_stream.send('')

  def message(self, dest, message):
    """str, str
    Send a private message to dest.
    """
    self.irc_stream.send('')

  def topic(self, chan, topic):
    """str, str
    Modify the topic of the chan.
    """
    self.irc_stream.send('')

  def set_mode(self, chan, mode, nick=None):
    """str, str, str
    Modify the mode of the selected chan.
    """
    self.irc_stream.send('')
 
