from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class resourceRestaurant (resources.ModelResource):
    class Meta:
        model = restaurant

class adminRestaurant(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'direction', 'phone', 'owner']
    resource_class = resourceRestaurant

admin.site.register(restaurant, adminRestaurant)

class resourceProduct (resources.ModelResource):
    class Meta:
        model = product

class adminProduct(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_product']
    list_display = ['pk_product', 'saucer','description', 'price', 'fk_tipo_producto']
    resource_class = resourceProduct

admin.site.register(product, adminProduct)

class resourceTipo (resources.ModelResource):
    class Meta:
        model = tipo_producto

class adminTipo(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_tipo_producto']
    list_display = ['pk_tipo_producto','nombre', 'descripcion']
    resource_class = resourceTipo

admin.site.register(tipo_producto, adminTipo)
