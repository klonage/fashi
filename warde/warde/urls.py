from django.conf.urls import patterns, include, url
from django.contrib import admin

from authentic import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warde.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.join_and_auth),
    url(r'^logout/', views.logout_auth),
    url(r'^secret-login/', views.secret_login),
    url(r'^algo/', views.algotest),
    url(r'^admin/', include(admin.site.urls)),
)
