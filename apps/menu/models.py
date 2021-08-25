from django.db import models

# Create your models here.
class restaurant(models.Model):
    pk_restaurant = models.AutoField(primary_key=True, null=False, blank=False)
    saucer = models.CharField(max_length=50, null=False, blank=False)
    invoice = models.TextField(null=False, blank=False)
    employee = models.CharField(max_length=50, null=False, blank=False)
    client = models.CharField(max_length=50, null=False, blank=False)
    direction = models.CharField(max_length=100, null=False, blank=False)

class product(models.Model):
    pk_product = models.AutoField(primary_key=True, null=False, blank=False)
    code = models.IntegerField(null=False, blank=False)
    saucer = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(null=False, blank=False, max_digits=3, decimal_places=2)
    fk_restaurant = models.ForeignKey(restaurant, null=False, blank=False, on_delete=models.CASCADE)

