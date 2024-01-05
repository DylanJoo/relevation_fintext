# from django.conf.urls import patterns, url
from django.urls import re_path, path
from django.views.generic import TemplateView

from judgementapp import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^query$', views.query_list, name='query_list'),
    re_path(r'^query/qrels$', views.qrels, name='qrels'),
    re_path(r'^query/qlabels$', views.qlabels, name='qlabels'),
    re_path(r'^query/(?P<qId>[A-Za-z0-9_\-\+\.]+)/$', views.query, name='query'),
    re_path(r'^query/(?P<qId>[A-Za-z0-9_\-\+\.]+)/doc/(?P<docId>[A-Za-z0-9_\-\+\.]+)/$', views.document, name='document'),
	re_path(r'^query/(?P<qId>[A-Za-z0-9_\-\+\.]+)/doc/(?P<docId>[+A-Za-z0-9_\-\+\.]+)/judge/$', views.judge, name='judge'),    
    re_path(r'^upload/$', TemplateView.as_view(template_name='judgementapp/upload.html')),
	re_path(r'^upload/save$', views.upload, name='upload'),        
	re_path(r'^upload/delete$', views.delete, name='delete'),        
	re_path(r'^upload/reset$', views.reset, name='reset'),        
]
    # re_path(r'^about/$', TemplateView.as_view(template_name='judgementapp/about.html')),
