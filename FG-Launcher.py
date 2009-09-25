#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from fg.Settings import Settings
from fg.MPBrowser import MPBrowser

class FG_Launcher(QtGui.QMainWindow):
	class app:
		name = 'FlightGear Launcher.py'
		version = '0.1'
		copyright = 'Peter "mash" Morgan - ac001 [at] daffodil [dot] uk [dot] com'
		description = 'A front end for FlightGear written in python - snakes for transit'

	def __init__(self,  parent=None):
		QtGui.QMainWindow.__init__(self, parent)

		self.setMinimumWidth(600)
		self.setMinimumHeight(600)
		self.setWindowTitle( "%s - %s" % (self.app.name, self.app.version) )

		### Main Middle tabs
		self.mainTabWidget = QtGui.QTabWidget()
		self.setCentralWidget(self.mainTabWidget)
		self.tabs = {}
		
		## Add the Multiplayer Map Tab
		self.tabs['mp'] = MPBrowser(self, self)
		self.mainTabWidget.addTab(self.tabs['mp'], "Multiplayer Map")
		#self.tree = QtGui.QTreeView(self)
		


if __name__ == '__main__':

	#styleSheetString = open('style/cockpit.txt').read()
	#print styleSheetString
	app = QtGui.QApplication(sys.argv)


	mainWindow =  FG_Launcher()
	mainWindow.show()

	sys.exit(app.exec_())