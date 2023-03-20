from django.contrib import admin
from .models import New_File

# Register your models here.


class New_FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file', 'check_done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'file')
    list_filter = ('check_done',)
    list_editable = ('check_done',)

admin.site.register(New_File, New_FileAdmin)

