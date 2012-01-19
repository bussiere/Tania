from django.db import models

# Create your models here.
class Tag(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom

class FamilleTag(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Tag = models.ManyToManyField(Tag)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom
