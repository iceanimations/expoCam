'''
Created on Aug 22, 2013
@author: qurban.ali
'''
import site
import sys
site.addsitedir("R:/Python_Scripts/plugins/utilities")
import uiContainer
from PyQt4.QtGui import *
import os.path as osp
selfPath = __file__
sys.path.append( 'C:\solidangle\mtoadeploy\2015\scripts' )
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds
cmds.loadPlugin('mtoa')

def main(*args):
    app = QApplication(sys.argv)
    pixmap = QPixmap(r'%s\icons\splash.png'%osp.dirname(osp.dirname(selfPath)))
    spScreen = QSplashScreen(pixmap)
    spScreen.show()
    spScreen.showMessage('Loading...')
    import window as win
    global w
    w = win.Window()
    w.show()
    spScreen.deleteLater()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()