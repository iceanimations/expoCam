'''
Created on Aug 22, 2013
@author: qurban.ali
'''
import site
import sys
site.addsitedir(r"R:\Pipe_Repo\Users\Qurban\mayaize")
import mayaize2013
site.addsitedir(r"R:\Python_Scripts")
from PyQt4.QtGui import *
import os.path as osp
selfPath = sys.modules[__name__].__file__

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