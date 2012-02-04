from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *

class CategorieLien(Document):
    Nom =  StringProperty()
    Visibilite = ListProperty()


class Lien(models.Model):
    Categorie = ListProperty()
    Note = ListProperty()
    Tags = ListProperty()
    Nom = StringProperty()
    url = StringProperty()
    alt = StringProperty()
    Texte_contenu = StringProperty()
    MiseEnForme = StringProperty()
    Visibilite = ListProperty()

class LienFacebook(models.Model):
    LienFacaebook = ListProperty()

class LienTwitter(models.Model):
    LienTwitter = ListProperty()


