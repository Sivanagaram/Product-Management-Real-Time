from django.contrib import admin
from .models import products

# Register your models here.
class productsAdmin(admin.ModelAdmin):
    list_display=('id','name','price','company','is_available','description','released_on',)
    list_display_links=('id','name','price',)
    list_filter=('price','is_available',)
    list_editable=('is_available',)
    search_fields=('name','price',)
    ordering=('id',)

admin.site.register(products, productsAdmin)