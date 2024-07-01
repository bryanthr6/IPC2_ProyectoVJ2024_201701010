from django.urls import path

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
]