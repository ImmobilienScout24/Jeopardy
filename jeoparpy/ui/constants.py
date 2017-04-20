"""
constants.py

DESCRIPTION:
  Defines constants required by multiple ui modules and subpackages,
  and constants that reach external files required by ui modules (whose
  definitions do not belong in resmaps.py).


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
from os import path, listdir

from ..constants import ROOT_PATH
from ..util import get_first_textline, get_stripped_nonempty_file_lines
from ..config import DRIVE

file = open(path.join(ROOT_PATH, 'jeoparpy', 'dir.txt'), 'r')
directory = file.readline()

if DRIVE == False:
    _rulesPath = path.join(ROOT_PATH, 'games', directory, 'rules.txt')
    _subPath = path.join(ROOT_PATH, 'games', directory, 'subtitle.txt')
else:
    DEVICE = listdir('/media')[0]
    _rulesPath = path.join('/media', DEVICE, 'games', directory, 'rules.txt')
    _subPath = path.join('/media', DEVICE, 'games', directory, 'subtitle.txt')

# our grey background
JEOP_BLUE = (242, 242, 242) # RGB color
SUBTITLE = 'Scout24 Hackdays - Pi Edition'
RULES = get_stripped_nonempty_file_lines(_rulesPath)
