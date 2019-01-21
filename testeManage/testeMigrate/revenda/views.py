from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from veiculo.models import Veiculo

from .models import Revenda


def index(request):
    return render(request,"revenda/index.html", {'title':'Bem Vindo ao app Revenda carrros gustavo pereira'})
    #return render(request,"layout/layout.html", {'title':'Bem Vindo ao app Revenda gustavo pereira'})


def ativos(request):
    veiculos = Veiculo.seminovos.all()
    return render(request,"revenda/ativos.html", {'veiculos':veiculos})


class RevendaDetailView(DetailView):
    model = Revenda
    slug_field = 'slug'
