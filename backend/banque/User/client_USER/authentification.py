import requests
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QComboBox, QFormLayout, QDateEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from datetime import date
import jwt

# Classe pour gérer l'authentification
class AuthClient:
    def __init__(self, backend_url):
        self.backend_url = backend_url
        self.token = None  # Token d'accès initialement vide

    def authenticate(self, email, password):
        """Authentification avec email et mot de passe, en récupérant un token JWT"""
        url = f"{self.backend_url}/login_user/"
        payload = {
            'email': email,
            'password': password
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.token = data.get('access_token')  # On stocke le token dans le client
            with open('token.json', 'w') as f:
                json.dump({'access_token': self.token}, f)
            return True
        else:
            return False

    def logout(self):
        """Réinitialiser le token à la déconnexion"""
        self.token = None
        with open('token.json', 'w') as f:
            json.dump({'access_token': None}, f)

    def get_token(self):
        """Retourne le token d'accès"""
        return self.token

    def get_user_id(self):
        """Récupère l'ID de l'utilisateur à partir du token JWT"""
        if self.token:
            try:
                decoded_token = jwt.decode(self.token, options={"verify_signature": False})  # Décodage sans vérification de la signature
                return decoded_token.get('user_id')  # Récupère l'ID de l'utilisateur dans le token
            except jwt.ExpiredSignatureError:
                return None
        return None


# Classe pour le formulaire de création de compte bancaire
class BankAccountForm(QWidget):
    def __init__(self, auth_client):
        super().__init__()
        self.auth_client = auth_client
        self.setWindowTitle("Formulaire de création de compte bancaire")
        self.setGeometry(100, 100, 500, 700)
        self.setStyleSheet("background-color: #f2f2f2;")
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()

        # Champs de texte
        self.input_first_name = QLineEdit(self)
        self.input_first_name.setPlaceholderText("Prénom")
        layout.addRow("Prénom:", self.input_first_name)

        self.input_last_name = QLineEdit(self)
        self.input_last_name.setPlaceholderText("Nom")
        layout.addRow("Nom:", self.input_last_name)

        self.input_email = QLineEdit(self)
        self.input_email.setPlaceholderText("Email")
        layout.addRow("Email:", self.input_email)

        self.input_phone_number = QLineEdit(self)
        self.input_phone_number.setPlaceholderText("Numéro de téléphone")
        layout.addRow("Numéro de téléphone:", self.input_phone_number)

        self.input_civility = QLineEdit(self)
        self.input_civility.setPlaceholderText("Civilité")
        layout.addRow("Civilité:", self.input_civility)

        self.input_agency = QLineEdit(self)
        self.input_agency.setPlaceholderText("Agence")
        layout.addRow("Agence:", self.input_agency)

        self.input_zip_code = QLineEdit(self)
        self.input_zip_code.setPlaceholderText("Code postal")
        layout.addRow("Code postal:", self.input_zip_code)

        self.input_pin_code = QLineEdit(self)
        self.input_pin_code.setPlaceholderText("Code PIN")
        self.input_pin_code.setMaxLength(4)
        self.input_pin_code.setValidator(QIntValidator(1000, 9999))  # Validation du PIN (4 chiffres)
        layout.addRow("Code PIN:", self.input_pin_code)

        # Menus déroulants pour les sélections
        self.input_type_compte = QComboBox(self)
        self.input_type_compte.addItems(['Actif', 'Inactif', 'Bloqué'])
        layout.addRow("Type de compte:", self.input_type_compte)

        self.input_account_status = QComboBox(self)
        self.input_account_status.addItems(['Actif', 'Inactif'])
        layout.addRow("Statut du compte:", self.input_account_status)

        self.input_nationality = QComboBox(self)
        self.input_nationality.addItem("République Démocratique du Congo (RDC)", "CD")
        self.input_nationality.addItem("République du Congo (Congo-Brazzaville)", "CG")
        self.input_nationality.addItem("Gabon", "GA")
        self.input_nationality.addItem("Cameroun", "CM")
        self.input_nationality.addItem("Tchad", "TD")
        layout.addRow("Nationalité:", self.input_nationality)
        
        # Champ de date pour la date de naissance
        self.input_birth_day = QDateEdit(self)
        self.input_birth_day.setDate(date.today())  # Par défaut la date d'aujourd'hui
        self.input_birth_day.setDisplayFormat("yyyy-MM-dd")
        layout.addRow("Date de naissance:", self.input_birth_day)

        # Champ pour le solde du compte
        self.input_solde = QLineEdit(self)
        self.input_solde.setPlaceholderText("Solde du compte")
        self.input_solde.setValidator(QIntValidator(0, 999999))  # Validation du solde (valeur numérique)
        layout.addRow("Solde du compte:", self.input_solde)

        # Bouton de soumission
        self.submit_button = QPushButton("Soumettre", self)
        self.submit_button.clicked.connect(self.submit_form)
        layout.addRow(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        """Récupérer les données du formulaire et envoyer la requête au serveur."""
        user_id = self.auth_client.get_user_id()  # Récupérer l'ID de l'utilisateur connecté
        if not user_id:
            QMessageBox.warning(self, "Erreur", "L'utilisateur n'est pas connecté")
            return

        form_data = {
            "user": user_id,
            'type_compte': self.input_type_compte.currentText().lower(),
            'account_solde': self.input_solde.text(),
            'account_status': self.input_account_status.currentText(),
            'first_name': self.input_first_name.text(),
            'last_name': self.input_last_name.text(),
            'email': self.input_email.text(),
            'phone_number': self.input_phone_number.text(),
            'civility': self.input_civility.text(),
            'agency': self.input_agency.text(),
            'birth_day': self.input_birth_day.text(),  # Format yyyy-MM-dd
            'nationality': self.input_nationality.currentText(),
            'zip_code': self.input_zip_code.text(),
            'pin_code': self.input_pin_code.text()
        }

        # Récupérer le token d'accès depuis le fichier token.json
        with open('token.json', 'r') as f:
            token_data = json.load(f)
            access_token = token_data.get('access_token')

        # Vérifier si le token existe
        if access_token:
            headers = {
                'Authorization': f'Bearer {access_token}',  # Authentification via token
                'Content-Type': 'application/json'  # Déclaration de type JSON
            }

            # Envoi de la requête au serveur
            url = "http://127.0.0.1:8000/FS-Bank/create_bank_account/"
            response = requests.post(url, json=form_data, headers=headers)

            if response.status_code == 201:
                print("Réponse du serveur:", response.json())
                print("Code de statut:", response.status_code)
                QMessageBox.information(self, "Succès", "Compte bancaire créé avec succès.")
            else:
                print(f"Erreur lors de la soumission: {response.status_code} - {response.text}")
                QMessageBox.warning(self, "Erreur", "Erreur lors de la création du compte bancaire.")
        else:
            print("Aucun token d'accès trouvé. Veuillez vous connecter d'abord.")


# Classe pour la fenêtre principale avec gestion de la connexion
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.auth_client = AuthClient(backend_url="http://127.0.0.1:8000")
        self.setWindowTitle("Application de gestion de compte")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Email")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Mot de passe")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Se connecter", self)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.logout_button = QPushButton("Se déconnecter", self)
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def login(self):
        email = self.username_input.text()
        password = self.password_input.text()
        
        if self.auth_client.authenticate(email, password):
            self.open_bank_account_form()
        else:
            QMessageBox.warning(self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    def open_bank_account_form(self):
        self.close()  # Fermer la fenêtre de connexion
        self.bank_account_form = BankAccountForm(auth_client=self.auth_client)
        self.bank_account_form.show()

    def logout(self):
        self.auth_client.logout()
        self.close()  # Fermer la fenêtre de formulaire bancaire si un utilisateur se déconnecte


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
