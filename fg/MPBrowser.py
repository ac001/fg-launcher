# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui, QtWebKit

class MPBrowser(QtGui.QWidget):

	def __init__(self,  parent, main):
		QtGui.QWidget.__init__(self, parent)

		self.main = main
		self.url = QtCore.QUrl("http://mpmap02.flightgear.org/")

		mainLayout = QtGui.QVBoxLayout(self)
		self.setLayout(mainLayout)

		toolbar = QtGui.QToolBar(self)
		mainLayout.addWidget(toolbar)

		self.comboSelectServer = QtGui.QComboBox(self)
		toolbar.addWidget(self.comboSelectServer)

		self.webView = QtWebKit.QWebView(self)
		mainLayout.addWidget(self.webView, 20)
		self.webView.load(self.url)
		self.webView.show()
		
