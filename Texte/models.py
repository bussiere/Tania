from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *

class Categorie_Texte(models.Model):
    Nom = StringProperty()


class Texte(models.Model):
    Nom = StringProperty()
    Texte = StringProperty()
    Membre = ListProperty()
    Lien =  ListProperty()
    Adresse = ListProperty()
    tag = ListProperty()
    Visibilite = ListProperty()
    Proprietaire = ListProperty()
    DateCreation = DateTimeProperty()

