#!/usr/bin/python3
#-*- coding: utf-8 -*-


class BangModule:
    def __init__(self):
        self.bangz = {
            'hello': self.hello,
            'sayderp': self.derpity
            }


    def hello(self,args):
        retour = 'hello ' + args + ' -_-'
        return retour
    def derpity(self,args):
        retour = ''
        for i in range(int(args)):
            retour += 'derp'
        retour += '!'
        return retour

