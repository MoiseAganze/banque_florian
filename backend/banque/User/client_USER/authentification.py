import requests
import json

"""
Moise, je n'ai pas pu écrire une documentation des API qui gèrent les utilisateurs mais au moins j'ai constuit un client PYQT5 
pour te montrer comment tu peux t'y prendre.
le lien qui inscrit les user est :


register_url  = "http://127.0.0.1:8000/user/inscription_user/"
login_url = "http://127.0.0.1:8000/user/login_user/"
logout_url = "http://127.0.0.1:8000/user/login_user/"


je n'ai pas encore gerer la suppression de compte users et je ne pense le faire maintenant



tu as de questions ? faites-moi signe

"""
class AuthClient:
    def __init__(self, backend_url):
        self.backend_url = backend_url
        self.token = None  
    def authenticate(self, email, password):
        url = f"{self.backend_url}/user/login_user/"
        payload = {
            'email': "floriandiangongo22@gmail.com",
            'password': "123"
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.token = data.get('access_token')  
            with open('token.json', 'w') as f:
                json.dump({'access_token': self.token}, f)
            print("Authentification réussie")
        else:
            print("Échec de l'authentification :", response.text)
    def logout(self):
        """Réinitialiser le token à la déconnexion"""
        self.token = None
        with open('token.json', 'w') as f:
            json.dump({'access_token': None}, f)
        print("Déconnexion réussie")
    def get_token(self):
        return self.token
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.auth_client = AuthClient(backend_url="http://127.0.0.1:8000")
        self.setWindowTitle("Florian et Moise interaction APP")
        self.login_button = QPushButton("Se connecter", self)
        self.login_button.clicked.connect(self.login)
        self.login_button.resize(200, 50)
        self.login_button.move(100, 50)
        self.logout_button = QPushButton("Se déconnecter", self)
        self.logout_button.clicked.connect(self.logout)
        self.logout_button.resize(200, 50)
        self.logout_button.move(100, 150)
    def login(self):
        email = "floriandiangongo22@gmail.com"
        password = "123"
        self.auth_client.authenticate(email, password)
    def logout(self):
        self.auth_client.logout()
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
