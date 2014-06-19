#!/usr/bin/python3
#-*- coding: utf-8 -*-
import pickle
import bcrypt

#class User():

class Auth():

    def __init__(self, boat):
        self.bangz = {
            'pprint': self.peopleprint,
            'pickledict': self.pickledict,
            'unpickledict': self.unpickledict,
            'dothedict': self.dothedict,
            'getuserinfo': self.getuserinfo,
            'test': self.test,
            'printpeople': self.printpeople,
            }
        self.pcmd = {
          'identify': self.identify,
          'user': self.user,
          'register': self.register,
        }
        self.boat = boat
        self.boatpeople = []
        self.unpickledict('i', 'd', 'c')

    def user(self, source, argz):
      ''' user add/del/mod username:#chan:[lvl] '''
      # parse
      if len(argz) != 2:
        self.boat.msg(source,' user add/del/mod username:#chan:[lvl] ')
        return
      try:
        username = argz[1].split(':')[0]
        chan = argz[1].split(':')[1]
      if chan[0] =! '#':
        self.boat.msg(source,' user add/del/mod username:#chan:[lvl] ')
        return
      except IndexError:
        self.boat.msg(source,' user add/del/mod username:#chan:[lvl] ')
        return
      if argz[0] == 'del':
        pass
      # parse for optional lvl block
      try:
        lvl = int(argz[1].split(':')[2])
      except (IndexError, ValueError):
        self.boat.msg(source,' user add/del/mod username:#chan:[lvl] ')
        return
      if argz[0] == 'mod':
        pass
      elif argz[0] == 'add':
        self.addchanuser(username,chan,lvl)

    def register(self, source, argz):
      '''  register username password '''

    def identify(self, source, argz):
      for i in self.boatpeople:
        if i['username'] == argz[0]:
          hashed = bcrypt.hashpw(argz[1],bcrypt.gensalt(log_rounds=13))
          if bcrypt.hashpw(argz[1],i['hashword']) == i['hashword']:
            print('password ok')
          else:
            print('password fail')

    def hasrite(self,chan,username,subject):
      for i in self.boatpeople:
        if isinstance(subject,int):
          if i['username'] == username:
            userlvl = i['username']['chanlvl'][chan]
          if i['username'] == subject:
            subjectlvl = i['username']['chanlvl'][chan]

        if userlvl > subjectlvl:
          return True
        else:
          return False

    def getuserinfo(self, d, s, a):
      for i in self.boatpeople:
        print('A:',a[0],i)
        if i['username'] == a[0]:
          print(i['username'])
          self.getuserlvl(a[0],d)

    def getuserlvl(self, user, chan):
      for i in self.boatpeople:
        if i['username'] == user:
          if chan in i['chanlvl'].keys():
            print(user + "'s level for",chan,'is',i['chanlvl'][chan])

    def changeuserlvl(self, username, chan, newlvl):
      for i in self.boatpeople:
        if i['username'] == username:
          if chan in i['chanlvl'].keys():
            i['chanlvl'][chan] = newlvl

    def changeusergloblvl(self, username, newlvl):
      for i in self.boatpeople:
        if i['username'] == username:
          i['globlvl'] = newlvl

    def addchanuser(self, username, chan, lvl):
      for i in self.boatpeople:
        if i['username'] == username:
          i['chanlvl'][chan] = lvl

    def adduser(self, username, password):
      tmp = {
      'username': username,
      'globlvl': 1,
      'hashword': bcrypt.hashpw(password, bcrypt.gensalt(13)),
      'chanlvl': {
        }
      }
      self.boatpeople.append(tmp)

    def remuser(self, username, chan):
      for i in self.boatpeople:
        if i['username'] == username:
          try:
            del i['chanlvl'][chan]
          except KeyError:
            print('user is not registered in this channel')


    def test(self, d, s, a):
      print('before :',self.boatpeople)

      #self.changeusergloblvl('pwny',16)
      self.adduser('couscous','wesh1312')
      #self.remuser('niko','#test')

      print('after :', self.boatpeople)

    def printpeople(self, d, s, a):
      print(self.boatpeople)

    def dothedict(self, dest, source, argz):
        self.boatpeople = [
          {
          'username': 'pwny',
          'globlvl': 16,
          'chanlvl': {
            '#discutoire': 8,
            '#test': 3
            }
          },
          {
          'username': 'niko',
          'globlvl': 16,
          'chanlvl': {
            '#discutoire': 5,
            '#test': 8
            }
          }
        ]
        print(self.boatpeople)

    def peopleprint(self, dest, source, argz):
        print(self.boatpeople)

    def pickledict(self, dest, source, argz):
        pickle.dump( self.boatpeople, open( "modulez/Auth/boatpeople.pkl", "wb" ) )

    def unpickledict(self, dest, source, argz):
        self.boatpeople = pickle.load(open( "modulez/Auth/boatpeople.pkl", "rb" ) )
