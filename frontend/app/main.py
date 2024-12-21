import os
import sys
from src.ui_test import *
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from src.Function import GuiFunction
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter
from PySide6.QtCore import QSettings,QTimer,Qt,QPoint

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        # loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
            }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)
        self.app_functions=GuiFunction(self)
        self.old_pos=None
       


    def sassCompilationProgress(self, n):
        self.ui.activityProgress.setValue(n)
    # def mousePressEvent(self,event):
        
    #     if event.button()==Qt.LeftButton and self.childAt(event.pos())==self.ui.header: 
    #         self.old_pos=event.globalPos()
    #         print("header clicked")
    # def mouseMoveEvent(self,event):
    #     if self.old_pos:
    #         delta=QPoint(event.globalPos()-self.old_pos)
    #         self.move(self.x()+delta.x(),self.y()+delta.y())
    #         self.old_pos=event.globalPos()
    #         print("header moved")
    # def mouseReleaseEvent(self,event):
    #     if event.button()==Qt.LeftButton:
    #         self.old_pos=None
    #         print("header released")
########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    app_tooltip_filter=QCustomQToolTipFilter(tailPosition="auto")
    app.installEventFilter(app_tooltip_filter)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
