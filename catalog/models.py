from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from datetime import datetime

# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=100)
    site = models.CharField(max_length=1024)
    discount = models.FloatField(null=False, blank=False, default=0.0)
    urlprice = models.CharField(max_length=2048)
    update = models.DateField(null=True)
    
class Price(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.DO_NOTHING)
    nomenclature = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    articul = models.CharField(max_length=50)
    describe = models.CharField(max_length=2048)
    multi = models.IntegerField(null=False, blank=False, default=0)
    cost = models.FloatField(null=False, blank=False, default=0.0)
    availability = models.IntegerField(null=False, blank=False, default=0)
    delivery = models.IntegerField(null=False, blank=False, default=0)
    catnumber = models.CharField(max_length=50)
    oemnumber = models.CharField(max_length=2048)

class UserSession(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    session = models.ForeignKey(Session,on_delete=models.CASCADE,)
    create_date = models.DateField(auto_now=True)