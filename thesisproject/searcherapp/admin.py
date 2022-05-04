from django.contrib import admin
from .models import *

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class StartupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Startup, StartupAdmin)
