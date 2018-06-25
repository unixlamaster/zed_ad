from django.db import models

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