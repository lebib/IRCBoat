IRCBoat
=======

Yet Another Object Oriented IRC BOAT written in python by datamonkeys and cipherponies

Got an API for custom modules in python that can handle !bangz, events and private commands

Will share and update BOATModules with BOATz all over the intertubes

Will datalove in BOAT swarms with network communication protocol between BOATz

With battery included (to be coded tho)


TODO :

-	Add a module for authentication/user management
-	Add verification on arguments for all methods
-	Add a module to record all links wrote on chans


How-to API :

You can write custom modules and load them in BOAT

Here's the structure of a BOAT module :
```

Class BOATModules():                     # bangs are chan commands prefixed with
                                         # a '!' :
    def __init__(self, boat):            # !bang arg1 arg2 arg3 ..... argn
                                         # BOAT will execute any bang seen in a
                                         # channel and defined in self.bangz
                                         #
        self.bangz = {  <--------------  # dictionnary linking bangz to the
            'bang': self.bang,           # associated function
            'bangbang': self.bangbang    #
            }                            #
        self.pcmd  = { <---------------- # and this is the same for private commands
            'pvt': self.pvt              #
        }                                #
    self.boat = boat                     # <----- boat main instance for callbacks
                                         #
    def bang(self, dst, source, argz):   # every bang will be called in his module
        # code here                      # with those 3 arguments :
                                         # dst : the #chan where the bang was called
    def bangbang(self, dst, source, argz): # source : the nick who did the bang
        # code here                      # argz : array containing trailing argz
                                         #
    def pvt(self, source, argz):         # private has just source, which is the nick
        # here, code                     # and argz[] containing trailing argz
                                         #
    def eventjoin(self,source,dest,text):# you can also trigger on IRC event by strictly
        # code, code also code           # naming your hook function one of those name
                                         # corresponding to various (not all for now) IRC events :
                                         # eventjoin, eventquit, eventpart, eventnick,
                                         # eventnotice, enventmode, eventtopic, eventkick
                                         #
                                         # arguments givent to the func when calling are :
                                         # source : who
                                         # dest : where
                                         # text : what
                                         # except for chanless events like nick where dest will
                                         # contain the new nick and text will be empty
                                         #

 Here are the callback function that you can use by calling boat main instance self.boat.methodname(argz) :


     def join(chan):
         ''' Joindre un chan '''

     def msg(dest, message):
         ''' Envoie un message à un chan ou un user '''

     def topic(chan, topic):
         ''' Change le topic d'un chan '''

     def set_mode(chan, mode, nick=None):
         ''' Change les modes d\'un salon ou d\'un user '''

     def raw_irc_command(cmd):
         """Envoie de commande IRC brute"""

     def send(self, data):
         ''' Envoie brut au socket '''


```

 You could use any boat method found in the main class IRCBoat.py, thoses are the
 ones you should use mainly.

 Happy hacking !
