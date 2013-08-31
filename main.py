#!/usr/bin/python3
#-*- coding: utf-8 -*-

from IRCBoat import IRCBoat

import time


boat = IRCBoat('irc.pastafarai.me',
                    1337, 'funnyBOAT', 'V1.3', 'John BOAT')

boat.ssl_connect()
time.sleep(0.5)
boat.join("#discutoire")


while 1:
    #boat.refresh_bib_status()
    boat.listen_input()
