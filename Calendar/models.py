from datetime import datetime
from django.db import models

from couchdbkit.ext.django.schema import *
#a developper


class Date(Document):
    Date = DateTimeProperty()
    

class Minute(Document):
    Minute = StringProperty(required=True)
    
class Heure(Document):
    Heure = StringProperty(required=True)
    
class HoraireDebut(Document):
    Minute = ListProperty()
    Heure = ListProperty()


class HoraireFin(models.Model):
    Minute = ListProperty()
    Heure = ListProperty()







class Horaire(models.Model):
    HoraireDebut = ListProperty()
    HoraireFin = ListProperty()







class Lundi(models.Model):

    HoraireDebut = ListProperty()
    HoraireFin = ListProperty()
    Note = ListProperty()
    Date = ListProperty()







class Mardi(models.Model):
    HoraireDebut = ListProperty()
    HoraireFin = ListProperty()
    Note = ListProperty()
    Date = ListProperty()


    



class Mercredi(models.Model):
    HoraireDebut = ListProperty()
    HoraireFin = ListProperty()
    Note = ListProperty()
    Date = ListProperty()





class Jeudi(models.Model):


    HoraireDebut = ListProperty()
    HoraireFin = ListProperty()
    Note = ListProperty()
    Date = ListProperty()






class Vendredi(models.Model):

    HoraireDebut = ListProperty()
    HoraireFin = ListProperty()
    Note = ListProperty()
    Date = ListProperty()






class Samedi(models.Model):

    HoraireDebut = ListProperty()
    HoraireFin = ListProperty()
    Note = ListProperty()
    Date = ListProperty()





class Dimanche(models.Model):

    HoraireDebut = ListProperty()
    HoraireFin = ListProperty()
    Note = ListProperty()
    Date = ListProperty()






class Ouverture(models.Model):



    Lundi = models.ManyToManyField('Lundi',null=True,blank=True)



    Mardi = models.ManyToManyField('Mardi',null=True,blank=True)



    Mercredi = models.ManyToManyField('Mercredi',null=True,blank=True)



    Jeudi = models.ManyToManyField('Jeudi',null=True,blank=True)



    Vendredi = models.ManyToManyField('Vendredi',null=True,blank=True)



    Samedi = models.ManyToManyField('Samedi',null=True,blank=True)



    Dimanche = models.ManyToManyField('Dimanche',null=True,blank=True)



    Note = models.ManyToManyField('note.Note_divers',related_name='Ouverture_Note_notes_Note_divers',null=True,blank=True)



    Notation = models.ManyToManyField('note.Note_divers',related_name='Ouverture_Notation_notes_Note_divers',null=True,blank=True)






