# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/LearnHotkeys/editor.ui'
#
# Created: Wed Dec 12 16:15:15 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName(_fromUtf8("Editor"))
        Editor.setWindowModality(QtCore.Qt.NonModal)
        Editor.resize(529, 485)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Editor.sizePolicy().hasHeightForWidth())
        Editor.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QtGui.QWidget(Editor)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 511, 471))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 491, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboHotkeys = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboHotkeys.setObjectName(_fromUtf8("comboHotkeys"))
        self.horizontalLayout.addWidget(self.comboHotkeys)
        self.pushSave = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushSave.setObjectName(_fromUtf8("pushSave"))
        self.horizontalLayout.addWidget(self.pushSave)
        self.pushNew = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushNew.setObjectName(_fromUtf8("pushNew"))
        self.horizontalLayout.addWidget(self.pushNew)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 491, 371))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.description = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.description.setObjectName(_fromUtf8("description"))
        self.horizontalLayout_3.addWidget(self.description)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.webSite = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.webSite.setObjectName(_fromUtf8("webSite"))
        self.horizontalLayout_3.addWidget(self.webSite)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 367))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.fileVersion = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.fileVersion.setObjectName(_fromUtf8("fileVersion"))
        self.horizontalLayout_2.addWidget(self.fileVersion)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.softwareName = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.softwareName.setObjectName(_fromUtf8("softwareName"))
        self.horizontalLayout_2.addWidget(self.softwareName)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.softwareVersion = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.softwareVersion.setObjectName(_fromUtf8("softwareVersion"))
        self.horizontalLayout_2.addWidget(self.softwareVersion)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.totalQuestion = QtGui.QLabel(self.verticalLayoutWidget)
        self.totalQuestion.setObjectName(_fromUtf8("totalQuestion"))
        self.horizontalLayout_4.addWidget(self.totalQuestion)
        self.pushNewQuestion = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushNewQuestion.setObjectName(_fromUtf8("pushNewQuestion"))
        self.horizontalLayout_4.addWidget(self.pushNewQuestion)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.scrollArea = QtGui.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 483, 272))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.retranslateUi(Editor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Editor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Editor.reject)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        Editor.setWindowTitle(QtGui.QApplication.translate("Editor", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSave.setText(QtGui.QApplication.translate("Editor", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushNew.setText(QtGui.QApplication.translate("Editor", "New File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Editor", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Editor", "Web Site Software", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Editor", "File version", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Editor", "Software", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Editor", "Software Version", None, QtGui.QApplication.UnicodeUTF8))
        self.totalQuestion.setText(QtGui.QApplication.translate("Editor", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushNewQuestion.setText(QtGui.QApplication.translate("Editor", "New Question", None, QtGui.QApplication.UnicodeUTF8))

