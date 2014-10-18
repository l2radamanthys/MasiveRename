

import sys
from distutils.core import setup

kwargs = {}
if 'py2exe' in sys.argv:
    import py2exe
    kwargs = {
        'data_files': ['C:\\Python27\\tcl\\tcl8.5\\init.tcl'],
        'windows': [{
        #'console': [{
            'script': 'renamer.pyw',
            'description':'utilidad para renombrar masivamente diferentes archivos',
            #'icon_resources': [(0, 'icon.ico')],
        }],
        'zipfile': None,
        'options': { 'py2exe': {
            'dll_excludes': ['w9xpopen.exe'],
            'bundle_files': 1,
            'compressed': True,
            'optimize': 2,
        }},       
    }
setup(
    name='Renombrador Masivo',
    autor='Ricardo D. Quiroga - CeO2Soft',
    autor_email='ricardoquiroga.dev@gmail.com',
    **kwargs)
