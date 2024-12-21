import os
import sys
from src.ui_test import *
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from src.Function import GuiFunction
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter
from PySide6.QtCore import QSettings, QTimer, Qt, QPoint

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/style.json"})

        ########################################################################
        # SHOW WINDOW
        ########################################################################
        
        self.show()
        
        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET
        ########################################################################
        QAppSettings.updateAppSettings(self)
        self.app_functions = GuiFunction(self)
        
    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton and self.childAt(event.pos()) == self.ui.header:
    #         # Calculer le décalage entre la position de la souris et le coin supérieur gauche de la fenêtre
    #         self.old_pos = event.globalPos() - self.frameGeometry().topLeft()
    #         self._is_moving = True
    #         print("header clicked")

    # def mouseMoveEvent(self, event):
    #     if self._is_moving and self.old_pos is not None:
    #         # Déplacer la fenêtre en maintenant le décalage initial
    #         self.move(event.globalPos() - self.old_pos)
    #         print("header moved")

    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self._is_moving = False
    #         self.old_pos = None
    #         print("header released")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_tooltip_filter = QCustomQToolTipFilter(tailPosition="auto")
    app.installEventFilter(app_tooltip_filter)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())