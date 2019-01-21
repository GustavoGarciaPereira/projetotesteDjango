from django.urls import path
from django.conf.urls import url

from pessoa.views import PessoaDetailView, index


urlpatterns = [
	path('',index,name='index'),
    url(r'detail/(?P<pk>\d+)/$', PessoaDetailView.as_view(), name='pessoa_detail'),
]