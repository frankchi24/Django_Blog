from django.contrib import admin
from .models import Script_Tag, Script
# Register your models here.


class ScriptAdmin(admin.ModelAdmin):
    list_display = ('scripts','position','epi_number','season','show_name')
    search_fields = ('scripts', 'show_name')



admin.site.register(Script_Tag)
admin.site.register(Script,ScriptAdmin)
