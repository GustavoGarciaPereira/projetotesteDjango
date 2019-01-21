from django.shortcuts import render
from django.http import HttpResponse
from django_ajax.decorators import ajax
# Create your views here.



def index(request):
    return render(request,"veiculo/index.html", {'title':'Bem Vindo ao app veiculo gustavo pereira'})




# We're using `django_ajax.middleware.AJAXMiddleware` in settings
# so we don't need to use `@ajax` and `AJAXMixin` decorators


@ajax
def foo_view(request):
    return {'nome': 'gustavo'}


@ajax
def my_view(request):
    return render(request, 'veiculo/index.html',{'nome': 'gustavo'})