import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
import json

class BankAccountClient(QWidget):
    def __init__(self):
        super().__init__()
        
        self.attempts = 0  # Compteur pour les tentatives de code PIN
        self.max_attempts = 3  # Nombre maximum de tentatives
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Consultation de Compte Bancaire')

        # Layout principal
        self.layout = QVBoxLayout()

        # Vérifier le code PIN ou récupérer le code PIN
        self.pin_recovery_layout = QVBoxLayout()

        # Champ pour entrer le numéro de compte
        self.label_account_number = QLabel('Entrez votre numéro de compte bancaire:')
        self.account_input = QLineEdit(self)
        self.pin_recovery_layout.addWidget(self.label_account_number)
        self.pin_recovery_layout.addWidget(self.account_input)

        # Bouton pour commencer la récupération du code PIN
        self.recover_button = QPushButton('Récupérer le code PIN', self)
        self.recover_button.clicked.connect(self.recover_pin)
        self.pin_recovery_layout.addWidget(self.recover_button)

        self.layout.addLayout(self.pin_recovery_layout)

        # Champs pour saisir et confirmer le nouveau code PIN (cachés initialement)
        self.pin_input_layout = QVBoxLayout()
        
        self.label_new_pin = QLabel('Entrez votre nouveau code PIN:')
        self.new_pin_input = QLineEdit(self)
        self.new_pin_input.setEchoMode(QLineEdit.Password)
        self.pin_input_layout.addWidget(self.label_new_pin)
        self.pin_input_layout.addWidget(self.new_pin_input)

        self.label_confirm_pin = QLabel('Confirmez votre nouveau code PIN:')
        self.confirm_pin_input = QLineEdit(self)
        self.confirm_pin_input.setEchoMode(QLineEdit.Password)
        self.pin_input_layout.addWidget(self.label_confirm_pin)
        self.pin_input_layout.addWidget(self.confirm_pin_input)

        # Bouton pour soumettre le nouveau code PIN
        self.submit_pin_button = QPushButton('Valider le nouveau code PIN', self)
        self.submit_pin_button.clicked.connect(self.submit_new_pin)
        self.pin_input_layout.addWidget(self.submit_pin_button)

        self.layout.addLayout(self.pin_input_layout)

        # Ajouter le layout à la fenêtre
        self.setLayout(self.layout)

        # Masquer les champs de récupération de code PIN
        self.set_widgets_visible(self.pin_input_layout, False)

    def recover_pin(self):
        # Vérification du numéro de compte
        account_number = self.account_input.text()

        if not account_number:
            self.show_error_message("Veuillez entrer un numéro de compte.")
            return

        if self.attempts >= self.max_attempts:
            self.show_error_message(f"Vous avez atteint le nombre maximum de tentatives ({self.max_attempts}).")
            return
        
        with open('token.json', 'r') as f:
            token_data = json.load(f)
            access_token = token_data.get('access_token') 
        
        if access_token:
            headers = {
                'Authorization': f'Bearer {access_token}', 
                'Content-Type': 'application/json' 
            }

        # Requête pour vérifier si le numéro de compte existe
        url = "http://127.0.0.1:8000/FS-Bank/VerifyAccountNumber/"
        response = requests.post(url, data={'account_number': account_number},headers=headers)

        if response.status_code == 200:
            # Si le numéro de compte est valide, afficher les champs pour saisir le nouveau code PIN
            self.set_widgets_visible(self.pin_recovery_layout, False)  # Masquer la partie récupération
            self.set_widgets_visible(self.pin_input_layout, True)  # Afficher la partie saisie du PIN
        else:
            self.attempts += 1
            self.show_error_message(f"Numéro de compte invalide. Tentative {self.attempts}/{self.max_attempts}")

    def submit_new_pin(self):
        # Soumettre le nouveau code PIN
        new_pin = self.new_pin_input.text()
        confirm_pin = self.confirm_pin_input.text()

        if new_pin != confirm_pin:
            self.show_error_message("Les codes PIN ne correspondent pas.")
            return

        if len(new_pin) != 4:  # Vérifiez que le code PIN est de 4 chiffres
            self.show_error_message("Le code PIN doit comporter 4 chiffres.")
            return
        
        url = "http://127.0.0.1:8000/FS-Bank/ResetCodePin/"

        # Soumettre la mise à jour du code PIN
        account_number = self.account_input.text()
        response = requests.post(url, data={'account_number': account_number, 'new_pin': new_pin})

        if response.status_code == 200:
            self.show_error_message("Code PIN mis à jour avec succès!")
            self.close()  # Fermer la fenêtre une fois la mise à jour effectuée
        else:
            self.show_error_message("Erreur lors de la mise à jour du code PIN.")

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Erreur")
        msg.exec_()

    def set_widgets_visible(self, layout, visible):
        # Utiliser cette fonction pour rendre visible/invisible les widgets dans un layout
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setVisible(visible)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BankAccountClient()
    window.show()
    sys.exit(app.exec_())
