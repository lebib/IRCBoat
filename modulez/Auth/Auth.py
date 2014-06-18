#!/usr/bin/python3
#-*- coding: utf-8 -*-



# attr :
#
#
# func :
#
# login, adduser, remuser, moduser
#
#
#
Class Auth():
    def __init__(self, boat):
        self.bangz = {
            }
        self.pcmd = {
          'identify': self.identify
        }
        self.boat = boat
