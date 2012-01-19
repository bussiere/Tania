from django.db import models

# Create your models here.

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
