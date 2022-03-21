from django.contrib import admin

from profesionales.models import Administrativo, Freelance, Marketing, Permanente

admin.site.register(Marketing)
admin.site.register(Permanente)
admin.site.register(Freelance)
admin.site.register(Administrativo)
