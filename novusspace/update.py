#! Python / utf-8
# (C) 2020 Novus Space

import os
import shutil
import requests

__author__ = 'alex'
__version__ = '1.0'

def update(oldFile, newFileUrl, fileName, path, logs=False):
    if logs:
        print('starting update...')

    if not os.path.exists(os.path.abspath('tempDir')):
        os.mkdir('tempDir')
    else:
        pass

    path = '../' + path
    if os.path.exists(os.path.abspath(path + '/' + fileName)):
        os.remove(os.path.abspath(path + '/' + fileName))

    updateRequest = requests.get(newFileUrl, allow_redirects=True)
    tempFileName = 'tempDir/' + fileName
    open(tempFileName, 'wb').write(updateRequest.content)

    if os.path.exists(os.path.abspath(oldFile)):
        os.remove(os.path.abspath(oldFile))
    else:
        pass

    shutil.move(tempFileName, os.path.abspath(path))
    os.rmdir('tempDir')

    if logs:
        print('update complete')