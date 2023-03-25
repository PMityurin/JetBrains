from django.contrib import admin
from .models import New_File, Result

# Register your models here.


class New_FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'description')
    list_display_links = ('id', 'file')
    search_fields = ('id', 'file')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'new_file_id')
    search_fields = ('id', 'result', 'new_file_id')

admin.site.register(New_File, New_FileAdmin)
admin.site.register(Result, ResultAdmin)

