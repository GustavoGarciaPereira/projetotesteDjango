from django.db import models

from utils.gerador_hash import gerar_hash

from veiculo.models import Veiculo
# Create your models here.


class Revenda(models.Model):
    nome = models.CharField(max_length = 50)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True, null=True)

    def __str__(self):
    	return self.nome

    @property
    def veiculos_antigos(self):
    	return Veiculo.antigos.filter(revenda = self)

    @property
    def veiculos_seminovos(self):
    	return Veiculo.seminovos.filter(revenda = self)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gerar_hash()
        super(Revenda, self).save(*args, **kwargs)