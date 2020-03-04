#!/usr/bin/python3

'''
    Setup script for Jupyter Tray.
'''

import os
print("Set up Jupyter tray for you.")

try:
    pathToJupyter = input("The full path of jupyter: ").strip()
    pathForPythonScript = input("Prefix for the python script [~/.local/bin]:").strip().rstrip('/')
    pathForDesktopEntry = input("Prefix for the desktop entry [~/.local/share/applications]:").strip().rstrip('/')
    pathForIcon = input("Prefix for the application " + \
            "icons [~/.local/share/icons/hicolor/64x64/apps]:").strip().rstrip('/')
    if not pathToJupyter:
        raise RuntimeError("You may try to use 'which jupyter' to find path to jupyter")
except:
    pass

if not pathForPythonScript:
    pathForPythonScript = '~/.local/bin'
if not pathForDesktopEntry:
    pathForDesktopEntry = '~/.local/share/applications'
if not pathForIcon:
    pathForIcon = '~/.local/share/icons/hicolor/64x64/apps'

os.system("cp -i jupyter.png " + \
        pathForIcon + '/jupyter.png')

os.system('sed  "s|JUPYTER|' + pathToJupyter + '|g" jupyter-tray.py.model > jupyter-tray.py')
os.system('chmod +x jupyter-tray.py && cp -i jupyter-tray.py ' + \
        pathForPythonScript + '/jupyter-tray.py')

os.system('sed  "s|JUPYTER|'+ pathForPythonScript + \
        '/jupyter-tray.py|g" jupyter-tray.desktop.model > jupyter-tray.desktop')
os.system('cp -i jupyter-tray.desktop ' + \
        pathForDesktopEntry + '/jupyter-tray.desktop')
