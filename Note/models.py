from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *
        
class Note(Document):
    Nom = StringProperty(required=True)
    Creation = DateTimeProperty(default=datetime.utcnow)
    Texte = StringProperty(required=True)
    Tags = ListProperty()
    Membre = ListProperty()
    Lien = ListProperty()
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom
   
   