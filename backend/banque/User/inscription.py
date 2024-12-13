import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox

# URL de l'API pour l'inscription des utilisateurs
url = "http://127.0.0.1:8000/register/"

class MainWindow(QMainWindow):  # Définition de la classe de la fenêtre principale
    def __init__(self):  # Initialisation de la fenêtre principale
        super().__init__()  # Appel du constructeur de la classe parente

        self.setWindowTitle("Inscription d'un Utilisateur")  # Définition du titre de la fenêtre
        self.setGeometry(100, 100, 400, 400)  # Définition de la taille de la fenêtre

        self.central_widget = QWidget()  # Création du widget central
        self.setCentralWidget(self.central_widget)  # Définition du widget central

        self.layout = QVBoxLayout()  # Création d'un layout vertical
        self.central_widget.setLayout(self.layout)  # Définition du layout pour le widget central

        self.form_layout = QFormLayout()  # Création d'un layout de formulaire
        self.layout.addLayout(self.form_layout)  # Ajout du layout de formulaire au layout principal

        # Création des champs du formulaire d'inscription
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Champ de mot de passe masqué
        self.email_input = QLineEdit()
        self.phone_number_input = QLineEdit()
        self.address_input = QLineEdit()
        self.city_input = QLineEdit()
        self.state_input = QLineEdit()
        self.zip_code_input = QLineEdit()
        self.date_of_birth_input = QLineEdit()
        self.occupation_input = QLineEdit()
        self.income_input = QLineEdit()

        # Ajout des champs au layout de formulaire avec des étiquettes
        self.form_layout.addRow("Nom d'utilisateur :", self.username_input)
        self.form_layout.addRow("Mot de passe :", self.password_input)
        self.form_layout.addRow("Email :", self.email_input)
        self.form_layout.addRow("Numéro de téléphone :", self.phone_number_input)
        self.form_layout.addRow("Adresse :", self.address_input)
        self.form_layout.addRow("Ville :", self.city_input)
        self.form_layout.addRow("État :", self.state_input)
        self.form_layout.addRow("Code postal :", self.zip_code_input)
        self.form_layout.addRow("Date de naissance :", self.date_of_birth_input)
        self.form_layout.addRow("Occupation :", self.occupation_input)
        self.form_layout.addRow("Revenu :", self.income_input)

        self.submit_button = QPushButton("S'inscrire")  # Création du bouton de soumission
        self.submit_button.clicked.connect(self.submit_data)  # Connexion du bouton à la méthode de soumission
        self.layout.addWidget(self.submit_button)  # Ajout du bouton au layout principal

    def submit_data(self):  # Méthode de soumission des données du formulaire
        data = {  # Création d'un dictionnaire de données à partir des champs du formulaire
            "username": self.username_input.text(),
            "password": self.password_input.text(),
            "email": self.email_input.text(),
            "phone_number": self.phone_number_input.text(),
            "address": self.address_input.text(),
            "city": self.city_input.text(),
            "state": self.state_input.text(),
            "zip_code": self.zip_code_input.text(),
            "date_of_birth": self.date_of_birth_input.text(),
            "occupation": self.occupation_input.text(),
            "income": self.income_input.text(),
        }

        response = requests.post(url, json=data)  # Envoi des données à l'API via une requête POST

        if response.status_code == 201:  # Vérification du succès de l'inscription
            QMessageBox.information(self, "Succès", "Utilisateur inscrit avec succès")
        else:  # Gestion des erreurs d'inscription
            QMessageBox.warning(self, "Erreur", "Erreur lors de l'inscription")

if __name__ == "__main__":  # Point d'entrée principal de l'application
    app = QApplication(sys.argv)  # Création de l'application PyQt5
    mainWin = MainWindow()  # Création de l'instance de la fenêtre principale
    mainWin.show()  # Affichage de la fenêtre principale
    sys.exit(app.exec_())  # Exécution de l'application PyQt5
