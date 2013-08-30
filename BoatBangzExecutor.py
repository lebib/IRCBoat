#!/usr/bin/python3
#-*- coding: utf-8 -*-

# /!\ CHANTIER /!\

class Modulator:

    def __init__(self):
        self.bangzlib = {}
        print('Done!')
    def load(self, filename):
        mod = __import__('bangz.' + filename)
        mod = getattr(mod,filename)
        mod = mod.BangModule()
        print('loaded')
        print(mod.bangz.items())
        for bang, func in mod.bangz.items():
            self.bangzlib[bang] = func

    def execute(self, bang, args, dst, nick):
        print('exec',args)
        # TODO : gestion d'exeptions
        feedback = dst + '!' + nick
        return self.bangzlib[bang](args, feedback)



# run dat
#BBE = Modulator()
#BBE.load('LocalMod')
#try:
    #retour = BBE.execute('hello','niko')
    #print('retour:',retour)
#except:
    #pass

