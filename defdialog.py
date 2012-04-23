#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import * 
import sys, os
from ui_defdialog import Ui_DefDialog

class DefWindow ( QDialog , Ui_DefDialog):
	
	def_file = []
	settings = QSettings('settings.ini', QSettings.IniFormat)
	settings.setFallbacksEnabled(False)
	
	def __init__ ( self, parent = None ):
		QDialog.__init__( self, parent )
		self.ui = Ui_DefDialog()
		self.ui.setupUi( self )
		self.ui.pushApply.clicked.connect(self.saveConfig)
		self.show()
		for root, dirs, files in os.walk('./hotkeys'):
			for name in files:
			   filename = os.path.join(root, name)
			   self.ui.comboDef.addItem(os.path.basename(filename))
			   #self.def_file.append(filename)
		if self.ui.comboDef.findText(self.settings.value('file_name_default').toString()) != -1:
			self.ui.comboDef.setCurrentIndex(self.ui.comboDef.findText(self.settings.value('file_name_default').toString()) )
		self.ui.comboDef.currentIndexChanged.connect(self.comboDefChanged)
		
	def comboDefChanged(self, file):
		fname = './hotkeys/'+self.ui.comboDef.currentText()
		dom = QDomDocument()
		error = None
		fh = None
		try:
			fh = QFile(fname)
			if not fh.open(QIODevice.ReadOnly):
				raise IOError, unicode(fh.errorString())
			if not dom.setContent(fh):
				raise ValueError, "could not parse XML"
		except (IOError, OSError, ValueError), e:
			error = "Failed to import: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error
		root = dom.documentElement()
		if not root.hasAttribute('fileversion'):
			QMessageBox.information(self.window(), "LearnHotkeys","The file "+self.ui.comboDef.currentText()+" is not an LearnHotkeys definition file.")
			return False
		self.ui.labelDef.setText('<font style="font-weight:bold">'+root.attribute('software')+' - '+root.attribute('softwareversion')+'<font><br>'+root.attribute('def'))
		
	def saveConfig(self):
		self.settings.setValue("file_name_default", self.ui.comboDef.currentText())
		self.accept()
