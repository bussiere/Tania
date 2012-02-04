from django.db import models


class Langue(models.Model):
    Nom = models.CharField(max_length=400,null=True,blank=True)
    Abreviation = models.CharField(max_length=2,null=True,blank=True)
    def ___str__(self):
    	return self.Nom

    def __unicode__(self):
        return self.Nom







class Categorie_Texte(models.Model):
    Nom = models.CharField(max_length=400,null=True,blank=True)
    def ___str__(self):
    	return self.Nom


    def __unicode__(self):
        return self.Nom



    



class Texte(models.Model):
    Nom = models.CharField(max_length=400,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Texte = models.CharField(max_length=4000,null=True,blank=True)
    Langue = models.ManyToManyField(Langue,null=True,blank=True)
    Categorie = models.ManyToManyField(Categorie_Texte,null=True,blank=True)
    
    def ___str__(self):
    	return self.Nom



    def __unicode__(self):
        return self.Nom







class Couleur(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    CodeHexa = models.CharField(max_length=7,null=True,blank=True)



    



    def ___str__(self):
    	return self.Nom



    def __unicode__(self):
        return self.Nom



class Categorie_code(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    def ___str__(self):
    	return self.Nom

    def __unicode__(self):
        return self.Nom







class Code(models.Model):
    Categorie = models.ManyToManyField(Categorie_code,null=True,blank=True)
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Code = models.ManyToManyField(Texte,null=True,blank=True)
    Couleur = models.ManyToManyField(Couleur,null=True,blank=True)

    def ___str__(self):
    	return self.Nom



    def __unicode__(self):
        return self.Nom







class StyleCss(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Code = models.ManyToManyField(Code,null=True,blank=True)
    Couleur  = models.ManyToManyField(Couleur,null=True,blank=True)





    def ___str__(self):
    	return self.Nom



    def __unicode__(self):
        return self.Nom







class MiseEnForme(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    StyleCss = models.ManyToManyField(StyleCss,null=True,blank=True)
    Code = models.ManyToManyField(Texte,null=True,blank=True)



    def ___str__(self):
    	return self.Nom



    def __unicode__(self):
        return self.Nom







class Categorie_Texte_contenu(models.Model):
    Nom = models.CharField(max_length=400,null=True,blank=True)



    def ___str__(self):
    	return self.Nom



    def __unicode__(self):
        return self.Nom







class Texte_contenu(models.Model):
    Categorie = models.ManyToManyField(Categorie_Texte_contenu,null=True,blank=True)
    nom = models.CharField(max_length=200,null=True,blank=True)
    Texte = models.ManyToManyField(Texte,null=True,blank=True)
    MiseEnForme = models.ManyToManyField(MiseEnForme,null=True,blank=True)




    def ___str__(self):
    	return self.Nom



    def __unicode__(self):
        return self.Nom



	











class Categorie_ImageSite(models.Model):
      Nom = models.CharField(max_length=200,null=True,blank=True)


      











class ImageSite(models.Model):
    Base64 = models.CharField(max_length=1000000)
    Categorie = models.ManyToManyField(Categorie_ImageSite,null=True,blank=True)
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    Tag = models.ManyToManyField('tag.Tag',related_name='ImageSite_Tag_tags_Tag',null=True,blank=True)
    FamilleTag = models.ManyToManyField('tag.FamilleTag',related_name='ImageSite_FamilleTag_tags_FamilleTag',null=True,blank=True)
    Type = models.CharField(max_length=200,null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Image = models.FileField(upload_to='media',null=True,blank=True)
    Texte_contenu = models.ManyToManyField(Texte_contenu,null=True,blank=True)
    Lien = models.ManyToManyField('lien.Lien',related_name='ImageSite_lien',null=True,blank=True)








class Item_Menu(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Lien = models.ManyToManyField('lien.Lien',related_name='Item_Menu_Lien_liens_Lien',null=True,blank=True)
    Images = models.ManyToManyField(ImageSite,null=True,blank=True)
    Texte_contenu = models.ManyToManyField(Texte_contenu,null=True,blank=True)
    MiseEnForme = models.ManyToManyField(MiseEnForme,null=True,blank=True)







class Menu(models.Model):
	Nom = models.CharField(max_length=200,null=True,blank=True)
	Lien = models.ManyToManyField('lien.Lien',related_name='Menu_Lien_liens_Lien',null=True,blank=True)
	Images = models.ManyToManyField(ImageSite,null=True,blank=True)
	Texte_contenu = models.ManyToManyField(Texte_contenu,null=True,blank=True)
	MiseEnForme = models.ManyToManyField(MiseEnForme,null=True,blank=True)
	Item = models.ManyToManyField(Item_Menu,null=True,blank=True)




