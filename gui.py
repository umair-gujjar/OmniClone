import saves
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


app = QApplication(sys.argv)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.screen_size        = QSize()
        self.win                = QDialog()
        self.gwindow            = QGridLayout()

        self.toolbar            = QFrame(self.win)
        self.selector           = QFrame(self.win)
        self.projectList        = QTableWidget(len(saves.projects) + 1, 4)
        self.projectInspector   = QFrame(self.win)
        self.actionList         = QTableWidget(len(saves.actions) + 1, 6)
        self.actionInspector    = QFrame(self.win)
        self.calendar           = QFrame(self.win)
        self.calendarInspector  = QFrame(self.win)

        self.widgets = [self.toolbar,
                        self.selector,
                        self.projectList,
                        self.projectInspector,
                        self.actionList,
                        self.actionInspector,
                        self.calendar,
                        self.calendarInspector,
                        ]

        self.bCalendar  = QPushButton(self.selector)
        self.bFlagged   = QPushButton(self.selector)
        self.bForecast  = QPushButton(self.selector)
        self.bInbox     = QPushButton(self.selector)
        self.bProjects  = QPushButton(self.selector)
        self.bReview    = QPushButton(self.selector)
        self.bTags      = QPushButton(self.selector)
        self.bOther     = QPushButton(self.selector)

        self.selector_buttons = [self.bCalendar,
                                 self.bFlagged,
                                 self.bForecast,
                                 self.bInbox,
                                 self.bProjects,
                                 self.bReview,
                                 self.bTags,
                                 self.bOther
                                 ]

        self.backgroundColor = '#c5c9c7'
        self.phheader = self.projectList.horizontalHeader()
        self.pvheader = self.projectList.verticalHeader()
        self.ahheader = self.actionList.horizontalHeader()
        self.avheader = self.actionList.verticalHeader()

        self.createWindow()
        self.createFrameToolbar()
        self.createFrameSelector()
        self.createFrameProjectList()
        self.createFrameProjectInspector()
        self.createFrameActionList()
        self.createFrameActionInspector()
        self.createFrameCalendar()
        self.createFrameCalendarInspector()
        self.connectButtons()
        # + open up where you left off ( + save display args when quitting)
        self.display('projects', 'projects')
        self.display('projects', 'projects')
        sys.exit(app.exec_())

    def createWindow(self):
        # + make size consistent throughout all display sizes/formats
        self.screen_size.setWidth(3600)
        self.screen_size.setHeight(1800)
        self.win.setGeometry(0, 0, self.screen_size.width(), self.screen_size.height())

        # + set window icon ( self.setWindowIcon(QIcon('neptune.jpg')) ?)

        self.win.setWindowTitle('OmniClone v0.1')
        self.win.setLayout(self.gwindow)

    def createFrameToolbar(self):
        # + add sorting options via button
        pass

    def createFrameSelector(self):
        pass

    def createFrameProjectList(self):
        self.pvheader.setVisible(False)

        self.phheader.setResizeMode(0, QHeaderView.Stretch)
        self.phheader.setResizeMode(1, QHeaderView.Fixed)
        self.phheader.setResizeMode(2, QHeaderView.Fixed)
        self.phheader.setResizeMode(3, QHeaderView.Fixed)

        self.projectList.setHorizontalHeaderLabels(['project name', 'ds', 'od', 's'])

        self.projectList.setColumnWidth(1, 30)
        self.projectList.setColumnWidth(2, 30)
        self.projectList.setColumnWidth(3, 22)

        # + add dueSoon, overDue, status labels -> create function to determine these values

    def createFrameProjectInspector(self):
        # + add project information
        pass

    def createFrameActionList(self):
        self.avheader.setVisible(False)

        self.ahheader.setResizeMode(0, QHeaderView.Stretch)
        self.ahheader.setResizeMode(1, QHeaderView.Fixed)
        self.ahheader.setResizeMode(2, QHeaderView.Fixed)
        self.ahheader.setResizeMode(3, QHeaderView.Fixed)
        self.ahheader.setResizeMode(4, QHeaderView.Fixed)

        self.actionList.setHorizontalHeaderLabels(['action name', 'project', 'defer', 'eT', 'due', 's'])

        self.actionList.setColumnWidth(1, int(self.actionList.frameGeometry().width() / 875 * 350))
        self.actionList.setColumnWidth(2, int(self.actionList.frameGeometry().width() / 875 * 150))
        self.actionList.setColumnWidth(3, int(self.actionList.frameGeometry().width() / 875 * 50))
        self.actionList.setColumnWidth(4, int(self.actionList.frameGeometry().width() / 875 * 150))
        self.actionList.setColumnWidth(5, int(self.actionList.frameGeometry().width() / 875 * 35))

    def createFrameActionInspector(self):
        # + add action information
        pass

    def createFrameCalendar(self):
        # + add calendar
        pass

    def createFrameCalendarInspector(self):
        # + add CalendarEvent information
        pass

    def connectButtons(self):
        # + connect buttons to corresponding functions
        # + also connect table edit events to corresponding functions (e.g. when editing action dueDate)
        
        # + maybe the following lambda values will have to be adjusted
        self.bCalendar.clicked.connect(lambda: self.display('calendar', 'calendar'))
        self.bFlagged.clicked.connect(lambda: self.display('flagged', 'actions'))
        self.bForecast.clicked.connect(lambda: self.display('forecast', 'actions'))
        self.bInbox.clicked.connect(lambda: self.display('inbox', 'actions'))
        self.bProjects.clicked.connect(lambda: self.display('projects', 'projects'))
        self.bReview.clicked.connect(lambda: self.display('review', 'actions'))
        self.bTags.clicked.connect(lambda: self.display('tags', 'actions'))
        self.bOther.clicked.connect(lambda: self.display('other', 'other'))
        
        # + if top row clicked -> change sorting_key_a & i & p (think about how to do display_index sorting correctly when having a project selected)

    def display(self, mainFrameMode, inspectorMode):
        for w in self.widgets:
            w.setStyleSheet('background-color : ' + self.backgroundColor)

        n = 0
        for b in self.selector_buttons:
            b.resize(self.selector.frameGeometry().width(), self.selector.frameGeometry().width())
            b.setText(['inbox', 'projects', 'tags', 'flagged', 'forecast', 'calendar', 'review', 'other'][n])
            b.move(0, (self.selector.frameGeometry().width()) * n)
            n += 1
        self.gwindow.addWidget(self.toolbar, 0, 0, 1, 34)
        self.gwindow.addWidget(self.selector, 2, 0, 18, 2)

        if mainFrameMode in ['calendar', 'inbox']:
            if mainFrameMode in ['calendar']:
                self.gwindow.addWidget(self.calendar, 2, 2, 18, 25)
                self.gwindow.addWidget(self.calendarInspector, 2, 27, 18, 7)
                # + add calendar grid
                # + add full calendar functionality

            elif mainFrameMode in ['inbox']:
                # + display inbox items
                pass

        elif mainFrameMode in ['flagged', 'forecast', 'projects', 'review', 'tags']:
            self.gwindow.addWidget(self.projectList, 2, 2, 18, 8)
            self.gwindow.addWidget(self.actionList, 2, 10, 18, 17)
            self.gwindow.addWidget(self.actionInspector, 2, 27, 18, 7)

            if mainFrameMode in ['flagged']:
                # + show project list with projects containing flagged items
                pass

            elif mainFrameMode in ['forecast']:
                # + show small calendar view in projectList
                # + display nextUp items
                pass

            elif mainFrameMode == 'projects':

                bool_project_selected       = False
                index_project_selected      = 0 # + get selected cell via event

                while len(saves.projects)   > self.projectList.rowCount():
                    self.projectList.insertRow(self.actionList.rowCount())

                while len(saves.actions)    > self.actionList.rowCount():
                    self.actionList.insertRow(self.actionList.rowCount())

                n = 0
                for p in saves.projects:
                    cell_due_soon           = QTableWidgetItem()
                    cell_over_due           = QTableWidgetItem()
                    cell_status             = QTableWidgetItem()
                    cell_title              = QTableWidgetItem()

                    cell_due_soon.setText(str(len(saves.due_soon)))
                    cell_over_due.setText(str(len(saves.over_due)))
                    if p.status             == 0:
                        cell_status.setText('√')
                    elif p.status           == 1:
                        cell_status.setText('X')
                    elif p.status           == 2:
                        cell_status.setText('H')
                    else:
                        print("ERROR: Invalid action status.")
                    cell_title.setText(p.title)

                    self.projectList.setItem(n, 1, cell_due_soon)
                    self.projectList.setItem(n, 2, cell_over_due)
                    self.projectList.setItem(n, 3, cell_status)
                    self.projectList.setItem(n, 0, cell_title)
                    n += 1

                if not bool_project_selected:
                    n                       = 0
                    for a in saves.actions:
                        cell_defer_until    = QTableWidgetItem()
                        cell_due            = QTableWidgetItem()
                        cell_est_time       = QTableWidgetItem()
                        cell_project        = QTableWidgetItem()
                        cell_status         = QTableWidgetItem()
                        cell_title          = QTableWidgetItem()

                        cell_defer_until.setText(a.defer_until)
                        cell_due.setText(a.due)
                        cell_est_time.setText(a.est_time)
                        cell_project.setText(a.project)
                        if a.status         == 0:
                            cell_status.setText('H')
                        elif a.status       == 1:
                            cell_status.setText('X')
                        elif a.status       == 2:
                            cell_status.setText('√')
                        else:
                            print("ERROR: Invalid action status.")
                        cell_title.setText(a.title)

                        self.actionList.setItem(n, 0, cell_title)
                        self.actionList.setItem(n, 1, cell_project)
                        self.actionList.setItem(n, 2, cell_defer_until)
                        self.actionList.setItem(n, 3, cell_est_time)
                        self.actionList.setItem(n, 4, cell_due)
                        self.actionList.setItem(n, 5, cell_status)
                        n += 1
                else:
                    n = 0
                    project_actions         = []
                    for a in saves.actions:
                        if a.project        == saves.sort_projects(saves.sorting_key_a)[index_project_selected]:
                            project_actions.append(a)

                    for a in project_actions:
                        cell_defer_until    = QTableWidgetItem()
                        cell_due            = QTableWidgetItem()
                        cell_est_time       = QTableWidgetItem()
                        cell_project        = QTableWidgetItem()
                        cell_status         = QTableWidgetItem()
                        cell_title          = QTableWidgetItem()

                        cell_defer_until.setText(a.defer_until)
                        cell_due.setText(a.due)
                        cell_est_time.setText(a.est_time)
                        cell_project.setText(a.project)
                        if a.status         == 0:
                            cell_status.setText('H')
                        elif a.status       == 1:
                            cell_status.setText('X')
                        elif a.status       == 2:
                            cell_status.setText('√')
                        else:
                            print("ERROR: Invalid action status.")
                        cell_title.setText(a.title)

                        self.actionList.setItem(n, 0, cell_title)
                        self.actionList.setItem(n, 1, cell_project)
                        self.actionList.setItem(n, 2, cell_defer_until)
                        self.actionList.setItem(n, 3, cell_est_time)
                        self.actionList.setItem(n, 4, cell_due)
                        self.actionList.setItem(n, 5, cell_status)
                        n += 1


            elif mainFrameMode in ['review']:
                # + display projects to be reviewed in projectList
                # + display actions in project
                pass

            elif mainFrameMode in ['tags']:
                # display tags in projectList
                # display actions per tag
                pass

            elif mainFrameMode in ['other']:
                # placeholder, for now
                pass

            else:
                print('ERROR: Invalid mainFrameMode passed to display(): ' + mainFrameMode)

            if inspectorMode in ['projects']:
                # + display project info
                pass

            elif inspectorMode in ['calendar']:
                # + display event info
                pass

            elif inspectorMode in ['actions']:
                # + display action info
                pass

            elif inspectorMode in ['other']:
                # placeholder, for now
                pass

            else:
                print('Error: Invalid inspectorMode passed to display(): ' + inspectorMode)

        # + save everytime display is called?
        self.win.show()

        # + define button methods
