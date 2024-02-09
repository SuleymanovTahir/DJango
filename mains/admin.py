from django.contrib import admin
from .models import *

# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Courses)
admin.site.register(Students)
<<<<<<< HEAD
# admin.site.register(Icecream)

from mptt.admin import MPTTModelAdmin


class MenuItemAdmin(MPTTModelAdmin):
    list_display = ['name', 'tree_id', 'level']

admin.site.register(MenuItem, MenuItemAdmin)

@admin.register(Icecream)
class IcecreamAdmin(admin.ModelAdmin):
    list_display=['id','name','description','slug']
    prepopulated_fields={'slug':['name']}
=======

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    # list_display='name','created','updated','publish',
    # # readonly_fields=('created','updated',)
    # fieldsets=(('1',{
    #     # 'fields':('created',)
    # }),
    # ('2',{'fields':('publish',)}),
    # ('3',{'fields':('name','updated',)}))
    
@admin.register(Icecream)
class IcecreamAdmin(admin.ModelAdmin):
    pass

>>>>>>> 1a650661f41c000c90c55023eb10a39d4bc66ffe
