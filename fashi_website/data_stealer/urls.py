from django.conf.urls import patterns, url
from data_stealer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)