#!/usr/bin/python3
#-*- coding: utf-8 -*-
import pickle
import bcrypt


class BOATUser():

  def __init__(self,username,password,globlevel=1):
    self.username = username
    self.logged = False
    self.nick = '' # current nick
    self.host = '' # nick!realname@host
    self.hashword = bcrypt.hashpw(password, bcrypt.gensalt(13))
    self.globlvl = 1
    self.chanlvls = {}


  def dump(self):
    print('##########################################################')
    print('name :', self.username, '\nhash :',self.hashword,'\ngloblvl :',self.globlvl,'\nchanlvls :',self.chanlvls)
    print('##########################################################')

  def login(self,who,password):
    if self.check_password(password) == True:
      self.host = who[0] + '!' + who[1]+ '@' + who[2]
      self.nick = who[0]
      self.logged = True
      return True

  def check_password(self,password):
    hashed = bcrypt.hashpw(password,bcrypt.gensalt(log_rounds=13))
    if bcrypt.hashpw(password,self.hashword) == self.hashword:
      return True
    else:
      return False

  def addchan(self,chan,lvl):
    print('addchan')
    try:
      self.chanlvls[chan] = lvl
      print('updating : ',self.chanlvls[chan])
      return True
    except KeyError:
      return False

  def remchan(self,chan):
    print('remchan')
    try:
      del self.chanlvls[chan]
      return True
    except KeyError:
      return False

  def getuserlevel(self, chan):
    try:
      return self.chanlvls[chan]
    except KeyError:
      return 0

  def getusername(self):
    return self.username

  def changechanlvl(self,chan,lvl):
    try:
      self.chanlvls[chan] = lvl
    except KeyError:
      return 0




class Auth():

    def __init__(self, boat):
        self.bangz = {
            'pprint': self.peopleprint,
            'picklepeople': self.picklepeople,
            'unpicklepeople': self.unpicklepeople,
            'dothedict': self.dothedict,
            'test': self.test,
            'peopleprint': self.peopleprint,
            'whoami': self.whoami
            }
        self.pcmd = {
          'identify': self.identify,
          'user': self.user,
          'register': self.register,
        }
        self.boat = boat
        self.boatpeople = {}
        self.unpicklepeople('i', 'd', 'c')

    def user(self, source, argz):
      ''' user del/mod username:#chan:[lvl] '''
      # parse
      print('user')
      if len(argz) != 2:
        self.boat.msg(source,' user del/mod username:#chan[:lvl] ')
        return False
      try:
        username = argz[1].split(':')[0]
        chan = argz[1].split(':')[1]
        if chan[0] != '#':
          self.boat.msg(source,' user del/mod username:#chan[:lvl] ')
          return False
      except IndexError:
        self.boat.msg(source,' user del/mod username:#chan[:lvl] ')
        return False
      if argz[0] == 'del':
        self.boatpeople[username].remchan(chan)
      # parse for optional lvl block
      try:
        lvl = int(argz[1].split(':')[2])
      except (IndexError, ValueError):
        self.boat.msg(source,' user del/mod username:#chan[:lvl] ')
        return False
      if argz[0] == 'mod':
        print('match')
        self.boatpeople[username].addchan(chan,lvl)

    def register(self, source, argz):
      '''  register username password '''
      newuser = BOATUser(argz[0],argz[1],1)
      self.boatpeople.update({newuser.username: newuser})


    def identify(self, source, argz):
      who = self.boat.whois(source)
      if self.boatpeople[argz[0]].login(who,argz[1]) == True:
        self.boat.msg(source,'success !')
      else:
        self.boat.msg(source,'FAILURE !')


    def whoami(self, dest, source, argz):
      if self.whois(source) is not False:
        self.boat.msg(dest,self.whois(source))
      else:
        self.boat.msg(dest,'Nobody !')


    def whois(self, source):
      who = self.boat.whois(source)
      host = who[0] + '!' + who[1]+ '@' + who[2]
      try:
        user = self.boatpeople[source]
      except KeyError:
        print('No one')
        return False
      if user.host == host and user.nick == source and user.logged == True:
        print('ya',user.host)
        return user.getusername()
      else:
        return False


    def hasrite(self,chan,user,subject):
        userlvl = user.getuserlvl()
        if isinstance(subject,BOATUser):
          subjectlvl = subject.getuserlvl()
        elif isinstance(subject,int):
          subjectlvl = subject
        else:
          return 0
        if userlvl > subjectlvl:
          return True
        else:
          return False


    def test(self, d, s, a=' '):
      for i in self.boatpeople.values():
        i.dump()


    def dothedict(self, dest, source, argz):
        self.boatpeople = {}
        newuser = BOATUser('pwny','acabpartout',1)
        newuser.dump()
        self.boatpeople.update({ newuser.getusername(): newuser })
        newuser = BOATUser('niko','mescoyes',1)
        newuser.dump()
        self.boatpeople.update({ newuser.getusername(): newuser })
        newuser = BOATUser('couscous','wesh1312',1)
        newuser.dump()
        self.boatpeople.update({ newuser.getusername(): newuser })
        print(self.boatpeople)

    def peopleprint(self, dest, source, argz):
       for user in self.boatpeople:
         for i in self.boatpeople.values():
           i.dump()

    def picklepeople(self, dest, source, argz):
        pickle.dump( self.boatpeople, open( "modulez/Auth/boatpeople.pkl", "wb" ) )

    def unpicklepeople(self, dest, source, argz):
        self.boatpeople = pickle.load(open( "modulez/Auth/boatpeople.pkl", "rb" ) )
