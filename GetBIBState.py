#!/usr/bin/python3
#-*- coding: utf-8 -*-

from html.parser import HTMLParser


class GetBIBState(HTMLParser):
    ''' Parse le site du bib pour rechercher son état ouvert ou fermé '''
    def __init__(self):
        self.state = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        ''' Cherche un attribut dans un tag HTML '''
        if attrs:
            if tag == "div" and attrs[0] == ('id', 'bibopen'):
                self.state = 1

    def get_state(self):
        ''' Booléen d\'état ouvert ou fermé du BIB '''
        return self.state
