from django.urls import path

from new_app import views

urlpatterns = [

    path("home",views.home,name='home'),
    path('index',views.index,name='index'),
    path('dash',views.dash,name='dash'),
    path('views_data',views.views_data,name='views_data'),
]