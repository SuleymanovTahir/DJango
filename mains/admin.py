from django.contrib import admin
from .models import *

admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Courses)
admin.site.register(Students)
# admin.site.register(Icecream)

from mptt.admin import MPTTModelAdmin


class MenuItemAdmin(MPTTModelAdmin):
    list_display = ['name', 'tree_id', 'level']

admin.site.register(MenuItem, MenuItemAdmin)

@admin.register(Icecream)
class IcecreamAdmin(admin.ModelAdmin):
    list_display=['id','name','description','slug']
    prepopulated_fields={'slug':['name']}
