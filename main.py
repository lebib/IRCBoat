
#!/usr/bin/python3
#-*- coding: utf-8 -*-

from IRCBoat import IRCBoat

import time

def level(flevel):
  print("inside lvl")
  def mod_exec(func):
    print('inside mod_exec')

    def wrapper(fnc, dest, source, argz):
      print('will debug: {0},{1} {2} {3}'.format(dest, source, argz))
      print('inside wrapper, flevel is {0}'.format(flevel))
      return func(dest, source, argz)

    return wrapper
  return mod_exec




boat = IRCBoat('5.39.80.229',
                    6667, 'tehBOAT', 'V1.3', 'John BOAT')

boat.connect()
time.sleep(0.5)
#boat.join("#discutoire")
boat.join('#balek')
boat.join('#test')
boat.load_module("BaseIRC")
boat.load_module("ModulezManager")
boat.load_module('Souleicous')
boat.load_module('URLLogger')
boat.load_module('Auth')

while 1:
    #boat.refresh_bib_status()
    boat.listen_input()
