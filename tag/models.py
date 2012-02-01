from django.db import models
from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *
# Create your models here.
class Tag(Document):
    Nom = StringProperty(required=True)
    Creation = DateTimeProperty(default=datetime.utcnow)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom

class FamilleTag(Document):
    Nom = StringProperty(required=True)
    Tags = ListProperty()
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom
