from django.urls import path
from django.conf.urls import url

from revenda.views import RevendaDetailView, ProfileCreate, ProfileList, ProfileFamilyMemberCreate, RevendaCarroCreate, RevendaList
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ativos/asdrftgyhujk', views.ativos, name='ativos'),
    url(r'(?P<pk>\d+)/detalhe/$', RevendaDetailView.as_view(), name='revenda_detail'),
    # url(r'^(?P<slug>[-\w\d]+)/$', RevendaDetailView.as_view(), name='revenda_detail'),
    path('perfil/', ProfileFamilyMemberCreate.as_view(), name='crate_perfil'),
    path('list/', ProfileList.as_view(), name='profile-list'),

    path('revendacarrocriate/', RevendaCarroCreate.as_view(), name='crate_revenda'),
    path('revendaList/', RevendaList.as_view(), name='revenda-list'),


    path('<slug:slug>/', RevendaDetailView.as_view(), name='revenda_detail'),
]