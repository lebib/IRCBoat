#!/usr/bin/python3
#-*- coding: utf-8 -*-

# /!\ CHANTIER /!\
# TODO :
# Gestion d'exeption,
# redondance de bangs,
# controle input utilisateurs
#

class Modulator:

    def __init__(self):
        self.bangzlib = {}

    def load(self, filename):
        mod = __import__('bangz.' + filename)
        mod = getattr(mod,filename)
        mod = mod.BangModule()
        print('loaded')
        print(mod.bangz.items())
        for bang, func in mod.bangz.items():
            self.bangzlib[bang] = func

    def execute(self, bang, args, dst, nick):
        feedback = dst + '!' + nick
        return self.bangzlib[bang](args, feedback)



