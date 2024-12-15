


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import re
from django.core.exceptions import ValidationError

class GestionUtilisateur(BaseUserManager) :
    def InscriptionUtlisateur(self,
                              email,
                              nom_complet,
                              telephone,
                              adresse,
                              mot_de_passe=None,
                              ) :
        email = self.normalize_email(email)
       
        utilisateur = self.model(
            email=email,
            nom_complet=nom_complet,
            telephone=telephone,
            adresse=adresse,
            mot_de_passe=mot_de_passe
        
        )
        utilisateur.set_password(mot_de_passe)
        utilisateur.save(using=self._db)
        
        return utilisateur
class InscriptionModel(AbstractBaseUser) :
    nom_complet = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=120)
    adresse = models.TextField()
    data_inscription = models.DateTimeField(auto_now_add=True)
    
    # le champ email j'utilise ça pour authentifier les users
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = "__all__"
    objects = GestionUtilisateur()
    
    def __str__(self):
        return self.nom_complet
