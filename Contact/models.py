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
    
    

class Type_Email(Document):
    Nom = StringProperty(required=True)
    
    
class Email(Document):
    Email = StringProperty(required=True)
    Type = ListProperty()


class Rue(Document):
    Nom = StringProperty()
    Creation = DateTimeProperty(default=datetime.utcnow)
    Tags = ListProperty()
    Lien = ListProperty()
    Metro = ListProperty()
    GpsLiens =  ListProperty()
    GeoHash = ListProperty()
    
class CP(Document):
    CP = StringProperty()
    Creation = DateTimeProperty(default=datetime.utcnow)
    Tags = ListProperty()
    Lien = ListProperty()
    Metro = ListProperty()
    GpsLiens =  ListProperty()
    GeoHash = ListProperty() 

class Ville(Document):
    Ville = StringProperty()
    Creation = DateTimeProperty(default=datetime.utcnow)
    Tags = ListProperty()
    Lien = ListProperty()
    Metro = ListProperty()
    GpsLiens =  ListProperty()
    GeoHash = ListProperty()   
    
class Region(Document):
    Region = StringProperty()
    Creation = DateTimeProperty(default=datetime.utcnow)
    Tags = ListProperty()
    Lien = ListProperty()
    Metro = ListProperty()
    GpsLiens =  ListProperty()
    GeoHash = ListProperty()   

class Pays(Document):
    Pays = StringProperty()
    Creation = DateTimeProperty(default=datetime.utcnow)
    Tags = ListProperty()
    Lien = ListProperty()
    Metro = ListProperty()
    GpsLiens =  ListProperty()
    GeoHash = ListProperty()  
  
class Adresse(Document):
    Nom = StringProperty(required=True)
    Numero = StringProperty()
    Rue = ListProperty()
    AD2 = StringProperty()
    AD3 = StringProperty()
    AD4 = StringProperty()
    AD5 = StringProperty()
    AD6 = StringProperty()
    CP = ListProperty()
    Ville = ListProperty()
    Region = ListProperty()
    Pays = ListProperty()
    Creation = DateTimeProperty(default=datetime.utcnow)
    Tags = ListProperty()
    Lien = ListProperty()
    Metro = ListProperty()
    GpsLiens =  ListProperty()
    GeoHash = ListProperty()
    
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom
    
class Contact(Document):
    Nom = StringProperty(required=True)
    Adresse = ListProperty()
    Horaire = ListProperty()
    Tags = ListProperty()
    Private = BooleanProperty()
    Note = ListProperty()
    Creation = DateTimeProperty(default=datetime.utcnow)
    Email = ListProperty()
    Telephone = ListProperty()
    Horaire = ListProperty()
# Create your models here.
