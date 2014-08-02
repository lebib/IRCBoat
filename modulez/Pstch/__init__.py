#!/usr/bin/python3
#-*- coding: utf-8 -*-
#from IRCBoat import level
from .base import Module


class PrototypeModule(Module):
    def say(self, dst, source, argz):
        text = ''
        for arg in argz:
            text = text + ' ' + arg
        self.boat.msg(dst, text)

    def op(self, dst, source, argz):
        self.boat.set_mode(dst, '+o', source)

    def join(self, dst, source, argz):
        self.boat.join(argz[0])

    def topic(self, dst, source, argz):
        topic = ''
        for arg in argz:
            topic = topic + ' ' + arg
        self.boat.topic(dst, topic)
