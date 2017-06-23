#!/usr/local/bin/python\ 3.6
import datetime, json, os, random, sys
from pprint import pprint as pprint
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Gui options
app = QApplication(sys.argv)

class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		# Screen Settings
		self.screen_size = QSize()
		self.screen_size.setWidth(3600)
		self.screen_size.setHeight(1800)
		#-self.setWindowIcon(GtGui.QIcon('pythonlogo.png'))
		self.win = QDialog()
		self.win.setGeometry(0, 0, self.screen_size.width(), self.screen_size.height())
		self.win.setWindowTitle('OmniClone')	
		#-make size constant throughout all display sizes/formats		
		# Widget Instantiation+Arrangement
		# Main Frames
		self.gwindow = QGridLayout()
		self.actionList = QTableWidget(len(actions)+1, 6)
		self.calendar = QFrame(self.win)
		self.inspectorCal = QFrame(self.win)
		self.inspectorPro = QFrame(self.win)
		self.inspectorRem = QFrame(self.win)
		self.projectList = QTableWidget(len(projects)+1, 4)
		self.selector = QFrame(self.win)	
		self.toolbar = QFrame(self.win)
		# ActionList Table
		hheader = self.actionList.horizontalHeader()
		hheader.setResizeMode(0, QHeaderView.Stretch)
		hheader.setResizeMode(1, QHeaderView.Fixed)
		hheader.setResizeMode(2, QHeaderView.Fixed)
		hheader.setResizeMode(3, QHeaderView.Fixed)
		hheader.setResizeMode(4, QHeaderView.Fixed)
		self.actionList.setHorizontalHeaderLabels(['action name', 'project', 'deferred', 'eT', 'due', 'c'])
		self.actionList.setColumnWidth(1, 350)
		self.actionList.setColumnWidth(2, 200)
		self.actionList.setColumnWidth(3, 75)
		self.actionList.setColumnWidth(4, 200)
		self.actionList.setColumnWidth(5, 50)
		vheader = self.actionList.verticalHeader()
		vheader.setVisible(False)
		# InspectorCal
		
		# InspectorPro

		# InspectorRem
		self.lInspector1 = QLabel(self.inspectorRem)
		self.lInspector1.setText('None')
		# ProjectList Table
		hheader = self.projectList.horizontalHeader()	
		hheader.setResizeMode(0, QHeaderView.Stretch)
		hheader.setResizeMode(1, QHeaderView.Fixed)
		hheader.setResizeMode(2, QHeaderView.Fixed)
		hheader.setResizeMode(3, QHeaderView.Fixed)
		self.projectList.setHorizontalHeaderLabels(['project name', 'ds', 'od', 's'])
		self.projectList.setColumnWidth(1, 50)
		self.projectList.setColumnWidth(2, 50)
		self.projectList.setColumnWidth(3, 75)
		vheader = self.projectList.verticalHeader()
		vheader.setVisible(False)
		# Button Instantiation
		self.bCalendar = QPushButton(self.selector)
		self.bFlagged = QPushButton(self.selector)
		self.bForecast = QPushButton(self.selector)
		self.bInbox = QPushButton(self.selector)
		self.bProjects = QPushButton(self.selector)
		self.bReview = QPushButton(self.selector)
		self.bTags = QPushButton(self.selector)
		# Button Connections
		self.bCalendar.clicked.connect(self.bCalendarClicked)
		self.bInbox.clicked.connect(self.bInboxClicked)
		self.bProjects.clicked.connect(self.bProjectsClicked)
		self.bTags.clicked.connect(self.bTagsClicked)
		self.bFlagged.clicked.connect(self.bFlaggedClicked)
		self.bForecast.clicked.connect(self.bForecastClicked)
		self.bReview.clicked.connect(self.bReviewClicked)
		self.actionList.cellClicked.connect(self.tActionClicked)
		self.projectList.cellClicked.connect(self.tProjectClicked)
		self.actionList.cellDoubleClicked.connect(self.tActionDoubleClicked)
		self.projectList.cellDoubleClicked.connect(self.tProjectDoubleClicked)
		# Table Edit Connections
			
		# Display
		self.display('', '')
		self.display('projects', 'pro')
		sys.exit(app.exec_())
		# Saving to files
		save_to_file(actions, 'actions.txt')					# write to files
		save_to_file(inbox, 'inbox.txt')
		save_to_file(projects, 'projects.txt')
		save_to_file(tags, 'tags.txt')
		#-create backups periodically

	def display(self, mode, inspector):
		# Widget Stylesheets
		bc = '#c5c9c7'
		self.actionList.setStyleSheet('background-color : ' + bc)
		self.calendar.setStyleSheet('background-color : ' + bc)
		self.inspectorCal.setStyleSheet('background-color : ' + bc)
		self.inspectorRem.setStyleSheet('background-color : ' + bc)
		self.projectList.setStyleSheet('background-color : ' + bc)
		self.selector.setStyleSheet('background-color : ' + bc)
		self.toolbar.setStyleSheet('background-color : ' + bc)
		for w in [self.actionList, self.calendar, self.inspectorCal, self.inspectorRem, self.projectList, self.selector, self.toolbar]:
			w.setLineWidth(3)

		# Button Styles
		self.Buttons = [self.bInbox, self.bProjects, self.bTags, self.bFlagged, self.bForecast, self.bCalendar, self.bReview]
		self.selectorWidth = self.selector.frameGeometry().width()
		self.selectorHeight = self.selector.frameGeometry().height()
		i = 0
		for b in self.Buttons:
			b.resize(self.selectorWidth, self.selectorWidth)
			b.setText(['inbox', 'projects', 'tags', 'flagged', 'forecast', 'calendar', 'review'][i])
			b.move(0, (self.selectorWidth)*i)
			i += 1	
		# Displaying main section
		self.gwindow.addWidget(self.toolbar, 0, 0, 1, 34)
		self.gwindow.addWidget(self.selector, 2, 0, 18, 2)
		if mode == 'calendar':
			self.gwindow.addWidget(self.calendar, 2, 2, 18, 25)
			self.gwindow.addWidget(self.inspectorCal, 2, 27, 18, 7)
		elif mode in ['inbox', 'flagged', 'forecast', 'projects', 'review', 'tags']:
			self.gwindow.addWidget(self.projectList, 2, 2, 18, 8)
			self.gwindow.addWidget(self.actionList, 2, 10, 18, 17)
			self.gwindow.addWidget(self.inspectorRem, 2, 27, 18, 7)
			if mode == 'inbox':
				pass
			elif mode == 'forecast':
				pass
			elif mode == 'projects':
				i = 0
				for p in projects:
					while len(actions) > self.actionList.rowCount():
						self.actionList.insertRow(self.actionList.rowCount())
					# Display Project Title+Attributes
					tTitle = QTableWidgetItem()
					tTitle.setText(p.title)
					self.projectList.setItem(i, 0, tTitle)
					tDueSoon = QTableWidgetItem()
					#-implement due soon count
					tDueSoon.setText('')
					self.projectList.setItem(i, 2, tDueSoon)
					tOverDue = QTableWidgetItem()
					#-implement over due count
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
					#tTitle = QTableWidgetItem()
					#tTitle.setText(a.title)
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
			elif mode == 'review':
				pass
			elif mode == 'tags':
				pass
			# Display Object Attributes in Inspector
			if inspector == 'pro':
				pass
			elif inspector == 'cal':
				pass
			elif inspector == 'rem':
				pass
			else:
				print('Error 1')

		self.win.setLayout(self.gwindow)
		self.win.show()

	'''self.BoxSelector = QVBoxLayout()
	self.BoxSelector.addWidget(self.bInbox)
	self.BoxSelector.addWidget(self.bProjects)
	self.BoxSelector.addWidget(self.bTags)
	self.BoxSelector.addWidget(self.bFlagged)
	self.BoxSelector.addWidget(self.bReview)
	self.selector.setLayout(self.BoxSelector)
	self.vbox = QVBoxLayout()
	self.hbox = QHBoxLayout()
	self.vbox.addWidget(self.toolbar)
	self.vbox.addWidget(self.main)
	self.hbox.addWidget(self.selector)
	self.hbox.addWidget(self.project_list)
	self.hbox.addWidget(self.action_list)
	self.hbox.addWidget(self.inspector)
	self.toolbar.resize(self.getSize(self.toolbar)[0], 20)
	self.main.resize(self.getSize(self.main)[0], self.window_height - self.getSize(self.toolbar)[1])
	self.win.setLayout(self.vbox)
	self.main.setLayout(self.hbox)'''

	def bCalendarClicked(self):
		self.display('calendar', 'cal')

	def bInboxClicked(self):
		self.display('inbox' 'pro')

	def bFlaggedClicked(self):
		self.display('flagged', 'pro')

	def bForecastClicked(self):
		self.display('forecast', 'pro')

	def bProjectsClicked(self):
		self.display('projects', 'pro')

	def bReviewClicked(self):
		self.display('review', 'pro')

	def bTagsClicked(self):
		self.display('tags', 'pro')

	def tActionClicked(self):
		#-show action inspector
		self.display('projects', 'rem')

	def tActionDoubleClicked(self):	
		#print(self.actionList.currentRow())
		p = projects[self.projectList.currentRow()]
		if self.actionList.currentRow() == self.actionList.rowCount()-1:
			newAction = Action(p)
			actions.append(newAction)
			self.display('projects', 'rem')
		else:
			None

	def tProjectClicked(self):
		pass
		#-show project in actionList
		#-show project inspector
		self.display('projects', 'pro')

	def tProjectDoubleClicked(self):
		if self.projectList.currentRow() == self.projectList.rowCount()-1:
			newProject = Project()
			projects.append(newProject)
			self.display('projects', 'pro')
		else:
			None

	def projectCellChanged(self):
		print('cell changed!')
		#projects[self.projectList.currentRow] = self.projectList.currentItem().text()
		self.display('projects', 'rem')

