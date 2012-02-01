
from django.db import models
from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *
        
class Note(Document):
    Nom = StringProperty(required=True)
    Creation = DateTimeProperty(default=datetime.utcnow)
    Texte = StringProperty(required=True)
    Tags = ListProperty()
    Membre = ListProperty()
    Lien = ListProperty()
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom
   

class SommeInitiale(models.Model):
    Montant = models.FloatField(max_length=400)
    Texte = models.ManyToManyField('texte.Texte')
    Utilisateur = models.ManyToManyField('utilisateur.Utilisateur', null=True, blank=True)

class Credit(models.Model):
     Montant = models.FloatField(max_length=400)
     Texte = models.ManyToManyField('texte.Texte')
     Utilisateur = models.ManyToManyField('utilisateur.Utilisateur', null=True, blank=True)


class Debit(models.Model):
     Montant = models.FloatField(max_length=400)
     Texte = models.ManyToManyField('texte.Texte')
     Utilisateur = models.ManyToManyField('utilisateur.Utilisateur', null=True, blank=True)

class Budget(models.Model):
    Utilisateur = models.ManyToManyField('utilisateur.Utilisateur', null=True, blank=True)
    SommeInitiale = models.ManyToManyField('SommeInitiale', null=True, blank=True)
    Credit = models.ManyToManyField('Credit', null=True, blank=True)
    Debit = models.ManyToManyField('Debit', null=True, blank=True)
