from django.db import models




from django.db import models
from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *

class GPSLien(Document):
    Lien = ListProperty()

class GeoHash(Document):
    GeoHash = StringProperty()

class Metro(Document):
    Ligne = StringProperty()


class Type_Telephone(Document):
    Nom = StringProperty(required=True)
    
    
class Telephone(Document):
    Tel = StringProperty(required=True)
    Type = ListProperty()
    
    

class Adresse(Document):
    Nom = StringProperty(required=True)
    AD1 = StringProperty()
    AD2 = StringProperty()
    AD3 = StringProperty()
    AD4 = StringProperty()
    AD5 = StringProperty()
    AD6 = StringProperty()
    Creation = DateTimeProperty(default=datetime.utcnow)
    Tags = ListProperty()
    Membre = ListProperty()
    Lien = ListProperty()
    Metro = ListProperty()
    GpsLiens =  ListProperty()
    GeoHash = ListProperty()
    Private = BooleanProperty()
    Note = StringProperty(required=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom
# Create your models here.
