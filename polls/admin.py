from django.contrib import admin
from .models import Preguntas

admin.site.register(Preguntas)
admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Bienvenido al area de pollster'