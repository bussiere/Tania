from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *

class TypeItem(Document):
    Type = StringProperty(required=True)
    Tags = ListProperty()

class Categorie1(Document):
    Type = StringProperty(required=True)
    Tags = ListProperty()
    
class Categorie2(Document):
    Type = StringProperty(required=True)
    Tags = ListProperty()
    
class Categorie3(Document):
    Type = StringProperty(required=True)
    Tags = ListProperty()

class Magasins(Document):
    Contact = ListProperty()
    Liens = ListProperty()
    
class Prix(Document):
    Prix =  FloatProperty(required=True)
    Magasin = ListProperty()
    
class Cote(Document):
    Prix =  FloatProperty(required=True)
    Magasin = ListProperty()

class CodeBarre(Document):
    Code = StringProperty(required=True)
    
class ISBN(Document):
    Code = StringProperty(required=True)
    
class Description(Document):
    Type = StringProperty(required=True)
    Tags = ListProperty()
    
class Proprietaire(Document):
    Utilisateur = ListProperty()
    
class Item(Document):
    Nom = StringProperty(required=True)
    Tags = ListProperty()
    Note =  ListProperty()
    TypeItem = ListProperty()
    Proprietaire = ListProperty()
    Categorie1 = ListProperty()
    Categorie2 = ListProperty()
    Categorie3 = ListProperty()
    Magasins = ListProperty()
    Liens = ListProperty()
    Prix = ListProperty()
    Cote = ListProperty()
    CodeBarre = ListProperty()
    ISBN = ListProperty()
    Description = ListProperty()
    
    