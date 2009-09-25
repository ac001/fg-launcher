# -*- coding: utf-8 -*-

from PyQt4 import QtCore

class Settings(QtCore.QObject):

	def __init__(self, parent):
		QtCore.QObject.__init__(self)

		self.settings = QtCore.QSettings("FG_Launcher.py", "FG_Launcher.py")


	#################################################
	## Proxy for QSettings class
	#################################################
	def value(self, ki):
		return self.settings.value( ki )

	def setValue(self, ki, valu ):
		return self.settings.setValue( ki, QtCore.QVariant(valu) )

	def remove(self, ki):
		self.settings.remove(ki)

	#################################################
	## Save Window Postion
	#################################################
	def save_window(self, windowName, window):
		self.settings.setValue( "%s/geometry" % windowName, QtCore.QVariant(window.saveGeometry()) )

	def restore_window(self, windowName, window):
		geo = self.settings.value( "%s/geometry" % windowName )
		window.restoreGeometry( geo.toByteArray() )


