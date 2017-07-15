#!/usr/local/bin/python3.6
import gui
import saves

for file in ['actions.txt', 'events.txt', 'inbox.txt', 'projects.txt', 'tags.txt']:
    saves.file_to_list(file)

win = gui.Window()

# + create backups periodically
