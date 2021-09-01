from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class resourceRestaurant (resources.ModelResource):
    class Meta:
        model = restaurant

class adminRestaurant(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['saucer']
    list_display = ['saucer']
    resource_class = resourceRestaurant

admin.site.register(restaurant, adminRestaurant)

class resourceProduct (resources.ModelResource):
    class Meta:
        model = product

class adminProduct(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_product']
    list_display = ['pk_product', 'code', 'saucer','description', 'price', 'fk_restaurant']
    resource_class = resourceProduct

admin.site.register(product, adminProduct)