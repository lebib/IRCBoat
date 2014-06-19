#!/usr/bin/python3
#-*- coding: utf-8 -*-

from urllib.parse import urlparse
from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup
import re
from pprint import pprint
import socket
import pickle

class URLLogger():

    def __init__(self, boat):
        self.bangz = {
            'urlz': self.urlz,
            'logswitch' : self.logswitch
            }
        self.boat = boat
        self.pkl = open('modulez/URLLogger/loggerdata.pkl','rb')
        self.dolog = False
        self.disclosure = True

    def logswitch(self, dest, source, argz):
        if self.dolog == True:
            self.dolog = False
            self.boat.msg(dest,'Logging is OFF')
        elif self.dolog == False:
            self.dolog = True
            self.boat.msg(dest,'Logging is ON')

    def eventchanmsg(self,source,dest,text):
        print('source:',source,'dest:',dest,'text:',text)
        for url in self.find_urls(text):
            print('URL :', url)
            self.handle_urlz(source,dest,text,url)

    def get_page_title(self,url):
        soup = url + ' down or bad link : '
        try:
            soup = BeautifulSoup(urlopen(url,timeout=5))
            ret = soup.title.string
            ret += ' ' + soup.h1.string
        except ValueError:
            try:
                soup = BeautifulSoup(urlopen('http://' + url, timeout=5))
                ret = 'Title : ' + soup.title.string
                ret += ' / ' + soup.h1.string
            except ValueError as e:
                print(e)
        except urllib.error.URLError as e:
            ret = url + ' down or bad link : ' + str(e)
            print(e)
        except socket.timeout as e:
            ret = url + ' down or bad link : ' + str(e)
            print(e)
        finally:
            return ret

    def handle_urlz(self,source,dest,text,url):
        if self.disclosure == True:
            print('DISCLOSING')
            title = self.get_page_title(url)
            title = title
            self.boat.msg(dest,title)
        if self.dolog == True:
            data = []
            with open('modulez/URLLogger/loggerdata.pkl','wb') as p:
                try:
                    data = pickle.load(p)
                    pprint(data)
                except ValueError as e:
                    print('fuck',e)
                newurl = {
                    'nick' : source,
                    'chan' : dest,
                    'url'  : url,
                    'title': self.get_page_title(url)
                    }
                data.append(newurl)
            try:
                with open('modulez/URLLogger/loggerdata.pkl','wb') as j:
                    p.dump(j, data)
            except TypeError:
                pass
        else:
            pass
    def urlz(self, dest, source, argz):
        data = pickle.load(self.pkl)
        pprint(data)


    def find_urls(self,text):
        pat_url = re.compile(  r'''
                                (?xi)
                                \b
                                (                           # Capture 1: entire matched URL
                                  (?:
                                    [a-z][\w-]+:                # URL protocol and colon
                                    (?:
                                      /{1,3}                        # 1-3 slashes
                                      |                             #   or
                                      [a-z0-9%]                     # Single letter or digit or '%'
                                                                    # (Trying not to match e.g. "URI::Escape")
                                    )
                                    |                           #   or
                                    www\d{0,3}[.]               # "www.", "www1.", "www2." … "www999."
                                    |                           #   or
                                    [a-z0-9.\-]+[.][a-z]{2,4}/  # looks like domain name followed by a slash
                                  )
                                  (?:                           # One or more:
                                    [^\s()<>]+                      # Run of non-space, non-()<>
                                    |                               #   or
                                    \(([^\s()<>]+|(\([^\s()<>]+\)))*\)  # balanced parens, up to 2 levels
                                  )+
                                  (?:                           # End with:
                                    \(([^\s()<>]+|(\([^\s()<>]+\)))*\)  # balanced parens, up to 2 levels
                                    |                                   #   or
                                    [^\s`!()\[\]{};:'".,<>?«»“”‘’]        # not a space or one of these punct chars
                                  )
                                )
                               ''')
        for url in re.findall(pat_url, text):
            yield url[0]
