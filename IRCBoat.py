from IRCConnect import IRCConnect

class IRCBoat:
  def __init__(self, irc_stream):
    """IRCConnect
    """
    self.irc_stream = irc_stream
  
  def read_stream(self):
  """Parser
  """


  ################################
  # BASIC IRC'S COMMANDS         #
  ################################

  def pong(self, ping):
    """str
    Address of the server.
    """
    pass

  def join(self, chan):
    """str
    Join chan.
    """
    pass

  def message(self, dest, message):
    """str, str
    Send a private message to dest.
    """
    pass

  def topic(self, chan, topic):
    """str, str
    Modify the topic of the chan.
    """
    pass

  def set_mode(self, chan, mode, nick=None):
    """str, str, str
    Modify the mode of the selected chan.
    """
    pass
 
