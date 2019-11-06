from django.contrib import admin
from .models import Service,Item,Quantity



class QuantityAdmin(admin.ModelAdmin):
  list_display = [
      'author',
      'quantity',
      'item',
      'flat_number',
      'time1',
  ]



class ServiceAdmin(admin.ModelAdmin):
  list_display = [
      
      'aut',
      'flat_number',
      'created',
      'time',
  ]



class ItemAdmin(admin.ModelAdmin):
  list_display = [
      'item_name',
      'price',
      'brand',
     
  ]
  search_fields = ['author']
admin.site.register(Quantity, QuantityAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Item, ItemAdmin)