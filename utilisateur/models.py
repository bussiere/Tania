from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Utilisateur(models.Model):
    User = models.ForeignKey(User, unique=True,null=True,blank=True)
    Surnom = models.CharField(max_length=10000)
