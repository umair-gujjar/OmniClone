class Project():
    def __init__(self):
        self.comment        = ''
        self.date_added     = ''
        self.date_changed   = ''
        self.defer_until    = ''
        self.display_index  = 0
        self.due            = ''
        self.est_time       = ''
        self.flagged        = False
        self.status         = 1
        self.tags           = []
        self.title          = ''


class Action():
    def __init__(self):
        self.comment        = ''
        self.date_added     = ''
        self.date_changed   = ''
        self.defer_until    = ''
        self.display_index  = 0
        self.due            = ''
        self.est_time       = ''
        self.flagged        = False
        self.project        = ''
        self.status         = 1
        self.tags           = []
        self.title          = ''


class Event():
    def __init__(self):
        self.comment        = ''
        self.date_start     = ''
        self.date_end       = ''
        self.project        = ''
        self.tags           = []
        self.title          = ''