class Project():
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
		#-add capability for on hold, active, paused and dropped projects
		#-repeat settings
		#-review settings
		#-initialize displayNr (append as last item in displayed list)

class Action(Project):
	def __init__(self, project):
		super(Action, self).__init__()
		# actions without projects have inbox as their project
		self.project = project

def save_to_file(list, PATH):
	f = open(PATH, 'w')
	if PATH in ['actions.txt', 'inbox.txt', 'projects.txt']:
		for item in list:
			json_str = json.dumps(item.__dict__)			# convert data to encoded string
			f.write(json_str + '\n')				# write encoded string to .txt
	elif PATH in ['tags.txt']:
		for item in list:
			f.write(item + '\n')
	f.close()

def load_from_file(PATH):
	list = []
	f = open(PATH, 'r')
	if PATH in ['actions.txt', 'inbox.txt', 'projects.txt']:
		for line in f.readlines():			
			list.append(json.loads(line[0:-1]))			# load json from file into var
	elif PATH in ['tags.txt']:
		for line in f.readlines():
			list.append(line[0:-1])
	f.close()
	return list
	
actions = load_from_file('actions.txt')					# load contents into variables
inbox = load_from_file('inbox.txt')
projects = load_from_file('projects.txt')
tags = load_from_file('tags.txt')


inbox = Project()
inbox.title = 'inbox'
p = Project()
p.title = 'peter lustig'
projects.append(inbox)
projects.append(p)

a = Action('peter lustig')
a.title = 'Die Penner müssen essen,'
b = Action('peter lustig')
b.title = 'doch sie haben kein essen'
c = Action('peter lustig')
c.title = 'darum sterben sie!'
d = Action('peter lustig')
d.title = 'lol'
e = Action('peter lustig') 
e.title = 'Aiman Abdallah knetet meine Eier'
f = Action('peter lustig')
f.title = 'darum kochen sie!'
g = Action('peter lustig')
g.title = 'und das ist eklig!'
h = Action('peter lustig')
h.title = 'Mehl, Salz und Ei'
i = Action('peter lustig')
i.title = 'Mehl, Salz und EI!'
j = Action('peter lustig')
j.title = 'Arbeit macht frei.'
k = Action('peter lustig')
k.title = 'Sieg'
l = Action('peter lustig')
l.title = 'Heil'
for i in [a, b, c, d, e, f, g, h, i, j, k, l]:
	actions.append(i)

GUI = Window()
