from PySide6.QtCore import QSettings, QEasingCurve
from PySide6.QtWidgets import QStackedWidget
import re
import requests
import json
from src.utils.write import ecrire_dans_fichier_json

class AuthFunctions:
    def __init__(self, AuthDialog, MainWindow):
        self.main = AuthDialog
        self.ui = AuthDialog.ui
        self.dash = MainWindow

        self.ui.valider_inscription.clicked.connect(self.handle_inscription)
        self.ui.valider_connexion.clicked.connect(self.handle_connexion)

    def handle_inscription(self):
        result = self.validate_inscription()
        if result["success"]:
            self.slide_to_page_connexion()
        else:
            self.ui.error_register.setText(result["message"])

    def handle_connexion(self):
        result = self.validate_connexion()
        if result["success"]:
            self.show_dashboard(self.dash)
        else:
            self.ui.error_login.setText(result["message"])

    def validate_inscription(self):
        self.ui.error_register.setText("")
        data = {
            "last_name": self.ui.register_lastname.text(),
            "first_name": self.ui.register_firstname.text(),
            "email": self.ui.register_email.text(),
            "password": self.ui.register_password.text(),
            "confirm": self.ui.register_confirm.text(),
        }

        messages = {
            "last_name": "Le nom doit contenir au moins 2 caractères.",
            "first_name": "Le prénom doit contenir au moins 2 caractères.",
            "email": "L'adresse e-mail est invalide.",
            "password": "Le mot de passe doit contenir au moins 8 caractères.",
            "confirm": "La confirmation ne correspond pas au mot de passe.",
        }

        validators = {
            "last_name": lambda v: len(v) >= 2,
            "first_name": lambda v: len(v) >= 2,
            "email": lambda v: re.match(r"^[^@]+@[^@]+\.[^@]+$", v),
            "password": lambda v: len(v) >= 8,
            "confirm": lambda v: v == data["password"],
        }

        return self.validate_fields(data, validators, messages, "register", "http://127.0.0.1:8000/inscription_user/")

    def validate_connexion(self):
        self.ui.error_login.setText("")
        data = {
            "email": self.ui.login_email.text(),
            "password": self.ui.login_password.text(),
        }

        messages = {
            "email": "L'adresse e-mail est invalide.",
            "password": "Le mot de passe est requis.",
        }

        validators = {
            "email": lambda v: re.match(r"^[^@]+@[^@]+\.[^@]+$", v),
            "password": lambda v: len(v) > 0,
        }

        return self.validate_fields(data, validators, messages, "login", "http://127.0.0.1:8000/login_user/")

    def validate_fields(self, data, validators, messages, action, url):
        errors = [messages[key] for key, validate in validators.items() if not validate(data[key])]

        if not all(value for value in data.values()):
            return {"success": False, "message": "Veuillez remplir tous les champs."}
        elif errors:
            return {"success": False, "message": errors[0]}

        headers = {"Content-Type": "application/json"}
            
        result = self.send_post_request(action,url, data, headers)
        print(result)
        ecrire_dans_fichier_json(f"datas/userauth/tokens.json",{"access":result["access_token"],"refresh":result["token_refresh"]})

        return result

    def slide_to_page_connexion(self):
        stacked_widget = self.ui.auth_pages
        target_page_index = stacked_widget.indexOf(self.ui.page_connexion)

        if target_page_index != -1:
            stacked_widget.setCurrentIndex(target_page_index)
            print("Transition vers la page de connexion effectuée !")

    def show_dashboard(self, dash):
        self.main.hide()
        dash.show()

    def toggle_loading_button(self, is_loading, action):
        button = self.ui.valider_inscription if action == "register" else self.ui.valider_connexion
        if is_loading:
            button.setText("Patientez...")
            button.setDisabled(True)
        else:
            button.setText("VALIDER")
            button.setDisabled(False)

    def send_post_request(self,action, url, data, headers=None):
        try:
            self.toggle_loading_button(True, action)
            response = requests.post(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return {**response.json(),"success":True,"message":"ok"}
        except requests.exceptions.RequestException as e:
            error_message=self.get_error_message(e.response)
            return {"success":False,"message":error_message}
        except ValueError as e:
            return {"success":False,"message":"erreur serveur"}
        finally:
            self.toggle_loading_button(False, action)
    def get_error_message(self,res):
        data=res.json()
        return data["non_field_errors"][0]