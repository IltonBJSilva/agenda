from django.contrib import admin
from core.models import Evento #importando os models

# Registros de models aqui


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento','data_criacao','data_evento','local_evento')
    list_filter = ('usuario','data_evento',)
admin.site.register(Evento,EventoAdmin) #registrando no banco


