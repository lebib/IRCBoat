#!/usr/bin/python3
#-*- coding: utf-8 -*-
#
#
#
# A l'attention des singes codeurs de BOAT :
#
# Convention de nommage (PEP-8):
    # classes : CorrectClassName
    # exceptions : IncorrectClassNameError (suffixe "Error" !)
    # fonctions : get_correct_number()
    # méthodes : get_correct_number(self, arg1=None, arg2, arg3)
    # arguments des méthodes et fonctions : get_correct_number(random=False, arg2)
    # variables : number = my_object.get_correct_number()
    # constantes : ANSWER_TO_LIFE_UNIVERSE = 42
#
#
#
# imports utiles aux anciennes fonctions, à moduler plus tard (pour moi)
# from fractions import Fraction as fr
# from random import randrange
# import sys, random, math
import socket
import time
import ssl
import os
from urllib.request import urlopen
from urllib.error import URLError

class IRCBoat():

    def __init__(self, host, port, nick, ident, realname):
        self.host = host
        self.port = port
        self.nick = nick
        self.ident = ident
        self.realname = realname
        self.users = ['niko', 'pwny'] # Default users for BOAT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = '' # Data read from chanz
        self.bangzlist = {} # Dictionnary containing the module functions availables
        self.timestamp = time.time()
        self.refreshrate = 5
        self.modulez = {} # Dictionnary containing the modules installed

    def load_module(self, modulename):
        if modulename not in self.modulez.keys():
            newmodule = __import__('modulez.' + modulename + '.' + modulename, fromlist=[modulename])
            print(newmodule)
            print(dir(newmodule))
            #moduleclass_ = getattr(newmodule, "BaseIRC")
            moduleclass_ = getattr(newmodule, modulename)

            self.modulez[modulename] = moduleclass_(self)
            print(modulename + ' loaded')
            for bang, func in self.modulez[modulename].bangz.items():
                if bang in self.bangzlist.keys():
                    print("Le bang est déjà utilisé => ignoré")
                else:
                    self.bangzlist[bang] = func
        else:
            print("Module déjà chargé")

    # Methodes
    #
    # Methodes de connexions
    # TODO : Fonction de connection normale

    def connect(self):
        pass

    def ssl_connect(self):
        """Connection au serveur en SSL"""
        self.socket.connect((self.host, self.port))
        self.socket = ssl.wrap_socket(self.socket, keyfile=None,
                                      certfile=None, server_side=False,
                                      do_handshake_on_connect=False,
                                      suppress_ragged_eofs=True)
        self.raw_irc_command('NICK ' + self.nick)
        print(('USER ' + self.ident + ' ' + self.host + ' :' + self.realname))
        self.raw_irc_command('USER ' + self.ident + ' ' + self.host + ' '
                             + self.host + ' :' + self.realname)
        print('Connexion OK')

    # Authentication processing TODO
    def is_boat_user(self, nick):
        return nick in self.users

    def clean_buffer(self, buffr):
        clean = []
        for item in buffr:
            clean.append(item.strip())
        return clean

    # BOAT Commandz
    def exec_bang(self, msg):  # à rename..
        nick = msg[0].split('!')[0].split(':')[1]
        dst = msg[2]  # chan
        cmd = msg[3].strip().split(':')[1]
        argz = msg[4:]
        if self.is_boat_user(nick):
            print(('Utilisateur ' + nick + " : BOAT'd"))
            if dst.find('#') != -1:
                if self.is_bang(cmd):
                    msg = self.clean_buffer(msg)
                    bang = cmd.split('!')[1]
                    print('bang :', bang)  # my baby shot me down
                    if bang in self.bangzlist.keys():
                        retour = self.bangzlist[bang](dst, nick, argz)
                        print(retour)
        # TODO : methode d'auth séparée
        elif dst.find(self.nick) != -1:
            if msg[3].find('login') and msg[4].find('passware'):
                self.users.append(nick)
                print(nick + ' ajouté aux utilisateurs !')

    def is_bang(self, cmd):
        if cmd[0] == '!':
            # TODO : cherche si c'est un bang qui retourne une fonction
            return True
        else:
            return False

    # Data processing
    def listen_input(self):
        ''' Écoute les messages du serveur '''
        lines = self.process_buffer()
        for line in lines:
            msg = line.split(' ')
            if msg[0] == 'PING':
                self.pong(msg[1].split(":")[1])
            if msg[1] == 'PRIVMSG':
                self.exec_bang(msg)
                # TODO : méthode is_bang(arg1)

    def process_buffer(self):
        ''' Traitement initial du buffer '''
        self.buffer = ''
        try:
            self.buffer = str(self.socket.recv(4096).decode('utf-8'))
        except:  # TODO : présicer l'exception
            print('Erreur de récupération du buffer')
        print('Buffer : ')
        print(self.buffer)
        if self.buffer != '':
            self.buffer = self.buffer.split("\n")
            self.buffer.pop()
            pass
        return self.buffer

    def print_state(self):
        '''Dump du buffer (debug)'''
        print(self.socket.recv(4096))

    # Basic IRC methodz
    def pong(self, ping):
        ''' Fonction de réponse aux ping'''
        self.raw_irc_command('PONG ' + ping)
        print('Ping : ' + ping)

    def join(self, chan):
        ''' Joindre un chan '''
        self.raw_irc_command('JOIN ' + chan)

    def msg(self, dest, message):
        ''' Envoie un message sur un chan ou un user '''
        self.raw_irc_command('PRIVMSG ' + dest + ' :' + message)
        print(">" + dest, ":", message)

    def topic(self, chan, topic):
        self.raw_irc_command('TOPIC ' + chan + ' :' + topic)

    def set_mode(self, chan, mode, nick=None):
        ''' Change les modes d\'un salon ou d\'un user '''
        self.raw_irc_command('MODE ' + chan + ' ' + mode + ' ' + nick)
        print('mode', chan, mode, nick)

    def raw_irc_command(self, cmd):
        """Envoie de commande IRC brute"""
        self.send(str(cmd) + '\r\n')

    def send(self, data):
        ''' Envoie brut au socket '''
        self.socket.send(bytes(data, 'UTF-8'))

