import sys
import requests
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class BankAccountClient(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialiser l'interface
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Consultation de Compte Bancaire')
        
        # Créer les éléments de l'interface
        self.layout = QVBoxLayout()
        
        self.label_pin = QLabel('Entrez votre code PIN:')
        self.layout.addWidget(self.label_pin)

        self.pin_input = QLineEdit(self)
        self.pin_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.pin_input)
        
        self.check_button = QPushButton('Vérifier le code PIN', self)
        self.check_button.clicked.connect(self.verify_pin)
        self.layout.addWidget(self.check_button)
        
        self.result_label = QLabel('')
        self.layout.addWidget(self.result_label)
        
        self.setLayout(self.layout)

    def verify_pin(self):
        pin = self.pin_input.text()
        if not pin:
            self.show_error_message("Veuillez entrer un code PIN.")
            return
        with open('token.json', 'r') as f:
            token_data = json.load(f)
            access_token = token_data.get('access_token') 
        if access_token:
            headers = {
                'Authorization': f'Bearer {access_token}', 
                'Content-Type': 'application/json' 
            }
        url = 'http://127.0.0.1:8000/FS-Bank/ViewBankAccount' 
        params = {'pin': pin}
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            account_info = response.json()
            self.result_label.setText(f"Compte bancaire: {account_info}")
        else:
            self.show_error_message(response.json().get('detail', 'Erreur inconnue'))

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Erreur")
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BankAccountClient()
    window.show()
    sys.exit(app.exec_())
