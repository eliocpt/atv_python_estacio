from django.contrib import admin

from .models import Paciente, Anamnese, Sessao

admin.site.register(Paciente)
admin.site.register(Anamnese)
admin.site.register(Sessao)