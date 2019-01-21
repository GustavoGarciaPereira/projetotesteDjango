from django.db import models
from django.db.models import signals
from django.dispatch import receiver

from datetime import datetime
# Create your models here.

class VeiculoAtivoManager(models.Manager):
    def get_queryset(self):
        return super(VeiculoAtivoManager, self).get_queryset().filter(is_active=True)


class VeiculoInativoManager(models.Manager):
    def get_queryset(self):
        return super(VeiculoInativoManager, self).get_queryset().filter(is_active=False)        


class VeiculoAntigoManager(models.Manager):
    def get_queryset(self):
        ano_atual = datetime.now().year
        ano_atras = ano_atual - 20
        return super(VeiculoAntigoManager, self).get_queryset().filter(ano__lte = ano_atras)


class VeiculoSeminovoManager(models.Manager):
    def get_queryset(self):
        ano_atual = datetime.now().year
        ano_atras = ano_atual - 5
        return super(VeiculoSeminovoManager, self).get_queryset().filter(ano__gte = ano_atras)


class Veiculo(models.Model):
    revenda = models.ForeignKey('revenda.Revenda',on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    ativos = VeiculoAtivoManager()
    inativos = VeiculoInativoManager()
    antigos = VeiculoAntigoManager()
    seminovos = VeiculoSeminovoManager()

    def __str__(self):
        return '%s - %s' % (self.revenda.nome, self.nome)

###########################################################
@receiver(signals.pre_save, sender=Veiculo)
def create_customer(sender, instance, **kwargs):
    print("antes de salvar")