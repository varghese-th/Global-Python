from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index_form, name='index_form'),
    

    
]