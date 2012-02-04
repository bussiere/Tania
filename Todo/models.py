from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import * 

class Todo(models.Model):
     Nom = StringProperty()
     DateCreation = DateTimeProperty()
     Texte = ListProperty()
     Debut = ListProperty()
     Fin = ListProperty()
     UtilisateurDonneur = ListProperty()
     UtilisateurReceveur = ListProperty()
     Createur = ListProperty()