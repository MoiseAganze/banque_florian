import os
import json

def ecrire_dans_fichier_json(chemin_fichier, contenu):

    repertoire = os.path.dirname(chemin_fichier)
    if not os.path.exists(repertoire):
        os.makedirs(repertoire)

    with open(chemin_fichier, 'w') as fichier:
        json.dump(contenu,fichier,indent=4)
