


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import re
import uuid
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError

class GestionUtilisateur(BaseUserManager) :
    def envoi_email_confirmation(self, email_utilisateur) :
        """
       ici je veux envoyer un code à 6 caracteres a l email de user pour confirmer que son email existe
        """
        code_confirmation = str(uuid.uuid4().int)[:6] # a 6 caracteres
        expiration = timezone.now()+timedelta(minutes=5) # le code est valide pendant 5 minutes
        
        confirmation  = EmailConfirmer.objects.create(
            email = email_utilisateur,
            code=code_confirmation,
            expirated_at = expiration
            
        )
        
        # envoie d email
        send_mail(
            'Code de confirmation pour votre confirmation \n',
            f"Votre code de confirmation est  :({code_confirmation})\n",
            "floriandiangongo22@gmail.com\n",
            [email_utilisateur],
            fail_silently=False
        )
    def verifier_code_confirmation(self, email_utilisateur, code_saisi) :
        
        """
        je verifie si le code de confirmation est valide
        """
        try :
            confirmation = EmailConfirmer.objects.get(email=email_utilisateur,code=code_saisi)
            if confirmation.expirated_at < timezone.now() :
                raise ValidationError('le code de confirmation est expiré ! ')
            confirmation.delete()
            return True
        
        except EmailConfirmer.DoesNotExist :
            raise ValidationError("le code de confirmation est invalide !")
        
            
    def InscriptionUtlisateur(self,
                              email,
                              nom_complet,
                              telephone,
                              adresse,
                              mot_de_passe=None,
                              code_confirmation=None) :
        if email is None :
            raise ValueError("l'email est obligatoire ")
        if telephone is None:
            raise ValueError("le numero de téléphone est obligatoire ")
        if mot_de_passe is None :
            raise ValueError("l'utilisateur doit avoir un mot de passe ")
        if len(mot_de_passe) < 6 :
            raise ValueError("le mot de passe doit avoir au moins 6 caracteres ")
        if not re.search(r"[A-Za-z]", mot_de_passe) :
            raise ValueError("le mot de passe doit contenir au moins une lettre ")
        if not re.search(r"[0-9]", mot_de_passe) :
            raise ValueError('le mot de passe doit avoir au moins un chiffre ')
        if not re.search(r"[@$!%*?&]", mot_de_passe) :
            raise ValueError("le mot de passe doit avoir un caractere special ")
        
        email = self.normalize_email(email)
        if not code_confirmation is None:
            raise ValueError("le code de validation est neccessaire pour valider l'incription")
        self.verifier_code_confirmation(code_saisi=code_confirmation,
                                        email_utilisateur=email)
        
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
class EmailConfirmer(models.Model) :
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6, unique=True)
    expirated_at = models.DateTimeField()
    
    def __str__(self):
        return f"Confirmation de ({self.email})  avec le code ({self.code})"