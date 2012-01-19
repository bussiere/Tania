from django.db import models

# Create your models here.

class Item(models.Model):
     Nom = models.CharField(max_length=400)
     Texte = models.ManyToManyField('texte.texte')
     Debut = models.ManyToManyField('date.Date',related_name='debut', null=True, blank=True)
     Fin = models.ManyToManyField('date.Date',related_name='fin', null=True, blank=True)
     UtilisateurDonneur = models.ManyToManyField('utilisateur.Utilisateur',related_name='donneur', null=True, blank=True)
     UtilisateurReceveur = models.ManyToManyField('utilisateur.Utilisateur',related_name='receveur', null=True, blank=True)
