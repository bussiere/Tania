from django.db import models

# Create your models here.



class Note(models.Model):
    Nom = models.CharField(max_length=400)
    Texte = models.ManyToManyField('texte.Texte')
    Membre = models.ManyToManyField('utilisateur.Utilisateur', null=True, blank=True)
    tag = models.ManyToManyField('tag.Tag')
