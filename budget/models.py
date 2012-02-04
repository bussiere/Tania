from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *
        


class SommeInitiale(Document):
    Montant = FloatProperty(required=True)
    Texte1 = StringProperty(required=True)
    Texte2 = StringProperty(required=True)
    Texte3 = StringProperty(required=True)
    Texte4 = StringProperty(required=True)
    Creation = DateTimeProperty(default=datetime.utcnow)
    Echeance = DateTimeProperty(default=datetime.utcnow)
    Debiteur = ListProperty()
    Crediteur  = ListProperty()
    Proprietaire = ListProperty()
    Note = ListProperty()

class Credit(models.Model):
    Montant = FloatProperty(required=True)
    Texte1 = StringProperty(required=True)
    Texte2 = StringProperty(required=True)
    Texte3 = StringProperty(required=True)
    Texte4 = StringProperty(required=True)
    Creation = DateTimeProperty(default=datetime.utcnow)
    Echeance = DateTimeProperty(default=datetime.utcnow)
    Debiteur = ListProperty()
    Crediteur  = ListProperty()
    Proprietaire = ListProperty()
    Note = ListProperty()


class Debit(models.Model):
    Montant = FloatProperty(required=True)
    Texte1 = StringProperty(required=True)
    Texte2 = StringProperty(required=True)
    Texte3 = StringProperty(required=True)
    Texte4 = StringProperty(required=True)
    Creation = DateTimeProperty(default=datetime.utcnow)
    Echeance = DateTimeProperty(default=datetime.utcnow)
    Debiteur = ListProperty()
    Crediteur  = ListProperty()
    Proprietaire = ListProperty()
    Note = ListProperty()

class Budget(models.Model):
    Utilisateur = ListProperty()
    SommeInitiale = ListProperty()
    Credit = ListProperty()
    Debit = ListProperty()
    Note = ListProperty()
