from django.contrib import admin
from .models import Profile, Programa


admin.site.register(Profile)


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'facultad', 'estado')
    search_fields = ('codigo', 'nombre', 'facultad')