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
# admin.site.register(Icecream)

# from mptt.admin import MPTTModelAdmin


# class MenuItemAdmin(MPTTModelAdmin):
#     list_display = ['name', 'tree_id', 'level']

# admin.site.register(MenuItem, MenuItemAdmin)

@admin.register(Icecream)
class IcecreamAdmin(admin.ModelAdmin):
    list_display=['id','name','description','slug']
    prepopulated_fields={'slug':['name']}

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
 list_display = ['name', 'email', 'post', 'created', 'active']
 list_filter = ['active', 'created', 'updated']
 search_fields = ['name', 'email', 'body']
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')  # Customize displayed fields
    list_filter = ('status', 'created', 'publish', 'author')  # Add filters for better navigation
    search_fields = ('title', 'body')  # Add search functionality for these fields
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate the slug field based on the title
    raw_id_fields = ('author',)  # Use raw_id_fields for better performance if you have many authors
    date_hierarchy = 'publish'  # Add date-based navigation hierarchy
    ordering = ('status', 'publish')  # Define default ordering
