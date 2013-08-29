#!/usr/bin/python3
#-*- coding: utf-8 -*-


class LocalMod:
    def __init__(self, user, args=None):
        self.args = args
        self.user = user

    def run(self, user, args):
        ''' !op nick '''
        rtrn = 'MODE ' + user + ' +o ' + args
        return rtrn