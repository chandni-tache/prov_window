#from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['pyHook'], excludes = [])

import sys
import os

from cx_Freeze import setup, Executable
#from PySide import QtXml

base = 'Win32GUI' if sys.platform=='win32' else None

options = {
    'build_exe': {
        'includes': ['atexit'],
		'include_files':['C:\Python34\Lib\site-packages\pyHook\_cpyHook.pyd']
    }
}

build_exe_options = {
    'includes': ['atexit'],
    'packages': ['PySide.QtXml','pyHook']
    }


setup(name='ProvLock',
      version = '0.10',
      description = 'First Release',
      options = dict(build_exe = buildOptions),
      executables = [
    Executable('testForm.py',shortcutName="ProvLock",
            shortcutDir="DesktopFolder")
])
'''
import sys
from cx_Freeze import setup, Executable
from PySide import *

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(name = 'spamandeggs',
      version = '0.0.1',
      executables = [Executable('testForm.py', base=base)],
      options = {'build_exe': {'includes': ['atexit']}})

'''
'''
from cx_Freeze import setup, Executable

# dependencies
build_exe_options = {
    "packages": ["os", "sys", "glob", "simplejson", "re", "atexit", "PySide.QtCore", "PySide.QtGui", "PySide.QtXml"],
    "include_files": [("./example/Ui/MainWindow.ui", "Ui/MainWindow.ui"),
                      ("./example/Ui/ExampleWidget.ui", "Ui/ExampleWidget.ui"),
                      ("./example/Ui/TestDialog.ui", "Ui/TestDialog.ui"),
                      ("./example/Resources/style.qss", "Ui/style.qss")], # this isn't necessary after all
    "excludes": ["Tkinter", "Tkconstants", "tcl"],
    "build_exe": "build",
    "icon": "./example/Resources/Icons/monitor.ico"
}

executable = [
    Executable("./bin/Example.py",
               base="Win32GUI",
               targetName="Example.exe",
               targetDir="build",
               copyDependentFiles=True)
]

setup(
    name="Example",
    version="0.1",
    description="Example", # Using the word "test" makes the exe to invoke the UAC in win7. WTH?
    author="Me",
    options={"build_exe": build_exe_options},
    executables=executable,
    requires=['PySide', 'cx_Freeze', 'simplejson']
)
'''
