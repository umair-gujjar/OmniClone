class Project():
    def __init__(self):
        self.comment        = ''
        self.completed      = False
        self.dateAdded      = ''
        self.dateChanged    = ''
        self.deferUntil     = ''
        self.displayIndex   = 0
        self.due            = ''
        self.estTime        = ''
        self.flagged        = False
        self.status         = ''
        self.tags           = []
        self.title          = ''

class Action():
    def __init__(self):
        self.comment        = ''
        self.completed      = False
        self.dateAdded      = ''
        self.dateChanged    = ''
        self.deferUntil     = ''
        self.displayIndex   = 0
        self.due            = ''
        self.estTime        = ''
        self.flagged        = False
        self.project        = ''
        self.status         = ''
        self.tags           = []
        self.title          = ''


class Event():
    def __init__(self):
        self.comment        = ''
        self.dateStart      = ''
        self.dateEnd        = ''
        self.project        = ''
        self.tags           = []
        self.title          = ''
