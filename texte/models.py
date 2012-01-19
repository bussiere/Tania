from django.db import models

# Create your models here.

class Categorie_Texte(models.Model):
    Nom = models.CharField(max_length=400)

class Lien(models.Model):
    nom = models.CharField(max_length=1000,null=True, blank=True)
    url = models.CharField(max_length=10000)
    tag = models.ManyToManyField('tag.Tag')
    

class Texte(models.Model):
    Nom = models.CharField(max_length=400)
    Texte = models.CharField(max_length=10000)
    Membre = models.ManyToManyField('utilisateur.Utilisateur', null=True, blank=True)
    Lien =  models.ManyToManyField('Lien')
    Geohash = models.CharField(max_length=1000)
    tag = models.ManyToManyField('tag.Tag')
