from datetime import datetime
from django.db import models
from couchdbkit.ext.django.schema import *

class AbreviationLangue(models.Model):
    Nom = StringProperty(required=True)
    Abreviation = StringProperty(required=True)

class Langue(models.Model):
    Nom = StringProperty(required=True)
    Abreviation = ListProperty() 
    Pays = ListProperty()
    def ___str__(self):
    	return self.Nom

    def __unicode__(self):
        return self.Nom


class Categorie_Texte(models.Model):
    Nom = StringProperty()
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom


class Texte(models.Model):
    Nom = StringProperty()
    Description = StringProperty()
    Texte = ListProperty()
    Langue = ListProperty()
    Categorie = ListProperty()
    Visibilite = ListProperty()
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom


class Couleur(models.Model):
    Nom = StringProperty()
    CodeHexa = StringProperty()
    def ___str__(self):
    	return self.Nom

    def __unicode__(self):
        return self.Nom

class Categorie_code(models.Model):
    Nom = StringProperty()
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom


class Code(models.Model):
    Categorie = ListProperty()
    Nom = StringProperty()
    Code = StringProperty()
    Couleur = ListProperty()
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom


class StyleCss(models.Model):
    Nom = StringProperty()
    Code = ListProperty()
    Couleur  = ListProperty()
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom





class MiseEnForme(models.Model):
    Nom = StringProperty()
    StyleCss = ListProperty()
    Code = ListProperty()



    def ___str__(self):
    	return self.Nom



    def __unicode__(self):
        return self.Nom



class Categorie_Texte_contenu(models.Model):
    Nom = StringProperty()



    def ___str__(self):
    	return self.Nom



    def __unicode__(self):
        return self.Nom


class Texte_contenu(models.Model):
    Categorie = ListProperty()
    nom = StringProperty()
    Texte = ListProperty()
    MiseEnForme = ListProperty()
    def ___str__(self):
    	return self.Nom

    def __unicode__(self):
        return self.Nom



class Categorie_ImageSite(models.Model):
      Nom = StringProperty()



class ImageSite(models.Model):
    Image = StringProperty()
    Categorie = ListProperty()
    Nom = StringProperty()
    Creation = DateTimeProperty()
    Tag = ListProperty()
    FamilleTag = ListProperty()
    Type = StringProperty()
    Description_courte = StringProperty()
    Description = StringProperty()
    Texte_contenu = ListProperty()
    Lien = ListProperty()








class Item_Menu(models.Model):
    Nom = StringProperty()
    Lien = ListProperty()
    Images = ListProperty()
    Texte_contenu = ListProperty()
    MiseEnForme = ListProperty()




class Menu(models.Model):
	Nom = StringProperty()
	Lien = ListProperty()
	Images = ListProperty()
	Texte_contenu = ListProperty()
	MiseEnForme = ListProperty()
	Item = ListProperty()




