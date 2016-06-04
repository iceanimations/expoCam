
import os
osp = os.path
import window
selfPath = window.__file__
import PyQt4
from PyQt4 import QtGui, QtCore, uic
Qt = QtCore.Qt
import logic
import time
import subprocess
import re

form, base = uic.loadUiType(r"%s\ui\ui.ui"%osp.dirname(osp.dirname(window.__file__)))
class Window(form, base):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.exportButton.clicked.connect(self.export)
        self.closeButton.clicked.connect(self.closeWindow)
        self.sourceToolButton.clicked.connect(lambda : self.showFileDialog())
        self.targetToolButton.clicked.connect(lambda : self.dialogCaller())
        self.selectAllButton.clicked.connect(self.selectAll)
        self.separateFilesButton.clicked.connect(lambda : self.switchSeparateFilesButton())
        self.listObjectsButton.clicked.connect(self.callListObjects)
        self.sourcePathBox.returnPressed.connect(self.callListObjects)
        self.targetPathBox.returnPressed.connect(self.export)
        self.typeBox.currentIndexChanged.connect(self.handleTypeBox)
        self.objects = []
        self.separateFiles = False
        self.spacerItem = None
        self.setWindowIcon(QtGui.QIcon(r'%s\icons\ef.png' % osp.dirname(osp.dirname(selfPath))))
        self.sourcePath = ''
        self.handleTypeBox()
        self.setWindowTitle("ExpoFast")
        self.scene = logic.Scene(self)
        self.iSize = QtCore.QSize(5,5)
        self.setIconSize(self.iSize)
        #system tray icon
        self.createSystemTrayIcon()
        
    def createSystemTrayIcon(self):
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setIcon(QtGui.QIcon(r'%s\icons\ef.png' % osp.dirname(osp.dirname(selfPath))))
        self.trayIcon.setToolTip('expoFast')
        self.trayIcon.show()

    def dialogCaller(self):
        '''opens the appropriate file dialog'''
        if self.separateFiles:
            self.showFolderDialog()
        else: self.showSaveDialog()
    
    def handleTypeBox(self):
        '''handles the change of object type'''
        text = self.typeBox.currentText()
        self.objectType = text
        self.listObjectsButton.setText("List "+ text)
        self.noObjectsLabel.setText("Choose a source file to list "+ text)
        if self.sourcePath and osp.exists(self.sourcePath):
            try:
                self.listObjects()
            except:
                pass
        if text == "Camera":
            pass
        if text == "Shader":
            pass
        if text == "Light":
            pass

    def closeWindow(self):
        '''called on the close event of the main window'''
        self.close()
        self.deleteLater()

    def selectAll(self):
        '''selects/deselects objects when the select all button is pressed'''
        if self.selectAllButton.isChecked():
            for obj in self.objects:
                obj.setChecked(True)
        else:
            for obj in self.objects:
                obj.setChecked(False)
                
    def switchSelectAll(self):
        '''deselects the select all button if the user deselects the any of
        the objects after selecting all and vice versa'''
        flag = True
        for obj in self.objects:
            if not obj.isChecked():
                flag = False
                break
        self.selectAllButton.setChecked(flag)
        

    def switchSeparateFilesButton(self):
        if self.separateFilesButton.isChecked():
            self.separateFiles = True
        else:
            self.separateFiles = False

    def callListObjects(self):
        '''starts the worker thread'''
        path = str(self.sourcePathBox.text()).strip('\"')
        if not osp.exists(path):
            self.msgBox({'msg': 'The system could not find the path specified\n'+ self.sourcePath,
                         'icon': QtGui.QMessageBox.Warning})
            return
        if not osp.splitext(path)[-1] in ['.ma', '.mb']:
            self.msgBox({'msg': 'The system could not recognize the file as a valid Maya file\n'+ path,
                         'icon': QtGui.QMessageBox.Warning})
            return
        if path != self.sourcePath:
            self.noObjectsLabel.show()
            self.noObjectsLabel.setText("Extracting "+ self.objectType + "s...")
            self.noObjectsLabel.repaint(1,1,1,1)
            self.scene.openScene(path)
            self.sourcePath = path
        self.listObjects()

    def listObjects(self):
        self.selectAllButton.setChecked(False)
        if self.objects:
            for obj in self.objects:
                obj.deleteLater()
            self.objects = []
        objs = self.scene.objects(str(self.objectType).lower())
        if objs:
            self.noObjectsLabel.hide()
            for obj in objs:
                chkBox = QtGui.QCheckBox(self)
                chkBox.setStyleSheet("background-color: #e0e0e0")
                text = str(obj)
                chkBox.setText(text)
                chkBox.clicked.connect(self.switchSelectAll)
                self.objects.append(chkBox)
                self.objectsLayout.addWidget(chkBox)
        else:
            self.noObjectsLabel.setText("No "+ self.objectType +" found...")
            self.noObjectsLabel.show()
            self.noObjectsLabel.repaint(1,1,1,1)
        self.trayIcon.showMessage('expoFast objects ready',
                                  'expoFast is done with the fetching and listing of the objects',
                                  QtGui.QSystemTrayIcon.Information, 5000)

    def export(self):
        self.targetPath = str(self.targetPathBox.text()).strip('\"')
        if not self.targetPath:
            self.msgBox({'msg': 'The system could not find the path specified', 'icon': QtGui.QMessageBox.Warning})
            return
        self.targetPath = osp.normpath(self.targetPath)
        if not osp.exists(self.targetPath):
            if self.separateFiles:
                directoryName = self.targetPath
            else: directoryName = osp.dirname(self.targetPath)
            try:
                if not osp.exists(directoryName):
                    os.mkdir(directoryName)
            except WindowsError as we:
                self.msgBox({'msg': we.strerror +'\n'+ directoryName,
                             'icon': QtGui.QMessageBox.Warning})
                return
        selectedObjects = []
        gotoLocPath = None
        for obj in self.objects:
            if obj.isChecked():
                selectedObjects.append(str(obj.text()))
        if selectedObjects:
            try:
                if self.separateFiles:
                    for obj in selectedObjects:
                        self.scene.selectObjects([obj])
                        obj = logic.purgeChar(obj, replace = '_')
                        fileName = osp.join(self.targetPath, obj +'.ma')
                        self.scene.export(fileName)
                else:
                    self.scene.selectObjects(selectedObjects)
                    if not osp.splitext(self.targetPath)[-1]:
                        self.targetPath = self.targetPath + '.ma'
                    self.scene.export(self.targetPath)
            except WindowsError as we:
                self.msgBox({'msg': we.strerror, 'icon': QtGui.QMessageBox.Warning})
                return
            except RuntimeError as rerror:
                self.msgBox({'msg': str(rerror), 'icon': QtGui.QMessageBox.Warning})
                return
            self.gotoLocation(self.targetPath)
        else: self.msgBox({'msg': 'No '+ self.objectType +' selected', 'icon': QtGui.QMessageBox.Warning})

    def gotoLocation(self, path):
        if path and osp.exists(path):
            s = ' '
            if osp.isfile(path):
                s = ' /select,'
            subprocess.Popen('explorer%s'%s + osp.normpath(path))

    def showSaveDialog(self):
        path = QtGui.QFileDialog.getSaveFileName(self, 'File name', '',  '*.ma *.mb')
        self.targetPathBox.setText(path)

    def showFileDialog(self, fileType = '*.mb *.ma', title = 'Select file', path = ''):
        dialog = QtGui.QFileDialog(self, title, path, fileType)
        if dialog.exec_():
            userSelectedThumb = dialog.selectedFiles()[0]
            if osp.exists(userSelectedThumb) and osp.isfile(userSelectedThumb):
                self.sourcePathBox.setText(userSelectedThumb)
                self.callListObjects()

    def showFolderDialog(self):
        path = QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', '',  QtGui.QFileDialog.ShowDirsOnly)
        self.targetPathBox.setText(path)

    def msgBox(self, args = None):
        '''
        dispalys the warnings
        @params:
                args: a dictionary containing the following sequence of variables
                {'msg': 'msg to be displayed'[, 'ques': 'question to be asked'],
                'btns': QMessageBox.btn1 | QMessageBox.btn2 | ....}
        '''
        if args.has_key('msg'):
            if not args.has_key('btns'):
                args['btns'] = QtGui.QMessageBox.Ok
            mBox = QtGui.QMessageBox(self)
            mBox.setWindowModality(Qt.ApplicationModal)
            mBox.setWindowTitle('ExpoFast')
            mBox.setText(args['msg'])
            if args.has_key('ques'):
                mBox.setInformativeText(args['ques'])
            if args.has_key('icon'):
                mBox.setIcon(args['icon'])
            if args.has_key('details'):
                mBox.setDetailedText(args['details'])
            mBox.setStandardButtons(args['btns'])
            buttonPressed = mBox.exec_()
            return buttonPressed