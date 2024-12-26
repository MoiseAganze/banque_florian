# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_auth.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
class Ui_auth(object):
    def setupUi(self, auth):
        if not auth.objectName():
            auth.setObjectName(u"auth")
        auth.resize(677, 660)
        self.verticalLayout_3 = QVBoxLayout(auth)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.auth_pages = QCustomQStackedWidget(auth)
        self.auth_pages.setObjectName(u"auth_pages")
        self.page_connexion = QWidget()
        self.page_connexion.setObjectName(u"page_connexion")
        self.verticalLayout_4 = QVBoxLayout(self.page_connexion)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.page_connexion)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.widget_3 = QWidget(self.page_connexion)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(400, 0))
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login_email = QLineEdit(self.widget_4)
        self.login_email.setObjectName(u"login_email")

        self.verticalLayout_2.addWidget(self.login_email)

        self.login_password = QLineEdit(self.widget_4)
        self.login_password.setObjectName(u"login_password")

        self.verticalLayout_2.addWidget(self.login_password)

        self.valider_connexion = QPushButton(self.widget_4)
        self.valider_connexion.setObjectName(u"valider_connexion")

        self.verticalLayout_2.addWidget(self.valider_connexion)

        self.error_login = QLabel(self.widget_4)
        self.error_login.setObjectName(u"error_login")
        self.error_login.setStyleSheet(u"color:red;")
        self.error_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.error_login)


        self.horizontalLayout_2.addWidget(self.widget_4)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(self.page_connexion)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.link_inscription = QPushButton(self.widget_2)
        self.link_inscription.setObjectName(u"link_inscription")

        self.verticalLayout.addWidget(self.link_inscription)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon()
        icon.addFile(u":/font_awesome/brands/icons/font_awesome/brands/google.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.auth_pages.addWidget(self.page_connexion)
        self.page_inscription = QWidget()
        self.page_inscription.setObjectName(u"page_inscription")
        self.verticalLayout_5 = QVBoxLayout(self.page_inscription)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_5 = QWidget(self.page_inscription)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.widget_6 = QWidget(self.page_inscription)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.widget_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.register_lastname = QLineEdit(self.widget_10)
        self.register_lastname.setObjectName(u"register_lastname")

        self.horizontalLayout_4.addWidget(self.register_lastname)

        self.register_firstname = QLineEdit(self.widget_10)
        self.register_firstname.setObjectName(u"register_firstname")

        self.horizontalLayout_4.addWidget(self.register_firstname)


        self.verticalLayout_8.addWidget(self.widget_10)

        self.register_email = QLineEdit(self.widget_7)
        self.register_email.setObjectName(u"register_email")

        self.verticalLayout_8.addWidget(self.register_email)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.register_password = QLineEdit(self.widget_8)
        self.register_password.setObjectName(u"register_password")

        self.horizontalLayout_5.addWidget(self.register_password)

        self.register_confirm = QLineEdit(self.widget_8)
        self.register_confirm.setObjectName(u"register_confirm")

        self.horizontalLayout_5.addWidget(self.register_confirm)


        self.verticalLayout_8.addWidget(self.widget_8)

        self.valider_inscription = QPushButton(self.widget_7)
        self.valider_inscription.setObjectName(u"valider_inscription")

        self.verticalLayout_8.addWidget(self.valider_inscription)

        self.error_register = QLabel(self.widget_7)
        self.error_register.setObjectName(u"error_register")
        self.error_register.setEnabled(True)
        self.error_register.setStyleSheet(u"color:red;")
        self.error_register.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.error_register)


        self.horizontalLayout_6.addWidget(self.widget_7)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.widget_9 = QWidget(self.page_inscription)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_7 = QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.link_connexion = QPushButton(self.widget_9)
        self.link_connexion.setObjectName(u"link_connexion")

        self.verticalLayout_7.addWidget(self.link_connexion)

        self.pushButton_5 = QPushButton(self.widget_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIcon(icon)

        self.verticalLayout_7.addWidget(self.pushButton_5)


        self.verticalLayout_5.addWidget(self.widget_9)

        self.auth_pages.addWidget(self.page_inscription)

        self.verticalLayout_3.addWidget(self.auth_pages)


        self.retranslateUi(auth)

        QMetaObject.connectSlotsByName(auth)
    # setupUi

    def retranslateUi(self, auth):
        auth.setWindowTitle(QCoreApplication.translate("auth", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("auth", u"Se Connecter", None))
        self.login_email.setPlaceholderText(QCoreApplication.translate("auth", u"adresse email", None))
        self.login_password.setPlaceholderText(QCoreApplication.translate("auth", u"mot de passe", None))
        self.valider_connexion.setText(QCoreApplication.translate("auth", u"VALIDER", None))
        self.error_login.setText("")
        self.link_inscription.setText(QCoreApplication.translate("auth", u"Creer un compte", None))
        self.pushButton_2.setText(QCoreApplication.translate("auth", u"Continuer avec google", None))
        self.label_2.setText(QCoreApplication.translate("auth", u"INSCRIPTION", None))
        self.register_lastname.setText("")
        self.register_lastname.setPlaceholderText(QCoreApplication.translate("auth", u"votre nom", None))
        self.register_firstname.setPlaceholderText(QCoreApplication.translate("auth", u"votre prenom", None))
        self.register_email.setPlaceholderText(QCoreApplication.translate("auth", u"adresse email", None))
        self.register_password.setPlaceholderText(QCoreApplication.translate("auth", u"mot de passe", None))
        self.register_confirm.setPlaceholderText(QCoreApplication.translate("auth", u"confirmer", None))
        self.valider_inscription.setText(QCoreApplication.translate("auth", u"valider", None))
        self.error_register.setText("")
        self.link_connexion.setText(QCoreApplication.translate("auth", u"se connecter", None))
        self.pushButton_5.setText(QCoreApplication.translate("auth", u"continuer avec google", None))
    # retranslateUi

