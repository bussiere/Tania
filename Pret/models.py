from datetime import datetime
from django.db import models
from couchdbkit.ext.django.schema import *

# Create your models here.


class Pret(Document):
    Preteur = ListProperty()
    Emprunteur = ListProperty()
    Item = ListProperty()
    DatePret = ListProperty()
    DateRetour = ListProperty()
    Note =  ListProperty()
    Tags =  ListProperty()