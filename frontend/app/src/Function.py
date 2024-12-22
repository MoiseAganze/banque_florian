from PySide6.QtGui import QFontDatabase,QFont,QColor
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader
from PySide6.QtCore import QSettings,QTimer,Qt,QPoint
class GuiFunction():
    def __init__(self,MainWindow):
        self.main=MainWindow
        self.ui=MainWindow.ui
        self.loadRobotoFonts()
        self.connectMenubuttons()
    def connectMenubuttons(self):
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenu.collapseMenu())
        self.ui.notificationBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.profileBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenu.collapseMenu()) 
    def createSearchTipOverlay(self):
        self.searchToolTip = QCustomTipOverlay(
            title="Search results.",
            description="Searching...",
            icon=self.main.theme.PATH_RESOURCES+"feather/search.png",
            isClosable=True,
            target=self.ui.searchInputCont,
            parent=self.main,
            aniType="pull-up",
            duration=-1,
            tailPosition="top-center",
            closeIcon=self.main.theme.PATH_RESOURCES+"material_design/close.png", 
        )
        loader = QCustom3CirclesLoader(
            parent=self.main,
            color=QColor(self.main.theme.COLOR_ACCENT_1),
            penWidth=20,
            animationDuration=400
        )
        self.searchToolTip.addWidget(loader)
    def showSearchResult(self):
        searchText=self.ui.searchInput.text()
        if not searchText:
            return
        try:
            self.searchToolTip.show()
        except:
            self.createSearchTipOverlay()
            self.searchToolTip.show()
        self.searchToolTip.setDescription("showing search results for "+searchText)
    def initializeAppTheme(self):
        settings=QSettings()
        current_theme=settings.value("THEME")
        #print(f"current theme is {current_theme}")
        self.populateThemeList(current_theme)
        self.ui.themeList.currentTextChanged.connect(self.changeAppTheme)
    def populateThemeList(self,current_theme):
        theme_count=-1
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name,theme.name)
            if theme.defaultTheme or theme.name==current_theme:
                self.ui.themeList.setCurrentIndex(theme_count)
    def changeAppTheme(self):

        settings=QSettings()
        selected_theme=self.ui.themeList.currentData()
        current_theme=settings.value("THEME")
        print(current_theme)
        if current_theme != selected_theme:
            settings.setValue("THEME",selected_theme)
            QAppSettings.updateAppSettings(self.main,reloadJson=True)
    def loadRobotoFonts(self):
        font_id=QFontDatabase.addApplicationFont("./fonts/Roboto/Roboto-Regular.ttf")
        if font_id==-1:
            print("faled to load roboto font")
        font_family=QFontDatabase.applicationFontFamilies(font_id)
        if font_family:
            roboto=QFont(font_family[0])
        else:
            roboto=QFont("Sans Serif")
        self.main.setFont(roboto)
    