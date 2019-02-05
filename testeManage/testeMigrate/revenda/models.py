from django.db import models

from django.utils import timezone

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


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)


class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile, on_delete=None)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
