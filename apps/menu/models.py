from django.db import models

# Create your models here.
class restaurant(models.Model):
    pk_restaurant = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    direction = models.CharField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    owner = models.CharField(max_length=50, null=False, blank=False)

class tipo_producto(models.Model):
    pk_tipo_producto = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)

class product(models.Model):
    pk_product = models.AutoField(primary_key=True, null=False, blank=False)
    saucer = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.URLField(max_length=8000, blank=False, null=False, default='https://d1uz88p17r663j.cloudfront.net/resized/D60D6F76-811C-6377-B9D8-FF0000673B69-500x295-b-principal_1200_600.png')
    fk_tipo_producto = models.ForeignKey(tipo_producto, null=False, blank=False, on_delete=models.CASCADE)



