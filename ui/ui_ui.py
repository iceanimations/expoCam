# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\My\Tasks\workSpace\expoCam\ui\ui.ui'
#
# Created: Fri Jun 07 15:19:36 2013
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 413)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.typeWidget = QtGui.QWidget(self.centralwidget)
        self.typeWidget.setObjectName("typeWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.typeWidget)
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.myLabel = QtGui.QLabel(self.typeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myLabel.sizePolicy().hasHeightForWidth())
        self.myLabel.setSizePolicy(sizePolicy)
        self.myLabel.setObjectName("myLabel")
        self.horizontalLayout_3.addWidget(self.myLabel)
        self.typeBox = QtGui.QComboBox(self.typeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeBox.sizePolicy().hasHeightForWidth())
        self.typeBox.setSizePolicy(sizePolicy)
        self.typeBox.setObjectName("typeBox")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.horizontalLayout_3.addWidget(self.typeBox)
        self.verticalLayout.addWidget(self.typeWidget)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.selectAllButton = QtGui.QCheckBox(self.centralwidget)
        self.selectAllButton.setObjectName("selectAllButton")
        self.verticalLayout.addWidget(self.selectAllButton)
        self.camsBox = QtGui.QScrollArea(self.centralwidget)
        self.camsBox.setStyleSheet("")
        self.camsBox.setFrameShape(QtGui.QFrame.WinPanel)
        self.camsBox.setWidgetResizable(True)
        self.camsBox.setObjectName("camsBox")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.camsBox)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 577, 191))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.objectsLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.objectsLayout.setContentsMargins(-1, 1, -1, 1)
        self.objectsLayout.setObjectName("objectsLayout")
        self.noObjectsLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.noObjectsLabel.setEnabled(False)
        self.noObjectsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noObjectsLabel.setObjectName("noObjectsLabel")
        self.objectsLayout.addWidget(self.noObjectsLabel)
        self.camsBox.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.camsBox)
        self.sourceWidget = QtGui.QWidget(self.centralwidget)
        self.sourceWidget.setObjectName("sourceWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.sourceWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(0, 6, 0, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.sourceWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sourcePathBox = QtGui.QLineEdit(self.sourceWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sourcePathBox.setFont(font)
        self.sourcePathBox.setFrame(True)
        self.sourcePathBox.setObjectName("sourcePathBox")
        self.horizontalLayout.addWidget(self.sourcePathBox)
        self.sourceToolButton = QtGui.QToolButton(self.sourceWidget)
        self.sourceToolButton.setObjectName("sourceToolButton")
        self.horizontalLayout.addWidget(self.sourceToolButton)
        self.listObjectsButton = QtGui.QPushButton(self.sourceWidget)
        self.listObjectsButton.setObjectName("listObjectsButton")
        self.horizontalLayout.addWidget(self.listObjectsButton)
        self.verticalLayout.addWidget(self.sourceWidget)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.separateFilesButton = QtGui.QCheckBox(self.centralwidget)
        self.separateFilesButton.setObjectName("separateFilesButton")
        self.verticalLayout.addWidget(self.separateFilesButton)
        self.targetWidget = QtGui.QWidget(self.centralwidget)
        self.targetWidget.setObjectName("targetWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.targetWidget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.targetWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.targetPathBox = QtGui.QLineEdit(self.targetWidget)
        self.targetPathBox.setObjectName("targetPathBox")
        self.horizontalLayout_2.addWidget(self.targetPathBox)
        self.targetToolButton = QtGui.QToolButton(self.targetWidget)
        self.targetToolButton.setObjectName("targetToolButton")
        self.horizontalLayout_2.addWidget(self.targetToolButton)
        self.exportButton = QtGui.QPushButton(self.targetWidget)
        self.exportButton.setDefault(False)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout_2.addWidget(self.exportButton)
        self.verticalLayout.addWidget(self.targetWidget)
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Export Objects", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel.setText(QtGui.QApplication.translate("MainWindow", "Select object type:   ", None, QtGui.QApplication.UnicodeUTF8))
        self.typeBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.typeBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Shader", None, QtGui.QApplication.UnicodeUTF8))
        self.typeBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Light", None, QtGui.QApplication.UnicodeUTF8))
        self.selectAllButton.setText(QtGui.QApplication.translate("MainWindow", "Select all", None, QtGui.QApplication.UnicodeUTF8))
        self.noObjectsLabel.setText(QtGui.QApplication.translate("MainWindow", "No object found...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Source file name:   ", None, QtGui.QApplication.UnicodeUTF8))
        self.sourceToolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.listObjectsButton.setText(QtGui.QApplication.translate("MainWindow", "List", None, QtGui.QApplication.UnicodeUTF8))
        self.separateFilesButton.setText(QtGui.QApplication.translate("MainWindow", "Export as separate files", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Target file name:   ", None, QtGui.QApplication.UnicodeUTF8))
        self.targetToolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.exportButton.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

