########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import iconify as ico
from iconify.qt import QtGui, QtWidgets
from PySide2.QtCore import *

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        #######################################################################
        # SHOW WINDOW
        #######################################################################


        self.show()

        anim = ico.anim.Breathe()

        icon = ico.Icon('feather:loader', color=QtGui.QColor('orange'), anim=anim)
        # self.ui.pushButton.setIcon(icon)
        icon.setAsButtonIcon(self.ui.pushButton)
        anim.start()
        self.ui.pushButton.setIconSize(QSize(64, 64))



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
