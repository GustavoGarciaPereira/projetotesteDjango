from django.urls import path
from django.conf.urls import url

from revenda.views import RevendaDetailView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ativos/asdrftgyhujk', views.ativos, name='ativos'),
    url(r'(?P<pk>\d+)/detalhe/$', RevendaDetailView.as_view(), name='revenda_detail'),
    # url(r'^(?P<slug>[-\w\d]+)/$', RevendaDetailView.as_view(), name='revenda_detail'),
    path('<slug:slug>/', RevendaDetailView.as_view(), name='revenda_detail')
]