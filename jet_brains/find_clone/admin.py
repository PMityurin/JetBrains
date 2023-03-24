from django.contrib import admin
from .models import New_File

# Register your models here.


class New_FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file', 'description')
    list_display_links = ('id', 'file')
    search_fields = ('id', 'file', 'title')

admin.site.register(New_File, New_FileAdmin)

