from django.contrib import admin
from .models import Catagory
from .models import Product
 

#class CatagoryAdmin(admin.ModelAdmin):
   # list_display=('name','image','description')
    
admin.site.register(Catagory)#,CatagoryAdmin
admin.site.register(Product)
 