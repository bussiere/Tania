from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *
#a developper

    
class HoraireDebut(Document):
    Minute = ListProperty()
    Heure = ListProperty()
    Horaire = ListProperty()


class HoraireFin(models.Model):
    Minute = ListProperty()
    Heure = ListProperty()


class Date(Document):
    Date = DateTimeProperty()
    
    
class Rdv(Document):
    Utilisateur = ListProperty()
    Personne = ListProperty()
    Note = ListProperty()
    Tags = ListProperty()
    Date = ListProperty()
    
class Minute(Document):
    Minute = StringProperty(required=True)
    
class Heure(Document):
    Heure = StringProperty(required=True)

class Horaire(models.Model):
    HoraireDebut = ListProperty()
    HoraireFin = ListProperty()

class Lundi(models.Model):
    Horaire = ListProperty()
    Note = ListProperty()
    Date = ListProperty()


class Mardi(models.Model):
    Horaire = ListProperty()
    Note = ListProperty()
    Date = ListProperty()


class Mercredi(models.Model):
    Horaire = ListProperty()
    Note = ListProperty()
    Date = ListProperty()

class Jeudi(models.Model):
    Horaire = ListProperty()
    Note = ListProperty()
    Date = ListProperty()

class Vendredi(models.Model):
    Horaire = ListProperty()
    Note = ListProperty()
    Date = ListProperty()

class Samedi(models.Model):
    Horaire = ListProperty()
    Note = ListProperty()
    Date = ListProperty()

class Dimanche(models.Model):
    Horaire = ListProperty()
    Note = ListProperty()
    Date = ListProperty()

class Ouverture(models.Model):
    Lundi = ListProperty()
    Mardi = ListProperty()
    Mercredi = ListProperty()
    Jeudi = ListProperty()
    Vendredi = ListProperty()
    Samedi = ListProperty()
    Dimanche = ListProperty()
    Note = ListProperty()
    Notation = ListProperty()





