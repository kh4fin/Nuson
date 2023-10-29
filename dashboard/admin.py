from django.contrib import admin
from .models import Nuson

class NusonAdmin(admin.ModelAdmin):
    site_header = "Nuson Admin Area"
    list_display = ('id', 'nilai1', 'nilai2', 'nilai3', 'nilai4', 'nilai5', 'deviceName', 'waktu')

admin.site.register(Nuson, NusonAdmin)
