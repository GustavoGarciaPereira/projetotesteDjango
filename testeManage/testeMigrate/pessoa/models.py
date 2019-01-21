from django.db import models




class Pessoa(models.Model):
    SEXOS = (
        ('M','Masculino'),
        ('F','Feminino')
        )

    nome = models.CharField(max_length = 50)
    sexo = models.CharField(max_length=1, choices = SEXOS, default = 'M')

    def __str__(self):
        return self.nome


