from django.contrib import admin

# Register your models here.
from .models import Revenda
from veiculo.models import Veiculo 

class VeiculoInline(admin.TabularInline):
    model = Veiculo

class RevendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'is_active']
    search_fields = ['nome']
    inlines = [VeiculoInline]


admin.site.register(Revenda, RevendaAdmin)