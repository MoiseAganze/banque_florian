# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_test.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(979, 608)
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(979, 608))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 10, 10, 10)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 30)
        self.widget_6 = QWidget(self.leftMenu)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(46, 42))
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.menuBtn = QPushButton(self.widget_6)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)

        self.verticalLayout_4.addWidget(self.menuBtn)


        self.verticalLayout.addWidget(self.widget_6, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_4 = QWidget(self.leftMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(134, 117))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.accueilBtn = QPushButton(self.widget_4)
        self.accueilBtn.setObjectName(u"accueilBtn")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accueilBtn.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.accueilBtn)

        self.histBtn = QPushButton(self.widget_4)
        self.histBtn.setObjectName(u"histBtn")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.histBtn.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.histBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.depotBtn = QPushButton(self.widget_4)
        self.depotBtn.setObjectName(u"depotBtn")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/arrow-down-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.depotBtn.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.depotBtn)

        self.retraitBtn = QPushButton(self.widget_4)
        self.retraitBtn.setObjectName(u"retraitBtn")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.retraitBtn.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.retraitBtn)

        self.envoiBtn = QPushButton(self.widget_4)
        self.envoiBtn.setObjectName(u"envoiBtn")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/send.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.envoiBtn.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.envoiBtn)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_5 = QWidget(self.leftMenu)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(105, 82))
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.settingsBtn = QPushButton(self.widget_5)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon6)

        self.verticalLayout_3.addWidget(self.settingsBtn)

        self.helpBtn = QPushButton(self.widget_5)
        self.helpBtn.setObjectName(u"helpBtn")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.helpBtn)


        self.verticalLayout.addWidget(self.widget_5, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignLeft)

        self.centerMenu = QCustomSlideMenu(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.widget_7 = QWidget(self.centerMenu)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.widget_7)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeCenterMenuBtn.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.closeCenterMenuBtn)


        self.verticalLayout_5.addWidget(self.widget_7)

        self.centerMenuPages = QStackedWidget(self.centerMenu)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.horizontalLayout_8 = QHBoxLayout(self.settingsPage)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.settingsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.horizontalLayout_21 = QHBoxLayout(self.helpPage)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_2 = QLabel(self.helpPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_2)

        self.centerMenuPages.addWidget(self.helpPage)

        self.verticalLayout_5.addWidget(self.centerMenuPages)


        self.horizontalLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout_10 = QVBoxLayout(self.mainBody)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.mainBody)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(3, 0, 0, 5)
        self.logo = QLabel(self.header)
        self.logo.setObjectName(u"logo")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.logo.setFont(font1)

        self.horizontalLayout_7.addWidget(self.logo, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.notificationBtn = QPushButton(self.frame_4)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/bell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationBtn.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.profileBtn = QPushButton(self.frame_4)
        self.profileBtn.setObjectName(u"profileBtn")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.profileBtn)


        self.horizontalLayout_7.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.frame_6 = QFrame(self.header)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.inimizeBtn = QPushButton(self.frame_6)
        self.inimizeBtn.setObjectName(u"inimizeBtn")
        icon11 = QIcon()
        icon11.addFile(u":/material_design/icons/material_design/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.inimizeBtn.setIcon(icon11)

        self.horizontalLayout_9.addWidget(self.inimizeBtn)

        self.restoreBtn = QPushButton(self.frame_6)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon12 = QIcon()
        icon12.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreBtn.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_6)
        self.closeBtn.setObjectName(u"closeBtn")
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon13)

        self.horizontalLayout_9.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.frame_6, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.header)

        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContents.sizePolicy().hasHeightForWidth())
        self.mainContents.setSizePolicy(sizePolicy1)
        self.mainContents.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_10 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 5, 0)
        self.mainPagesCont = QWidget(self.mainContents)
        self.mainPagesCont.setObjectName(u"mainPagesCont")
        self.mainPagesCont.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_11 = QHBoxLayout(self.mainPagesCont)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.mainPages = QCustomQStackedWidget(self.mainPagesCont)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setMaximumSize(QSize(16777215, 16777215))
        self.pageAccueil = QWidget()
        self.pageAccueil.setObjectName(u"pageAccueil")
        self.horizontalLayout_12 = QHBoxLayout(self.pageAccueil)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.pageAccueil)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_10)

        self.mainPages.addWidget(self.pageAccueil)
        self.pageHist = QWidget()
        self.pageHist.setObjectName(u"pageHist")
        self.horizontalLayout_13 = QHBoxLayout(self.pageHist)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.pageHist)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_11)

        self.mainPages.addWidget(self.pageHist)
        self.pageDepot = QWidget()
        self.pageDepot.setObjectName(u"pageDepot")
        self.horizontalLayout_14 = QHBoxLayout(self.pageDepot)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.pageDepot)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(200, 16777215))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_12)

        self.mainPages.addWidget(self.pageDepot)
        self.pageRetrait = QWidget()
        self.pageRetrait.setObjectName(u"pageRetrait")
        self.horizontalLayout_3 = QHBoxLayout(self.pageRetrait)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.pageRetrait)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.mainPages.addWidget(self.pageRetrait)
        self.pageEnvoi = QWidget()
        self.pageEnvoi.setObjectName(u"pageEnvoi")
        self.horizontalLayout_20 = QHBoxLayout(self.pageEnvoi)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_17 = QLabel(self.pageEnvoi)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_17)

        self.mainPages.addWidget(self.pageEnvoi)

        self.horizontalLayout_11.addWidget(self.mainPages)


        self.horizontalLayout_10.addWidget(self.mainPagesCont)

        self.rightMenu = QCustomSlideMenu(self.mainContents)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMaximumSize(QSize(280, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.widget_14 = QWidget(self.rightMenu)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(self.widget_14)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.closeRightMenuBtn = QPushButton(self.widget_14)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon8)

        self.horizontalLayout_15.addWidget(self.closeRightMenuBtn)


        self.verticalLayout_11.addWidget(self.widget_14)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenu)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.rightMenuPages.setMaximumSize(QSize(274, 16777215))
        self.notificationsPage = QWidget()
        self.notificationsPage.setObjectName(u"notificationsPage")
        self.horizontalLayout_16 = QHBoxLayout(self.notificationsPage)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.notificationsPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_14)

        self.rightMenuPages.addWidget(self.notificationsPage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.profilePage.setMaximumSize(QSize(274, 16777215))
        self.horizontalLayout_18 = QHBoxLayout(self.profilePage)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_8 = QLabel(self.profilePage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_8)

        self.rightMenuPages.addWidget(self.profilePage)

        self.verticalLayout_11.addWidget(self.rightMenuPages)


        self.horizontalLayout_10.addWidget(self.rightMenu)


        self.verticalLayout_10.addWidget(self.mainContents)

        self.footer = QWidget(self.mainBody)
        self.footer.setObjectName(u"footer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 0, 0)
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.footer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(40, -1, 3, 3)
        self.activityProgress = QProgressBar(self.frame_2)
        self.activityProgress.setObjectName(u"activityProgress")
        self.activityProgress.setMaximumSize(QSize(16777215, 10))
        self.activityProgress.setValue(24)
        self.activityProgress.setTextVisible(False)
        self.activityProgress.setOrientation(Qt.Horizontal)
        self.activityProgress.setInvertedAppearance(False)

        self.horizontalLayout_5.addWidget(self.activityProgress)

        self.sizeGrip = QWidget(self.frame_2)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.horizontalLayout_19 = QHBoxLayout(self.sizeGrip)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.sizeGrip)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setPixmap(QPixmap(u":/feather/icons/feather/window_grip.png"))

        self.horizontalLayout_19.addWidget(self.label_16)


        self.horizontalLayout_5.addWidget(self.sizeGrip)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Side Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
        self.accueilBtn.setText(QCoreApplication.translate("MainWindow", u"     ACCUEIL", None))
        self.histBtn.setText(QCoreApplication.translate("MainWindow", u"     HISTORIQUE", None))
        self.depotBtn.setText(QCoreApplication.translate("MainWindow", u"     DEPOT", None))
        self.retraitBtn.setText(QCoreApplication.translate("MainWindow", u"     RETRAIT", None))
        self.envoiBtn.setText(QCoreApplication.translate("MainWindow", u"     ENVOI", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"     PARAMETRES", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"     Aide", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"outils", None))
        self.closeCenterMenuBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"parametres", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"aide", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"BANQUE FLO", None))
        self.notificationBtn.setText("")
        self.profileBtn.setText("")
        self.inimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"historique", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"depot", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"retrait", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Envoi", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"compte", None))
        self.closeRightMenuBtn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright by moses 2024", None))
        self.label_16.setText("")
    # retranslateUi

