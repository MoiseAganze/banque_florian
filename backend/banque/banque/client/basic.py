

import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit, 
                             QHBoxLayout, QPushButton, QLabel, QSpacerItem, 
                             QSizePolicy, QDialog, QApplication)

class FenetreInscription(QDialog):
    def __init__(self):
        super().__init__()

        # Définir la fenêtre avec des couleurs violet dégradé
        self.setWindowTitle("Inscription Utilisateur")
        self.setFixedSize(600, 700)  # Taille de la fenêtre
        self.setStyleSheet("""
            background: linear-gradient(to bottom, #8E44AD, #9B59B6, #8E44AD);
            font-family: 'Arial', sans-serif;
            color: white;
        """)

        # Créer les champs de formulaire
        self.nom_complet = QLineEdit()
        self.email = QLineEdit()
        self.telephone = QLineEdit()
        self.adresse = QLineEdit()
        self.mot_de_passe = QLineEdit()
        self.mot_de_passe.setEchoMode(QLineEdit.Password)

        # Styliser les champs de texte avec des bordures arrondies et des tailles agrandies
        champ_style = """
            QLineEdit {
                border: 2px solid #BDC3C7;
                border-radius: 15px;
                padding: 15px;
                font-size: 16px;
                background-color: #ECF0F1;
                color: #34495E;
            }
            QLineEdit:focus {
                border-color: #9B59B6;
                background-color: #ffffff;
            }
        """
        self.nom_complet.setStyleSheet(champ_style)
        self.email.setStyleSheet(champ_style)
        self.telephone.setStyleSheet(champ_style)
        self.adresse.setStyleSheet(champ_style)
        self.mot_de_passe.setStyleSheet(champ_style)

        # Ajouter des placeholders descriptifs pour chaque champ
        self.nom_complet.setPlaceholderText("Entrez votre nom complet (Prénom Nom)")
        self.email.setPlaceholderText("Entrez votre adresse email (ex: exemple@domain.com)")
        self.telephone.setPlaceholderText("Entrez votre numéro de téléphone (ex: +33 612 345 678)")
        self.adresse.setPlaceholderText("Entrez votre adresse complète")
        self.mot_de_passe.setPlaceholderText("Entrez un mot de passe sécurisé")

        # Bouton pour soumettre le formulaire avec un style moderne
        self.bouton_soumettre = QPushButton("S'inscrire")
        self.bouton_soumettre.setStyleSheet("""
            QPushButton {
                background-color: #9B59B6;
                color: white;
                border-radius: 25px;
                font-size: 18px;
                padding: 20px;
                border: none;
                min-width: 250px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #8E44AD;
                transition: 0.3s;
            }
            QPushButton:pressed {
                background-color: #5E3370;
            }
        """)
        self.bouton_soumettre.clicked.connect(self.soumettre_formulaire)

        # Layout principal
        layout_principal = QVBoxLayout()

        # Titre de la fenêtre
        titre_label = QLabel("Inscrire")
        titre_label.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: white;
                text-align: center;
                margin-bottom: 30px;
                text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
            }
        """)
        layout_principal.addWidget(titre_label)

        # Formulaire avec les champs et labels
        formulaire = QFormLayout()
        formulaire.addRow(self.create_label("Nom complet:"), self.nom_complet)
        formulaire.addRow(self.create_label("Email:"), self.email)
        formulaire.addRow(self.create_label("Téléphone:"), self.telephone)
        formulaire.addRow(self.create_label("Adresse:"), self.adresse)
        formulaire.addRow(self.create_label("Mot de passe:"), self.mot_de_passe)

        # Ajouter une espace pour centrer le bouton
        espace = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout_principal.addItem(espace)

        # Ajouter les éléments au layout principal
        layout_principal.addLayout(formulaire)
        layout_principal.addWidget(self.bouton_soumettre)

        # Centrer le formulaire dans la fenêtre
        self.setLayout(layout_principal)
        self.center_window()

    def create_label(self, text):
        """Crée un label stylisé pour chaque champ avec des tailles et des couleurs bien distinctes"""
        label = QLabel(text)
        label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #ECF0F1;
                margin-bottom: 10px;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            }
        """)
        return label

    def soumettre_formulaire(self):
        """Envoyer les données du formulaire au serveur via une requête POST."""
        # Récupérer les valeurs des champs
        nom_complet = self.nom_complet.text()
        email = self.email.text()
        telephone = self.telephone.text()
        adresse = self.adresse.text()
        mot_de_passe = self.mot_de_passe.text()

        # Valider les champs
        if not nom_complet or not email or not telephone or not adresse or not mot_de_passe:
            self.afficher_message("Erreur", "Tous les champs doivent être remplis.")
            return

        # Créer un dictionnaire avec les données
        data = {
            "nom_complet": nom_complet,
            "email": email,
            "telephone": telephone,
            "adresse": adresse,
            "mot_de_passe": mot_de_passe
        }

        # URL de l'API où l'inscription sera envoyée
        url = "http://127.0.0.1:8000/inscription/"  # Remplacez cette URL par l'URL réelle de votre API

        try:
            # Effectuer la requête POST pour soumettre les données
            response = requests.post(url, json=data)
            
            # Si la requête a réussi
            if response.status_code == 201:
                self.afficher_message("Succès", "Inscription réussie!")
                self.reset_formulaire()
            else:
                self.afficher_message("Erreur", "Problème lors de l'inscription. Veuillez réessayer.")
        except requests.exceptions.RequestException as e:
            self.afficher_message("Erreur", f"Erreur de connexion: {str(e)}")

    def afficher_message(self, titre, message):
        """Afficher un message d'information ou d'erreur."""
        from PyQt5.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information if titre == "Succès" else QMessageBox.Critical)
        msg.setWindowTitle(titre)
        msg.setText(message)
        msg.exec_()

    def reset_formulaire(self):
        """Réinitialiser tous les champs du formulaire."""
        self.nom_complet.clear()
        self.email.clear()
        self.telephone.clear()
        self.adresse.clear()
        self.mot_de_passe.clear()

    def center_window(self):
        """Centre la fenêtre sur l'écran."""
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# Lancer l'application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = FenetreInscription()
    fenetre.show()
    sys.exit(app.exec_())
