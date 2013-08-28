#!/usr/bin/python3
#-*- coding: utf-8 -*-

# /!\ CHANTIER /!\
class BoatBangzExecutor:

    def __init__(self):
        self.loadedmodules = []

    def bangprobe(self, bang):
        # Cherche si le module est load
        if bang not in self.loaded_modules:
            # ~ search & loading in module land ~
            # chaque bang est dans un module du même nom
            # dans le sous dossier modules/*.py
            # ex : module/op.py
            try:
                mod = __import__('modules/', bang,'.py')
                self.loadeddmodules.append(bang)
                self.loadedmodules.append(mod)
            except ImportError:
                print('debug : erreur d\'importation', mod)
        if mod:
            # le module est load
            self.exec_bang(self, self.bang, self.args)

        def exec_bang(self, mod, user, args):
            #retour = getattr(mod, 'run')(user, args)
            return retour

class LocalMod:

    def __init__(self, user, args=None):
        self.args = args
        self.user = user

    def run(self, user, self.args):
        ''' !op nick '''
        rtrn = 'MODE ' + user + ' +o ' + args[1]
        return rtrn

BBQ = BoatBangExecutor('pwny','op')