from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import DetailView, ListView, CreateView

from django.contrib import messages

from veiculo.models import Veiculo

from django.urls import reverse_lazy

from .models import Revenda, Profile, FamilyMember

from .forms import FamilyMemberFormSet, RevendaFormSet

from django.db import transaction


def index(request):
    messages.info(request, 'informação')
    messages.success(request, 'Salvo com sucesso')
    messages.warning(request, 'Your account expires in three days.')
    messages.error(request, 'Document deleted.')
    return render(request,"revenda/index.html", {'title':'Bem Vindo ao app Revenda carrros gustavo pereira'})

    #return render(request,"layout/layout.html", {'title':'Bem Vindo ao app Revenda gustavo pereira'})


def ativos(request):
    veiculos = Veiculo.seminovos.all()
    return render(request,"revenda/ativos.html", {'veiculos':veiculos})


class RevendaDetailView(DetailView):
    model = Revenda
    slug_field = 'slug'


class RevendaList(ListView):
    model = Revenda


class RevendaCarroCreate(CreateView):
    model = Revenda
    fields = ['nome', 'is_active']
    success_url = reverse_lazy('revenda-list')

    def get_context_data(self, **kwargs):
        data = super(RevendaCarroCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = RevendaFormSet(self.request.POST)
        else:
            data['familymembers'] = RevendaFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(RevendaCarroCreate, self).form_valid(form)






class ProfileList(ListView):
    model = Profile

class ProfileFamilyMemberCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberCreate, self).form_valid(form)

class ProfileCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']

