import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import requests
class BankAccountForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Formulaire de création de compte bancaire')
        self.setGeometry(100, 100, 500, 700)
        self.setStyleSheet("background-color: #f2f2f2;")
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        # Titre du formulaire
        title = QtWidgets.QLabel("Créer un compte bancaire", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setFont(QtGui.QFont('Arial', 18, QtGui.QFont.Bold))
        layout.addWidget(title)

        # Formulaire principal
        form_layout = QtWidgets.QFormLayout()

        # Champs du formulaire
        self.type_compte = QtWidgets.QComboBox(self)
        self.type_compte.addItems(['Actif', 'Inactif', 'Bloqué'])

        self.account_solde = QtWidgets.QLineEdit(self)
        self.account_solde.setPlaceholderText("Montant du solde")

        self.account_status = QtWidgets.QComboBox(self)
        self.account_status.addItems(['Actif', 'Inactif', 'Bloqué'])

        self.first_name = QtWidgets.QLineEdit(self)
        self.first_name.setPlaceholderText("Prénom")

        self.last_name = QtWidgets.QLineEdit(self)
        self.last_name.setPlaceholderText("Nom")

        self.email = QtWidgets.QLineEdit(self)
        self.email.setPlaceholderText("Email")

        self.phone_number = QtWidgets.QLineEdit(self)
        self.phone_number.setPlaceholderText("Numéro de téléphone")

        self.civility = QtWidgets.QComboBox(self)
        self.civility.addItems(['Mr', 'Mme'])

        self.agency = QtWidgets.QLineEdit(self)
        self.agency.setPlaceholderText("Agence")

        self.birth_day = QtWidgets.QDateEdit(self)
        self.birth_day.setDisplayFormat('yyyy-MM-dd')

        self.nationality = QtWidgets.QComboBox(self)
        self.nationality.addItems(['CD', 'CG', 'GA', 'CM', 'TD'])

        self.zip_code = QtWidgets.QLineEdit(self)
        self.zip_code.setPlaceholderText("Code postal")

        self.pin_code = QtWidgets.QLineEdit(self)
        self.pin_code.setPlaceholderText("Code PIN")
        self.pin_code.setEchoMode(QtWidgets.QLineEdit.Password)

        # Ajouter les champs au layout
        form_layout.addRow("Type de compte:", self.type_compte)
        form_layout.addRow("Solde du compte:", self.account_solde)
        form_layout.addRow("Statut du compte:", self.account_status)
        form_layout.addRow("Prénom:", self.first_name)
        form_layout.addRow("Nom:", self.last_name)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Numéro de téléphone:", self.phone_number)
        form_layout.addRow("Civilité:", self.civility)
        form_layout.addRow("Agence:", self.agency)
        form_layout.addRow("Date de naissance:", self.birth_day)
        form_layout.addRow("Nationalité:", self.nationality)
        form_layout.addRow("Code postal:", self.zip_code)
        form_layout.addRow("Code PIN:", self.pin_code)

        layout.addLayout(form_layout)

        # Bouton de soumission stylisé
        self.submit_button = QtWidgets.QPushButton("Soumettre", self)
        self.submit_button.setFont(QtGui.QFont('Arial', 12, QtGui.QFont.Bold))
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 10px 0;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.submit_button.clicked.connect(self.submit_form)
        layout.addWidget(self.submit_button)

        # Configurer le layout principal
        self.setLayout(layout)

    def submit_form(self):
        data = {
            'type_compte': self.type_compte.currentText(),
            'account_solde': self.account_solde.text(),
            'account_status': self.account_status.currentText(),
            'first_name': self.first_name.text(),
            'last_name': self.last_name.text(),
            'email': self.email.text(),
            'phone_number': self.phone_number.text(),
            'civility': self.civility.currentText(),
            'agency': self.agency.text(),
            'birth_day': self.birth_day.date().toString('yyyy-MM-dd'),
            'nationality': self.nationality.currentText(),
            'zip_code': self.zip_code.text(),
            'pin_code': self.pin_code.text()
        }

        # Validation
        try:
            self.validate_data(data)
            headers = {
            'Content-Type': 'application/json'
        }
            url = "http://127.0.0.1:8000/FS-Bank/create_bank_account/"
            response = requests.post(url, data=data, headers=headers)
            QMessageBox.information(self, "Succès", "Le compte a été créé avec succès!")
        except Exception as e:
            QMessageBox.warning(self, "Erreur", str(e))

    def validate_data(self, data):
        # Validation des données du formulaire
        if not data['first_name'] or not data['last_name']:
            raise Exception("Le prénom et le nom sont requis.")
        if not data['email']:
            raise Exception("L'email est requis.")
        if not data['phone_number']:
            raise Exception("Le numéro de téléphone est requis.")
        if len(data['pin_code']) != 4 or not data['pin_code'].isdigit():
            raise Exception("Le code PIN doit comporter exactement 4 chiffres et ne peut pas contenir de lettres.")
        # Vous pouvez ajouter d'autres validations comme le format de l'email, etc.

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = BankAccountForm()
    form.show()
    sys.exit(app.exec_())
