#!/usr/local/bin/python3.6
from gui import *
from ocObjects import *
from saves import *

# load objects from files into vars
load_ocObjects()

GUI = Window()

# save objects from vars into files
save_ocObjects()

# + create backups periodically