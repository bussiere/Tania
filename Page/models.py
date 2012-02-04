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
	contenu = StringProperty(required=True)
	def ___str__(self):
		return self.Nom
	def __unicode__(self):
		return self.Nom



class Page(models.Model):
    Template = ListProperty()
    self_url = ListProperty()
    Categorie = ListProperty()
    Liens = ListProperty()
    Nom = StringProperty()
    ImagesSite = ListProperty()
    Texte_contenu = ListProperty()
    MiseEnForme = ListProperty()
    Menu = ListProperty()
    generated = DateTimeProperty()
    modified = DateTimeProperty()
    protege =  BooleanProperty(required=True)
    Visibilite = ListProperty()
    PEGI = ListProperty()
    

    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

class Admin:
    pass

