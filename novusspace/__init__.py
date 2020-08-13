#! Python
# (C) 2020 Novus Space

import os

''' Main class '''
class novusInit:
    def __init__(self):
        self.dependencies = 1
        self.directory = 'novusspace'
        self.checkDependencies()

    def checkDependencies(self):
        os.chdir(self.directory)
        if os.path.isfile('credentials/infos.py') and os.path.isfile('var.py') and os.path.isfile('update.py') and os.path.isfile('setup.py'):
            pass
        else:
            exit('[ERROR] missing dependency(ies)')

        try:
            import shutil
            import requests
        except ImportError:
            exit('[ERROR] Missing module(s)')


''' Initialsation of novusspace module'''
novusInit()
