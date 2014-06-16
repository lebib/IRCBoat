
#!/usr/bin/python3
#-*- coding: utf-8 -*-

from IRCBoat import IRCBoat

import time


boat = IRCBoat('5.39.80.229',
                    6667, 'tehBOAT', 'V1.3', 'John BOAT')

boat.connect()
time.sleep(0.5)
boat.join("#discutoire")
boat.join('#balek')
boat.load_module("BaseIRC")
boat.load_module("ModulezManager")
boat.load_module('Souleicous')
boat.load_module('URLLogger')


while 1:
    #boat.refresh_bib_status()
    boat.listen_input()
