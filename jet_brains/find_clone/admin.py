from django.contrib import admin
from .models import New_File


class New_FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'description', 'result')
    list_display_links = ('id', 'file', 'description', 'result')
    search_fields = ('id', 'file', 'description', 'result')


admin.site.register(New_File, New_FileAdmin)


