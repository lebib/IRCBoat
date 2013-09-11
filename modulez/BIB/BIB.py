#!/usr/bin/python3
#-*- coding: utf-8 -*-
from modulez.BIB.GetBIBState import GetBIBState
import time

class BIB():
    def __init__(self, boat):
        self.bangz = {
            'GetBIBState': self.get_bib_state
            }
        self.boat = boat
        self.bibstate = 0
        self.hardtopic = ''
        self.broadcastchan = '#discutoire'

    # BANG Methodz
    def get_bib_state(self, dst, nick, argz ):
        status = ''
        if self.bibstate == 0:
            status = 'Le BIB est fermé'
        elif self.bibstate == 1:
            status = 'Le BIB est ouvert'
        self.boat.msg(dst, status)


    # Kustom BIB Methodz
    def dtopic(self, msg=''):
        """Modifie le topic de #discutoire"""
        if msg != '':
            topic = msg
        self.boat.topic(self.broadcastchan, '[ ' +
                  ('BIB Ouvert' if self.bibstate else 'BIB Fermé')
                   + ' ][ ' + topic + ' ]' + self.hardtopic)

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
            # error !
            print('Erreur sur le retour du statut')
            return 2

    def refresh_bib_status(self):
        ''' Raffraîchit le topic selon l\'état  ouvert ou fermé du BIB '''
        if (time.time() - self.timestamp >= self.refreshrate):
            if self.check_bib_state() != self.oldstate:
                self.dtopic()
                self.timestamp = time.time()
                self.oldstate = self.bibstate
