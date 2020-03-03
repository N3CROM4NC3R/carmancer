"""Autos admin configure."""

#Django's imports
from django.contrib import admin


#Local's imports

from autos.models import Auto

class AutoAdmin(admin.ModelAdmin):
    list_display = ['nombre','modelo']

admin.site.register(Auto,AutoAdmin)
