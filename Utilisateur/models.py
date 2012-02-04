from datetime import datetime
from Droit.models import  *
from couchdbkit.ext.django.schema import *


class Groupe(Document):
    Nom = StringProperty()
    Users = ListProperty()
    Droits = ListProperty()
class Utilisateur(Document):
    User = StringProperty()
    Surnom = StringProperty()
    Contact = ListProperty()
    Liens = ListProperty()
    Groupe = ListProperty()
    Droits = ListProperty()
