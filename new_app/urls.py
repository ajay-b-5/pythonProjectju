from django.urls import path

from new_app import views

urlpatterns = [

    path("home",views.home,name='home'),
    path("",views.index,name='index')
]