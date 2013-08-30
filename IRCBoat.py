#!/usr/bin/python3
#-*- coding: utf-8 -*-
#
#
#
# A l'attention des nerds pisseurs de codes de BOAT :
#
# Convention de nommage (PEP-8)
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
#imports utiles aux anciennes fonctions, à moduler plus tard (pour moi)
#from fractions import Fraction as fr
#from random import randrange
#import sys, random, math
import socket
import time
import ssl
from urllib.request import urlopen
from urllib.error import URLError
from GetBIBState import GetBIBState
from BoatBangzExecutor import Modulator

class IRCBoat(Modulator):
    def __init__(self, host, port, nick, ident, realname):
        self.host = host
        self.port = port
        self.nick = nick
        self.ident = ident
        self.realname = realname
        self.users = ['niko', 'pwny']
        self.bibstate = 0
        self.biburl = 'http://lebib.org'
        self.discutopic = "BOAT'd"
        self.hardtopic = '[ http://lebib.org/ ] [ 7 Rue François Périer, 34000 Montpellier ]'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = ''
        self.timestamp = time.time()
        self.refreshrate = 5
        self.BBE = Modulator()
        self.BBE.load('LocalMod')
        print(self.BBE.bangzlib)
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

    #Authentication processing TODO
    def is_boat_user(self, nick):
        return nick in self.users

    def clean_buffer(self,buffr):
        clean = []
        for item in buffr:
            clean.append(item.strip())
        return clean

    #BOAT Commandz
    def exec_bang(self, msg):  # anciennement execBoatCmd
        nick = msg[0].split('!')[0].split(':')[1]
        dst = msg[2] # chan
        cmd = msg[3].strip().split(':')[1]
        if self.is_boat_user(nick):
            print(('Utilisateur ' + nick + " : BOAT'd"))
            if dst.find('#') != -1:
                if self.is_bang(cmd):
                    msg = self.clean_buffer(msg)
                    bang = cmd[1:]
                    print('bang :',bang) # my baby shot me down
                    if bang in self.BBE.bangzlib:
                        retour = self.BBE.execute(bang,msg[4:],dst,nick)
                        for cmd in retour:
                            self.raw_irc_command(cmd)

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
        except: # TODO : présicer l'exception
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

    #Basic IRC methodz
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

    def topic(self, chan, msg):
        self.raw_irc_command('TOPIC ' + chan + ' :' + msg)

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

    #Custom Bib methodz
    # à moduler !
    def dtopic(self, msg=''):
        """Modifie le topic de #discutoire"""
        if msg != '':
            self.discutopic = msg
        self.topic('#discutoire', '[ ' +
        ('BIB Ouvert' if self.bibstate else 'BIB Fermé')
        + ' ][ ' + self.discutopic + ' ]' + self.hardtopic)

    def check_web_status(self):
        ''' Vérifie la connectivité vers le site web du BIB '''
        try:
            usock = urlopen(self.biburl)
            bibpage = urlopen(self.biburl).read()
            usock.close()
            parser = GetBIBState()
            parser.feed(bibpage.decode('utf8'))
            self.bibstate = parser.get_state()
        except URLError:
            print('urlopen timeout')
            pass

    def check_bib_state(self):
        """Récupération de l'état du BIB"""
        self.oldstate = self.bibstate
        print('Getting bib status...')
        self.check_web_status()
        if self.bibstate == 0:  # closed !
            print('Fermé !')
            return 0
        elif self.bibstate == 1:  # openBIB!
            print('Ouvert !')
            return 1
        else:
            #error !
            print('Erreur sur le retour du statut')
            return 2

    def refresh_bib_status(self):
        ''' Raffraîchit le topic selon l\'état  ouvert ou fermé du BIB '''
        if (time.time() - self.timestamp >= self.refreshrate):
            if self.check_bib_state() != self.oldstate:
                self.dtopic()
                self.timestamp = time.time()
                self.oldstate = self.bibstate
