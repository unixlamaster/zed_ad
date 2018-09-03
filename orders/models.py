from django.db import models
from catalog.models import User,Price,Provider

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    status = models.CharField(max_length=128)
    create_date = models.DateField(auto_now=True)
    update = models.DateField(null=True)
    summa_invoice = models.FloatField(null=False, blank=False, default=0.0)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,)
    priceitem = models.ForeignKey(Price,on_delete=models.DO_NOTHING,)
    cost = models.FloatField(null=False, blank=False, default=0.0)
    count = models.IntegerField(null=False, blank=False, default=0)
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING)
    nomenclature = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    articul = models.CharField(max_length=50)    