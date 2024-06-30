from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('carga/', views.admin_carga, name='carga'),
    path('user/', views.userview, name='user'),
    path('signin/', views.signin, name='signin')
]