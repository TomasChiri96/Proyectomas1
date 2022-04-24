from django.contrib import admin
from .models import mozo, mesas, almancen

# Register your models here.

admin.site.register(mozo)
admin.site.register(mesas)
admin.site.register(almancen)