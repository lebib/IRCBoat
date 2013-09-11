#!/usr/bin/python3
#-*- coding: utf-8 -*-

class BaseIRC():

    def __init__(self, boat):
        self.bangz = {
            'say': self.say,
            'op': self.op,
            'join': self.join,
            'topic': self.topic
            }
        self.boat = boat

    def say(self, dst, sender, argz):
        text = ''
        for arg in argz:
            text = text + ' ' + arg
        self.boat.msg(dst, text)

    def op(self, dst, sender, argz):
        self.boat.set_mode(dst, '+o', sender)

    def join(self, dst, sender, argz):
        self.boat.join(argz[0])

    def topic(self, dst, sender, argz):
        topic = ''
        for arg in argz:
            topic = topic + ' ' + arg
        self.boat.topic(dst, topic)
