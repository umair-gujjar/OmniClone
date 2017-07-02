import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ocObjects import *
from saves import *


app = QApplication(sys.argv)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.createWindow()
        self.createFrames()
        self.createButtons()
        self.connectButtons()
        # + save display args -> open up where you left off
        self.display(mainFrameMode='projects', inspectorMode='projects')
        self.display(mainFrameMode = 'projects', inspectorMode = 'projects')

        sys.exit(app.exec_())

    def createWindow(self):
        # + make size consistent throughout all display sizes/formats
        self.screen_size = QSize()
        self.screen_size.setWidth(3600)
        self.screen_size.setHeight(1800)

        self.setWindowIcon(QIcon('neptune.jpg'))

        self.win = QDialog()
        self.win.setGeometry(0, 0, self.screen_size.width(), self.screen_size.height())
        self.win.setWindowTitle('OmniClone')

    def createFrames(self):
        self.createFrameProjectList()
        self.createFrameActionList()
        self.createFrameCalendar()
        self.createFrameProjectInspector()
        self.createFrameActionInspector()
        self.createFrameCalendarInspector()
        self.createFrameSelector()
        self.createFrameToolbar()

        self.widgets = [self.projectList, self.actionList, self.calendar, self.projectInspector, self.actionInspector, self.calendarInspector, self.selector, self.toolbar]

    def createFrameProjectList(self):
        self.projectList = QTableWidget(len(projects) + 1, 4)

        hheader = self.projectList.horizontalHeader()
        vheader = self.projectList.verticalHeader()
        vheader.setVisible(False)

        hheader.setResizeMode(0, QHeaderView.Stretch)
        hheader.setResizeMode(1, QHeaderView.Fixed)
        hheader.setResizeMode(2, QHeaderView.Fixed)
        hheader.setResizeMode(3, QHeaderView.Fixed)

        self.projectList.setHorizontalHeaderLabels(['project name', 'ds', 'od', 's'])
        self.projectList.setColumnWidth(1, 50)
        self.projectList.setColumnWidth(2, 50)
        self.projectList.setColumnWidth(3, 75)

        # + add dueSoon, overDue, status labels -> create function to determine these values


    def createFrameActionList(self):
        self.actionList = QTableWidget(len(actions) + 1, 6)

        hheader = self.actionList.horizontalHeader()
        vheader = self.actionList.verticalHeader()
        vheader.setVisible(False)

        hheader.setResizeMode(0, QHeaderView.Stretch)
        hheader.setResizeMode(1, QHeaderView.Fixed)
        hheader.setResizeMode(2, QHeaderView.Fixed)
        hheader.setResizeMode(3, QHeaderView.Fixed)
        hheader.setResizeMode(4, QHeaderView.Fixed)

        self.actionList.setHorizontalHeaderLabels(['action name', 'project', 'defer', 'eT', 'due', 'c'])

        self.actionList.setColumnWidth(1, int(self.actionList.frameGeometry().width()/875*350))
        self.actionList.setColumnWidth(2, int(self.actionList.frameGeometry().width()/875*200))
        self.actionList.setColumnWidth(3, int(self.actionList.frameGeometry().width()/875*75))
        self.actionList.setColumnWidth(4, int(self.actionList.frameGeometry().width()/875*200))
        self.actionList.setColumnWidth(5, int(self.actionList.frameGeometry().width()/875*50))

    def createFrameCalendar(self):
        self.calendar = QFrame(self.win)
        # + add calendar

    def createFrameProjectInspector(self):
        self.projectInspector = QFrame(self.win)
        # + add project information

    def createFrameActionInspector(self):
        self.actionInspector = QFrame(self.win)
        # + add action information

    def createFrameCalendarInspector(self):
        self.calendarInspector = QFrame(self.win)
        # + add CalendarEvent information

    def createFrameSelector(self):
        self.selector = QFrame(self.win)

    def createFrameToolbar(self):
        self.toolbar = QFrame(self.win)

    def createButtons(self):
        self.bCalendar = QPushButton(self.selector)
        self.bFlagged = QPushButton(self.selector)
        self.bForecast = QPushButton(self.selector)
        self.bInbox = QPushButton(self.selector)
        self.bProjects = QPushButton(self.selector)
        self.bReview = QPushButton(self.selector)
        self.bTags = QPushButton(self.selector)

        self.buttons = [self.bCalendar, self.bFlagged, self.bForecast, self.bInbox, self.bProjects, self.bReview, self.bTags]

    def connectButtons(self):
        pass
        # + connect buttons to corresponding functions

        # + also connect table edit events to corresponding functions (e.g. when editing action dueDate)

    def display(self, mainFrameMode, inspectorMode):
        backgroundColor = '#c5c9c7'
        self.projectList.setStyleSheet('background-color : ' + backgroundColor)
        self.actionList.setStyleSheet('background-color : ' + backgroundColor)
        self.calendar.setStyleSheet('background-color : ' + backgroundColor)
        self.projectInspector.setStyleSheet('background-color : ' + backgroundColor)
        self.actionInspector.setStyleSheet('background-color : ' + backgroundColor)
        self.calendarInspector.setStyleSheet('background-color : ' + backgroundColor)
        self.selector.setStyleSheet('background-color : ' + backgroundColor)
        self.toolbar.setStyleSheet('background-color : ' + backgroundColor)

        for widget in self.widgets:
            widget.setLineWidth(3)

        i = 0
        for b in self.buttons:
            b.resize(self.selector.frameGeometry().width(), self.selector.frameGeometry().width())
            b.setText(['inbox', 'projects', 'tags', 'flagged', 'forecast', 'calendar', 'review'][i])
            b.move(0, (self.selector.frameGeometry().width()) * i)
            i += 1

        self.gwindow = QGridLayout()
        self.gwindow.addWidget(self.toolbar, 0, 0, 1, 34)
        self.gwindow.addWidget(self.selector, 2, 0, 18, 2)

        if mainFrameMode == 'calendar':
            self.gwindow.addWidget(self.calendar, 2, 2, 18, 25)
            self.gwindow.addWidget(self.inspectorCal, 2, 27, 18, 7)

            # + add calendar grid
            # + add full calendar functionality

        elif mainFrameMode in ['inbox', 'flagged', 'forecast', 'projects', 'review', 'tags']:
            self.gwindow.addWidget(self.projectList, 2, 2, 18, 8)
            self.gwindow.addWidget(self.actionList, 2, 10, 18, 17)
            self.gwindow.addWidget(self.actionInspector, 2, 27, 18, 7)
            if mainFrameMode == 'inbox':
                # + projectList unnecessary? Maybe move remove projectList for inbox mode? (like in calendar mode)
                # + display inbox items
                pass
            elif mainFrameMode == 'forecast':
                # + show small calendar view in projectList
                # + display nextUp items
                pass
            elif mainFrameMode == 'projects':
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
                    i += 1

            elif mainFrameMode == 'review':
                # + display projects to be reviewed in projectList
                # + display actions in project
                pass

            elif mainFrameMode == 'tags':
                # display tags in projectList
                # display actions per tag
                pass

            # Display Object Attributes in Inspector
            if inspectorMode == 'projects':
                # + display project info
                pass

            elif inspectorMode == 'calendar':
                # + display event info
                pass

            elif inspectorMode == 'actions':
                # + display action info
                pass

            else:
                print('Error: Wrong inspectorMode passed to display()')

        self.win.setLayout(self.gwindow)
        self.win.show()

        # + save at every time display function is called?

    # Button methods:
