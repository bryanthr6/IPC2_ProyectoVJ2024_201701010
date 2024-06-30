from django.shortcuts import render, redirect
import requests
from .forms import LoginForm
import json
#Para el CACHE
from django.core.cache import cache
#Para las COOKIES
from django.http import HttpResponse


# Create your views here.

endpoint = 'http://localhost:5000/'

#contexto general
contexto = {
    'user': None,
    'contenido_archivo': None,
    'binario_xml': None
}

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                #Obtenemos los datos del formulario
                iduser = form.cleaned_data['iduser']
                password = form.cleaned_data['password']

                #Hacemos la peticion al servidor o backend
                url = endpoint + 'login'
                #data a enviar al backend
                data = {
                    'iduser': iduser,
                    'password': password
                }

                #convertimos los datos a json
                json_data = json.dumps(data)

                #HEADERS
                headers = {
                    'Content-Type': 'application/json'
                }

                #Llamamos a la petición backend, esto es lo que hacemos en postman, llamamos al backend
                response = requests.post(url, data=json_data, headers=headers)
                #lo pasamos como un diccionario
                respuesta = response.json()
                if response.status_code == 200:
                    rol = respuesta['role']
                    contexto['user'] = iduser
                    #Crear una variable para ver si es admin o usuario
                    paginaredireccion = None
                    #Ir a ADMIN
                    if rol == 0:
                        #Si yo quiero almacenar al usuario en cache
                        #cache.set('iduser', iduser, timeout=None)
                        #Si yo quiero almacenar al usuario en una cookies
                        pagina_redireccion = redirect('carga')
                        pagina_redireccion.set_cookie('iduser', iduser)
                        return pagina_redireccion
                    #Ir a USER
                    elif rol == 1:
                        #Si yo quiero almacenar al usuario en cache
                        #cache.set('iduser', iduser, timeout=None)
                        #Si yo quiero almacenar al usuario en una cookies
                        pagina_redireccion = redirect('user')
                        pagina_redireccion.set_cookie('iduser', iduser)
                        return pagina_redireccion

                    
    except:
        pass

def admin_carga(request):
    return render(request, 'admin_carga.html')

def userview(request):
    return render(request, 'user.html')