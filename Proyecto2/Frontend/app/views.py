from django.shortcuts import render, redirect
import requests
from .forms import LoginForm, FileForm
import json
#Para el CACHE
from django.core.cache import cache
#Para las COOKIES
from django.http import HttpResponse
#Para mostrar mensajes en pantalla
from django.contrib import messages


# Create your views here.

endpoint = 'http://localhost:5000/'

#contexto general, es como una variable global de entorno
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
                    'id': iduser,
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
                    rol = int(respuesta['role'])
                    contexto['user'] = iduser
                    #Crear una variable para ver si es admin o usuario
                    paginaredireccion = None

                    #Ir a ADMIN
                    if rol == 0:
                        #Si yo quiero almacenar al usuario en cache
                        #cache.set('iduser', iduser, timeout=None)
                        #Si yo quiero almacenar al usuario en una cookies
                        paginaredireccion = redirect('carga')
                        paginaredireccion.set_cookie('iduser', iduser)
                        return paginaredireccion
                    #Ir a USER
                    elif rol == 1:
                        #Si yo quiero almacenar al usuario en cache
                        #cache.set('iduser', iduser, timeout=None)
                        #Si yo quiero almacenar al usuario en una cookies
                        paginaredireccion = redirect('user')
                        paginaredireccion.set_cookie('iduser', iduser)
                        return paginaredireccion            
    except:
        return render(request, 'login.html')



def admincarga(request):
    ctx = {
        'title':'Carga Masiva'
    }
    return render(request, 'cargaadmin.html', ctx)

def cargarXML(request):
    ctx = {
        'contenido_archivo':None
    }
    try:
        if request.method == 'POST':
            #obtenemos el formulario
            form = FileForm(request.POST, request.FILES)
            print(form.is_valid())
            if form.is_valid():
                #obtenemos el archivo
                archivo = request.FILES['file']
                #guardamos el binario
                xml = archivo.read()
                xml_decodificado = xml.decode('utf-8')
                #guardamos el contenido del archivo
                contexto['binario_xml'] = xml
                contexto['contenido_archivo'] = xml_decodificado
                ctx['contenido_archivo'] = xml_decodificado
                return render(request, 'cargaadmin.html', ctx)
    except:
        return render(request, 'cargaadmin.html')

def enviarUsuarios(request):
    try:
        if request.method == 'POST':
            xml = contexto['binario_xml']
            if xml is None:
                messages.error(request, 'No se ha cargado ningun archivo')
                return render(request, 'cargaadmin.html')
            #Peticion al backend
            url = endpoint + 'cargausuarios'
            respuesta = requests.post(url, data=xml)

            mensaje = respuesta.json()
            messages.success(request, mensaje['message'])
            contexto['binario_xml'] = None
            contexto['contenido_archivo'] = None
            return render(request, 'cargaadmin.html', contexto)
    except:
        return render(request, 'cargaadmin.html')
    
def enviarProductos(request):
    try:
        if request.method == 'POST':
            xml = contexto['binario_xml']
            if xml is None:
                messages.error(request, 'No se ha cargado ningun archivo')
                return render(request, 'cargaadmin.html')
            #Peticion al backend
            url = endpoint + 'cargaproductos'
            respuesta = requests.post(url, data=xml)

            mensaje = respuesta.json()
            messages.success(request, mensaje['message'])
            contexto['binario_xml'] = None
            contexto['contenido_archivo'] = None
            return render(request, 'cargaadmin.html', contexto)
    except:
        return render(request, 'cargaadmin.html')
    
def enviarEmpleados(request):
    try:
        if request.method == 'POST':
            xml = contexto['binario_xml']
            if xml is None:
                messages.error(request, 'No se ha cargado ningun archivo')
                return render(request, 'cargaadmin.html')
            #Peticion al backend
            url = endpoint + 'cargaempleados'
            respuesta = requests.post(url, data=xml)

            mensaje = respuesta.json()
            messages.success(request, mensaje['message'])
            contexto['binario_xml'] = None
            contexto['contenido_archivo'] = None
            return render(request, 'cargaadmin.html', contexto)
    except:
        return render(request, 'cargaadmin.html')
    
def enviarActividades(request):
    try:
        if request.method == 'POST':
            xml = contexto['binario_xml']
            if xml is None:
                messages.error(request, 'No se ha cargado ningun archivo')
                return render(request, 'cargaadmin.html')
            #Peticion al backend
            url = endpoint + 'cargaactividades'
            respuesta = requests.post(url, data=xml)

            mensaje = respuesta.json()
            messages.success(request, mensaje['message'])
            contexto['binario_xml'] = None
            contexto['contenido_archivo'] = None
            return render(request, 'cargaadmin.html', contexto)
    except:
        return render(request, 'cargaadmin.html')

def verProductos(request):
    ctx = {
        'productos':None,
        'title':'Productos'
    }
    url = endpoint + 'verProductos'
    response = requests.get(url)
    data = response.json()
    ctx['productos'] = data['productos']
    return render(request, 'verproductosadmin.html', ctx)


def userview(request):
    return render(request, 'user.html')