#!/usr/bin/python3
#-*- coding: utf-8 -*-

# /!\ CHANTIER /!\


class BoatBangzExecutor:

    def __init__(self):
        self.loadedmodules = []

    def bangprobe(self, bang):
        # Cherche si le module est load
        if bang not in self.loadedmodules:
            # ~ search & loading in module land ~
            # chaque bang est dans un module du même nom
            # dans le sous dossier modules/*.py
            # ex : module/op.py
            mod = ''
            try:
                mod = __import__('modules/', bang,'.py')
                self.loadeddmodules.append(bang)
                self.loadedmodules.append(mod)
            except ImportError:
                print('debug : erreur d\'importation', mod)
        if mod:
            # le module est load
            self.exec_bang(self, self.bang, self.args)
            return 1
        else:
            return 0

    def exec_bang(self, mod, user, args):
        retour = getattr(mod, 'run',user)
        return retour


BBQ = BoatBangzExecutor()
BBQ.bangprobe('LocalMod')
fnc = BBQ.exec_bang(LocalMod,'pwny','niko')
ret = fnc(op,'pwy','niko')
print(ret)