#******************************************************************************
# setup.py, provides a distutils script for use with cx_Freeze
#
# Creates a standalone windows executable
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application
#
# TreeLine, an information storage program
# Copyright (C) 2015, Douglas W. Bell
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License, either Version 2 or any later
# version.  This program is distributed in the hope that it will be useful,
# but WITTHOUT ANY WARRANTY.  See the included LICENSE file for details.
#******************************************************************************

import sys
from cx_Freeze import setup, Executable
from gmedit import __version__

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

extraFiles =  [('../doc', 'doc'), ('../icons', 'icons'),
               ('../samples', 'samples'), ('../source', 'source'),
               ('../templates', 'templates'), ('qdarkstyle/style.qss', 'qdarkstyle/style.qss'),
               ('../translations', 'translations'), ('../win', '.')]

setup(name = 'GmEdit',
      version = __version__,
      description = 'GM Editing Tool',
      options = {'build_exe': {'includes': ['atexit', 'urllib'],
                               'include_files': extraFiles,
                               'excludes': ['*.pyc'],
                               'icon': '../win/gm_icon.ico',
                               'include_msvcr': True,
                               'build_exe': '../../GmEdit-0.1'}},
      executables = [Executable('gmedit.py', base=base)])
