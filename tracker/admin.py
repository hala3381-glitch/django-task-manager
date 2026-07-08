from django.contrib import admin
from .models import Goals

# Register your models here.

admin.site.register(Goals)
admin.site.site_header = 'habit tracker'