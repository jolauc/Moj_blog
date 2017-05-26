from django.contrib import admin

from .models import Category
from .models import News

from django.contrib import admin

from news.models import *

#admin.site.register(Category)
#admin.site.register(News)




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'posted_date']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)


# Register your models here.
