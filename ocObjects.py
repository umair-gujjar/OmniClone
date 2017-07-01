#!/usr/local/bin/python3.6

actions = []
inbox = []
projects = []
tags = []
files = {'actions.txt': actions, 'inbox.txt': inbox, 'projects.txt': projects, 'tags.txt': tags}


class Project:
    def __init__(self):
        self.completed = False
        self.title = ''
        self.tags = []
        self.deferUntil = ''
        self.due = ''
        self.estTime = ''
        self.comment = ''
        self.flagged = False
        self.dateAdded = ''
        self.dateChanged = ''
        self.status = 'active'
        # + add capability for on hold, active, paused and dropped projects
        # + repeat settings
        # + review settings
        # + initialize displayNr (append as last item in displayed list)


class Action(Project):
    def __init__(self, project):
        super(Action, self).__init__()
        # actions without projects have inbox as their project
        self.project = project

# + add class CalendarEvent
