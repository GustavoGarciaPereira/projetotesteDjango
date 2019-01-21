from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView


from .models import Pessoa


def index(request):
    # pessoas = Pessoa.pessoas.all()
    data_hora = request.session['data_hora']
    nome = request.session['nome']
    return render(request,"pessoa/index.html", {'data_hora':data_hora,'nome':nome})
    #return render(request,"layout/layout.html", {'title':'Bem Vindo ao app Revenda gustavo pereira'})


class PessoaDetailView(DetailView):
    model = Pessoa
