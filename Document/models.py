from datetime import datetime
from django.db import models
from couchdbkit.ext.django.schema import *

class Partage(Document):
    Proprietaire = ListProperty()
    Emprunteur = ListProperty()
    
class TypeFile(Document):
    Nom = StringProperty(required=True)
    Tags = ListProperty()

class Path(Document):
    Path = StringProperty(required=True)

class DateCreation(Document):
    Date = DateTimeProperty()

class DateModification(Document):
    Date = DateTimeProperty()

class Proprietaire(Document):
    Utilisateur = ListProperty()

class File(Document):
    Nom = StringProperty(required=True)
    Tags = ListProperty()
    liens = ListProperty()
    Note = ListProperty()
    Path = ListProperty()
    TypeFile = ListProperty()
    Base64 = StringProperty()
    Extension = StringProperty()
    Droit = StringProperty()
    DateCreation = ListProperty()
    DateModification = ListProperty()
    Proprietaire = ListProperty()
    Visibilite = ListProperty()
    Pegi = ListProperty()
    
class ImageFile(Document):
    File = ListProperty()
    Hauteur = StringProperty()
    Largeur = StringProperty()
    dpi = StringProperty()
    Miniature = ListProperty()
    
class Video(Document):
    File = ListProperty()
    Hauteur = StringProperty()
    Largeur = StringProperty()
    dpi = StringProperty()
    Codec = StringProperty()
    Miniature =  ListProperty()
    
class Texte(Document):
    File = ListProperty()
    Apercus = StringProperty()
    Contenu = StringProperty()
    
class Programmation(Document):
    File = ListProperty()
    Texte = ListProperty()
    Commande = ListProperty()
    
class Torrent(Document):
    File = ListProperty()
    Liens = ListProperty()