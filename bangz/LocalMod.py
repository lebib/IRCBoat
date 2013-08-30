#!/usr/bin/python3
#-*- coding: utf-8 -*-


class BangModule:
    def __init__(self):
        self.bangz = {
            'hello': self.hello,
            'sayderp': self.derpity
            }

    def hello(self,args,feedback=None):
        retour = []
        for dude in args:
            retour.append('PRIVMSG ' + feedback.split('!')[0] + ' :' + ' hello ' + dude)
        return retour

    def derpity(self, args, feedback=None):
        retour = []
        derp = ''
        for i in range(int(args)):
            derp += 'derp'
        derp += '!'
        retour.append('PRIVMSG ' + feedback.split('!')[0] + ' :' + derp)
        return retour

