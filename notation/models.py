from datetime import datetime
from django.db import models
from couchdbkit.ext.django.schema import *

class Proprietaire(Document):
    Utilisateur = ListProperty()
# Create your models here.
class Notation(Document):
    Notedonne = FloatProperty(required=True)
    Proprietaire = ListProperty()