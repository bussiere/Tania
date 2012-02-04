from django.db import models







# Create your models here.



Visible = (



    (1, 'Root_aucun'),



    (2, 'Admin_Admin'),



    (3, 'Membre_Aucun'),



    (4, 'Membre_Amis'),



    (5, 'Membre_Amis_Amis'),



    (6, 'Tous')



)







class Visibilite(Document):
	Proprietaire = ListProperty()
    Groupe = ListProperty()
    Droit = ListProperty()
    Visibilite = IntegerProperty()


class Admin:
    pass
