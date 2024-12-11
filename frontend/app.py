import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QWidget, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont

class LoginForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        

        self.setStyleSheet(self.get_stylesheet())
        # Layout principal pour centrer le formulaire
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)
        
        # Conteneur du formulaire
        form_widget = QWidget()
        form_widget.setObjectName("form")
        form_widget.setFixedSize(300, 400)  # Taille fixe pour le formulaire
        form_layout = QVBoxLayout(form_widget)
        form_layout.setAlignment(Qt.AlignCenter)

        # Titre
        title = QLabel("Connexion")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(title)

        # Champ email
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setObjectName("inputField")
        form_layout.addWidget(self.email_input)

        # Champ mot de passe
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mot de passe")
        self.password_input.setObjectName("inputField")
        self.password_input.setEchoMode(QLineEdit.Password)
        form_layout.addWidget(self.password_input)

        # Bouton de connexion
        login_button = QPushButton("Se connecter")
        login_button.setObjectName("loginButton")
        login_button.clicked.connect(self.parent.show_dashboard)
        form_layout.addWidget(login_button)

        # Ajouter le formulaire centré au layout principal
        main_layout.addWidget(form_widget)

    @staticmethod
    def get_stylesheet():
        return """
            QWidget#form {
                background-color: #2c3e50;
                color: #ecf0f1;
                font-family: Arial, sans-serif;
                border-radius:20px;
            }
            QLabel#title {
                font-size: 28px;
                font-weight: bold;
            }
            QLineEdit#inputField {
                background-color: #34495e;
                color: #ecf0f1;
                border: 1px solid #7f8c8d;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton#loginButton {
                background-color: #1abc9c;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton#loginButton:hover {
                background-color: #16a085;
            }
        """


from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 1200, 800)
        self.setup_ui()
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f4f4f4;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c6690;
            }
            QLabel {
                font-size: 14px;
                color: #34495e;
            }
        """)

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        # Barre latérale
        sidebar = QVBoxLayout()
        sidebar.setAlignment(Qt.AlignTop)
        sidebar.setSpacing(20)

        btn_home = QPushButton("Accueil")
        btn_profile = QPushButton("Profil")
        btn_transactions = QPushButton("Historique")
        for btn in [btn_home, btn_profile, btn_transactions]:
            btn.setFixedHeight(50)
            btn.clicked.connect(self.handle_navigation)
            sidebar.addWidget(btn)

        layout.addLayout(sidebar)

        # Zone principale
        self.pages = QStackedWidget()
        self.pages.addWidget(self.create_home_page())
        self.pages.addWidget(self.create_profile_page())
        self.pages.addWidget(self.create_transaction_history_page())
        layout.addWidget(self.pages)

        # Map buttons to pages
        self.navigation_map = {
            "Accueil": 0,
            "Profil": 1,
            "Historique": 2,
        }

    def handle_navigation(self):
        sender = self.sender()
        if sender:
            page_index = self.navigation_map.get(sender.text(), 0)
            self.pages.setCurrentIndex(page_index)

    def create_home_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel("Bienvenue dans l'application bancaire !")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 20, QFont.Bold))
        label.setStyleSheet("color: #2ecc71; margin: 20px;")
        layout.addWidget(label)
        return page

    def create_profile_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignCenter)

        profile_pic = QLabel()
        pixmap = QPixmap(150, 150)
        pixmap.fill(Qt.lightGray)  # Placeholder image
        profile_pic.setPixmap(pixmap)
        profile_pic.setFixedSize(150, 150)
        profile_pic.setAlignment(Qt.AlignCenter)

        username = QLabel("Nom d'utilisateur : John Doe")
        username.setAlignment(Qt.AlignCenter)
        username.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")

        email = QLabel("Email : johndoe@example.com")
        email.setAlignment(Qt.AlignCenter)
        email.setStyleSheet("font-size: 16px; color: #7f8c8d;")

        layout.addWidget(profile_pic)
        layout.addWidget(username)
        layout.addWidget(email)
        return page

    def create_transaction_history_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel("Historique des transactions")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 18, QFont.Bold))
        label.setStyleSheet("color: #e67e22; margin: 20px;")
        layout.addWidget(label)
        return page



class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Bancaire")
        self.setGeometry(100, 100, 800, 600)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login_form = LoginForm(self)
        self.dashboard = Dashboard()

        self.stack.addWidget(self.login_form)
        self.stack.addWidget(self.dashboard)
        self.setObjectName("main")
        self.setStyleSheet("""
            #main {
                border-image: url('images/money1.jpg') 0 0 0 0 stretch stretch;
            }
        """)

        self.show_login()

    def show_login(self):
        self.stack.setCurrentWidget(self.login_form)

    def show_dashboard(self):
        self.stack.setCurrentWidget(self.dashboard)


def main():
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
