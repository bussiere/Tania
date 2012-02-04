from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *
# Create your models here.
class Categorie_Tips(models.Model):
    Nom = StringProperty()


class Tips(models.Model):
    Nom = StringProperty()
    Texte = ListProperty()
    Membre = ListProperty()
    Lien =  ListProperty()
    Adresse = ListProperty()
    tag = ListProperty()
    Visibilite = ListProperty()
    Proprietaire = ListProperty()
