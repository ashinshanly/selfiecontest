from django.conf.urls import url 
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [  
    url(r'^$', views.post_list, name = 'post_list'),

    url(r'^login/$', login, {'template_name': 'blog/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'blog/logout.html'}),
    url(r'^register/$', views.register, name='register'),
   
    url(r'^upload$', views.upload, name='upload'),
   
    url(r'^index$', views.index, name='index'),

    url(r'^events$', views.events, name='events'),
   
    url(r'^hala$', views.hala, name='hala'),
    url(r'^enter$', views.enter, name='enter'),


]
