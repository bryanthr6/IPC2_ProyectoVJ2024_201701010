from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('carga/', views.admincarga, name='carga'),
    path('user/', views.userview, name='user'),
    path('signin/', views.signin, name='signin'),
    path('cargaxml/', views.cargarXML, name='cargaxml'),
    path('xmlUsuarios/', views.enviarUsuarios, name='xmlUsuarios'),
    path('xmlProductos/', views.enviarProductos, name='xmlProductos'),
    path('xmlEmpleados/', views.enviarEmpleados, name='xmlEmpleados'),
    path('xmlActividades/', views.enviarActividades, name='xmlActividades'),
    path('productos/', views.verProductos, name='productos'),
    path('verproductosu/', views.verProductosuser, name='verproductosu'),
    path('logout/', views.custom_logout, name='logout'),
    path('pdf/', views.viewPDF, name='pdf'),
]