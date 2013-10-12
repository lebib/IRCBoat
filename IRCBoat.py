from IRCConnect import IRCConnect

class IRCBoat:
  def __init__(self, irc_stream):
    self.irc_stream = irc_stream
    self.irc_stream.ssl_connect()
    self.irc_stream.send('NICK '+self.irc_stream.nick)
    self.irc_stream.send('USER '+self.irc_stream.ident+' '+self.irc_stream.host+' '
      +self.irc_stream.host+' :'+self.irc_stream.realname)
    self.irc_stream.send('JOIN #testbot2')
    self.irc_stream.send('PRIVMSG #testbot2 :Hello World')
    while 1:
      self.listen_input()

  def listen_input(self):
    """Get the content of the stream.
    """
    lines = self.irc_stream.read_stream()
    if lines != '':
      print(lines)
      for line in lines:
        msg = line.split(' ')
        #Insert analytics functions here.

  #######################
  # ANALYTICS FUNCTIONS #
  #######################
  
  def parser(self, stream_content):
    """str
    Parse the text and use functions for
    each case.
    """
    pass

  ########################
  # IRC BASIC'S COMMANDS #
  ########################

  def nick(self, nick):
    """str
    Set the nick of the bot.
    """
    self.irc_stream.send('NICK '+nick)
  def user(self, ident, host, realname):
    """str, str, str
    Auth on the server.
    """
    self.irc_stream.send('USER '+user+' '+host+' '+host+' :'+realname)
  def pong(self, ping):
    """str
    Answer to the server's ping.
    """
    self.irc_stream.send('PONG '+ping)
  def join(self, chan):
    """str
    Join the chan.
    """
    self.irc_stream.send('JOIN '+chan)
  def message(self, dest, msg):
    """str, str
    Send the message to the dest.
    Dest can be a channel or an user.
    """
    self.irc_stream.send('PRIVMSG '+dest+' :'+msg)
  def set_mode(self, chan, mode, nick=None):
    """str, str, str
    Change the mod of the channel.
    """
    self.irc_stream.send('MODE '+mode+' '+nick)


