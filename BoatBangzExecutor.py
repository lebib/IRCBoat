#!/usr/bin/python3
#-*- coding: utf-8 -*-

# /!\ CHANTIER /!\

class Modulator:

    def __init__(self):
        self.bangzlib = {}

    def load(self, filename):
        mod = __import__('bangz.' + filename)
        mod = getattr(mod,filename)
        mod = mod.BangModule()
        for bang, func in mod.bangz.items():
            self.bangzlib[bang] = func

    def execute(self, bang, args):
        # TODO : gestion d'exeptions
        return self.bangzlib[bang](args)



# run dat
BBE = Modulator()
BBE.load('LocalMod')
try:
    retour = BBE.execute('hello','niko')
    print('retour:',retour)
except:
    pass

