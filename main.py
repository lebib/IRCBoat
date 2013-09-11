
#!/usr/bin/python3
#-*- coding: utf-8 -*-

from IRCBoat import IRCBoat

import time


boat = IRCBoat('irc.pastafarai.me',
                    1337, 'N1K0BOAT', 'V1.3', 'John BOAT')

boat.ssl_connect()
time.sleep(0.5)
boat.join("#test")
boat.join('#balek')
boat.load_module("BaseIRC")
boat.load_module("ModulezManager")


while 1:
    #boat.refresh_bib_status()
    boat.listen_input()
