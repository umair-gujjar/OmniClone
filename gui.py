import saves
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


app = QApplication(sys.argv)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.screen_size = QSize()
        self.win = QDialog()
        self.gwindow = QGridLayout()

        self.toolbar = QFrame(self.win)
        self.selector = QFrame(self.win)
        self.projectList = QTableWidget(len(saves.projects) + 1, 4)
        self.projectInspector = QFrame(self.win)
        self.actionList = QTableWidget(len(saves.actions) + 1, 6)
        self.actionInspector = QFrame(self.win)
        self.calendar = QFrame(self.win)
        self.calendarInspector = QFrame(self.win)

        self.widgets = [self.toolbar,
                        self.selector,
                        self.projectList,
                        self.projectInspector,
                        self.actionList,
                        self.actionInspector,
                        self.calendar,
                        self.calendarInspector,
                        ]

        self.bCalendar = QPushButton(self.selector)
        self.bFlagged = QPushButton(self.selector)
        self.bForecast = QPushButton(self.selector)
        self.bInbox = QPushButton(self.selector)
        self.bProjects = QPushButton(self.selector)
        self.bReview = QPushButton(self.selector)
        self.bTags = QPushButton(self.selector)

        self.buttons = [self.bCalendar,
                        self.bFlagged,
                        self.bForecast,
                        self.bInbox,
                        self.bProjects,
                        self.bReview,
                        self.bTags
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
        self.createButtons()
        self.connectButtons()
        # + open up where you left off ( + save display args when quitting)
        self.display(mainFrameMode='projects', inspectorMode='projects')
        self.display(mainFrameMode='projects', inspectorMode='projects')
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

        self.projectList.setColumnWidth(1, 50)
        self.projectList.setColumnWidth(2, 50)
        self.projectList.setColumnWidth(3, 75)

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

        self.actionList.setHorizontalHeaderLabels(['action name', 'project', 'deferred', 'eT', 'due', 'c'])

        self.actionList.setColumnWidth(1, int(self.actionList.frameGeometry().width() / 875 * 350))
        self.actionList.setColumnWidth(2, int(self.actionList.frameGeometry().width() / 875 * 160))
        self.actionList.setColumnWidth(3, int(self.actionList.frameGeometry().width() / 875 * 75))
        self.actionList.setColumnWidth(4, int(self.actionList.frameGeometry().width() / 875 * 160))
        self.actionList.setColumnWidth(5, int(self.actionList.frameGeometry().width() / 875 * 50))

    def createFrameActionInspector(self):
        # + add action information
        pass

    def createFrameCalendar(self):
        # + add calendar
        pass

    def createFrameCalendarInspector(self):
        # + add CalendarEvent information
        pass

    def createButtons(self):
        pass

    def connectButtons(self):
        # + connect buttons to corresponding functions
        # + also connect table edit events to corresponding functions (e.g. when editing action dueDate)
        pass

    def display(self, mainFrameMode, inspectorMode):
        for w in self.widgets:
            w.setStyleSheet('background-color : ' + self.backgroundColor)

        i = 0
        for b in self.buttons:
            b.resize(self.selector.frameGeometry().width(), self.selector.frameGeometry().width())
            b.setText(['inbox', 'projects', 'tags', 'flagged', 'forecast', 'calendar', 'review'][i])
            b.move(0, (self.selector.frameGeometry().width()) * i)
            i += 1
        self.gwindow.addWidget(self.toolbar, 0, 0, 1, 34)
        self.gwindow.addWidget(self.selector, 2, 0, 18, 2)

        if mainFrameMode in ['calendar', 'inbox']:
            if mainFrameMode in ['calendar']:
                self.gwindow.addWidget(self.calendar, 2, 2, 18, 25)
                self.gwindow.addWidget(self.inspectorCal, 2, 27, 18, 7)
                # + add calendar grid
                # + add full calendar functionality

            elif mainFrameMode in ['inbox']:
                # + display inbox items
                pass

        elif mainFrameMode in ['flagged', 'forecast', 'projects', 'review', 'tags']:
            self.gwindow.addWidget(self.projectList, 2, 2, 18, 8)
            self.gwindow.addWidget(self.actionList, 2, 10, 18, 17)
            self.gwindow.addWidget(self.actionInspector, 2, 27, 18, 7)

            if mainFrameMode in ['forecast']:
                # + show small calendar view in projectList
                # + display nextUp items
                pass

            elif mainFrameMode == 'projects':
                while len(saves.projects) > self.projectList.rowCount():
                    self.projectList.insertRow(self.actionList.rowCount())
                while len(saves.actions) > self.actionList.rowCount():
                    self.actionList.insertRow(self.actionList.rowCount())
                """
                i = 0
                for p in sorted_projects('title'):
                    tTitle = QTableWidgetItem()
                    tTitle.setText(p.title)
                    self.projectList.setItem(i, 0, tTitle)
                    i += 1
                """
                """
                i = 0
                for p in projects:
                    while len(actions) > self.actionList.rowCount():
                        self.actionList.insertRow(self.actionList.rowCount())

                    # Display Project Title+Attributes
                    tTitle = QTableWidgetItem()
                    tTitle.setText(p.title)
                    self.projectList.setItem(i, 0, tTitle)
                    tDueSoon = QTableWidgetItem()
                    # -implement due soon count
                    tDueSoon.setText('')
                    self.projectList.setItem(i, 2, tDueSoon)
                    tOverDue = QTableWidgetItem()
                    # -implement over due count
                    tOverDue.setText('')
                    self.projectList.setItem(i, 3, tOverDue)
                    tStatus = QTableWidgetItem()
                    if p.status == 'active':
                        tStatus.setText('ACT')
                    elif p.status == 'on hold':
                        tStatus.setText('ONH')
                    elif p.status == 'dropped':
                        tStatus.setText('DRO')
                    elif p.status == 'completed':
                        tStatus.setText('COM')
                    self.projectList.setItem(i, 3, tStatus)
                    i += 1

                i = 0
                for a in actions:
                    while len(actions) > self.actionList.rowCount():
                        self.actionList.insertRow(self.actionList.rowCount())
                    # Display Action Title+Attributes
                    # tTitle = QTableWidgetItem()
                    # tTitle.setText(a.title)
                    self.actionList.setItem(i, 0, QTableWidgetItem(a.title))
                    tProject = QTableWidgetItem()
                    tProject.setText(a.project)
                    self.actionList.setItem(i, 1, tProject)
                    tDeferUntil = QTableWidgetItem()
                    tDeferUntil.setText(a.deferUntil)
                    self.actionList.setItem(i, 2, tDeferUntil)
                    tDue = QTableWidgetItem()
                    tDue.setText(a.due)
                    self.actionList.setItem(i, 3, tDue)
                    tEstTime = QTableWidgetItem()
                    tEstTime.setText(a.estTime)
                    self.actionList.setItem(i, 4, tEstTime)
                    tCompleted = QTableWidgetItem()
                    if a.completed is True:
                        tCompleted.setText('x')
                    else:
                        tCompleted.setText('o')
                    self.actionList.setItem(i, 5, tCompleted)
                    i += 1"""

            elif mainFrameMode in ['review']:
                # + display projects to be reviewed in projectList
                # + display actions in project
                pass

            elif mainFrameMode in ['tags']:
                # display tags in projectList
                # display actions per tag
                pass

                # Display Object Attributes in Inspector
            if inspectorMode in ['projects']:
                # + display project info
                pass

            elif inspectorMode in ['calendar']:
                # + display event info
                pass

            elif inspectorMode in ['actions']:
                # + display action info
                pass

            else:
                print('Error: Wrong inspectorMode passed to display()')

        # + save everytime display is called?
        self.win.show()

        # + buttons methods
