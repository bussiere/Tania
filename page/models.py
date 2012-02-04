from datetime import datetime
from django.db import models
from couchdbkit.ext.django.schema import *


class Categorie_Page(models.Model):
	Nom = StringProperty(required=True)
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom

class Template(models.Model):
	Nom = StringProperty(required=True)
	contenu = Nom = StringProperty(required=True)
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom



class Page(models.Model):
    Template = models.ManyToManyField(Template, null=True, blank=True)
    self_url = models.ManyToManyField('lien.Lien', related_name='pages_lien_self', null=True, blank=True)
    Categorie = models.ManyToManyField(Categorie_Page, null=True, blank=True)
    Liens = models.ManyToManyField('lien.Lien', related_name="Liens sur la page", null=True, blank=True)
    Nom = models.CharField(max_length=200)
    ImagesSite = models.ManyToManyField('presentation.ImageSite', related_name='ImagesSite_presentation_ImageSite', null=True, blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu', related_name='Texte_contenu_presentation_Texte_contenu', null=True, blank=True)
    MiseEnForme = models.ManyToManyField('presentation.MiseEnForme', related_name='MiseEnForme_presentation_MiseEnForme', null=True, blank=True)
    Menu = models.ManyToManyField('presentation.Menu', related_name='Menu_presentation_Menu', null=True, blank=True)
    generated = models.DateTimeField('date published', blank=True, null=True)
    modified = models.DateTimeField('date modified', blank=True, null=True)
    protege = models.BooleanField(blank=True)
    Visibilite = models.BooleanField(blank=True)

    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

class Admin:
    pass

