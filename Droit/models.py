
from datetime import datetime
from django.db import models
from couchdbkit.ext.django.schema import *






# Create your models here.



Visible = (



    (1, 'Root_aucun'),



    (2, 'Admin_Admin'),



    (3, 'Membre_Aucun'),



    (4, 'Membre_Amis'),



    (5, 'Membre_Amis_Amis'),



    (6, 'Tous')



)





class Droit(Document):
    Proprietaire = ListProperty()
    Groupe = ListProperty()
    Droit = StringProperty()
    

class Visibilite(Document):
    Proprietaire = ListProperty()
    Groupe = ListProperty()
    Droit = ListProperty()
    Visibilite = IntegerProperty()

class Admin:
    pass
