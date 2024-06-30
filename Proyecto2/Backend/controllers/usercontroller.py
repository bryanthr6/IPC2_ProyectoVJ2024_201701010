from flask import Blueprint, jsonify, request
from models.user import User
from controllers.estructuras import users
from xml.etree import ElementTree as ET
import os

Blueprint_user = Blueprint('user', __name__)
user_logueado = ''

@Blueprint_user.route('/cargausuarios', methods=['POST'])
def cargarUsuarios():
    try:
        # OBTENEMOS EL XML
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'message': 'Error al cargar los usuarios: EL XML está vacío',
                'status': 404
            }), 404
        # QUITARLE LOS SALTOS DE LÍNEA INNECESARIOS
        xml_entrada = xml_entrada.replace('\n', '')
        # LEER EL XML
        root = ET.fromstring(xml_entrada)
        for user in root:
            id = user.attrib['id']
            password = user.attrib['password']
            nombre = ''
            edad = ''
            email = ''
            telefono = ''
            for elemento in user:
                if elemento.tag == 'nombre':
                    nombre = elemento.text
                if elemento.tag == 'edad':
                    edad = elemento.text
                if elemento.tag == 'email':
                    email = elemento.text
                if elemento.tag == 'telefono':
                    telefono = elemento.text
            nuevo = User(id, password, nombre, edad, email, telefono)
            users.append(nuevo)
            # AGREGAMOS EL USUARIO AL XML QUE YA EXISTE
            if os.path.exists('database/usuarios.xml'):
                tree2 = ET.parse('database/usuarios.xml')
                root2 = tree2.getroot()
                nuevo_usuario = ET.Element('usuario', id=nuevo.id, password=nuevo.password)
                nombre = ET.SubElement(nuevo_usuario, 'nombre')
                nombre.text = nuevo.nombre
                edad = ET.SubElement(nuevo_usuario, 'edad')
                edad.text = nuevo.edad
                email = ET.SubElement(nuevo_usuario, 'email')
                email.text = nuevo.email
                telefono = ET.SubElement(nuevo_usuario, 'telefono')
                telefono.text = nuevo.telefono
                root2.append(nuevo_usuario)
                ET.indent(root2, space='\t', level=0)
                tree2.write('database/usuarios.xml', encoding='utf-8', xml_declaration=True)
        
        # SI EN DADO CASO NO EXISTE EL XML, LO CREAMOS
        if not os.path.exists('database/usuarios.xml'):
            with open('database/usuarios.xml', 'w', encoding='utf-8') as file:
                file.write(xml_entrada)
                file.close()
            
        return jsonify({
            'message': 'Usuarios cargados correctamente',
            'status': 200
        }), 200
    except:
        return jsonify({
            'message': 'Error al cargar los usuarios',
            'status': 404
        }), 404

@Blueprint_user.route('/verUsuario/<string:id>', methods=['GET'])
def obtenerUsuario(id):
    users = precargar_usuarios()
    diccionario_salida = {
        'mensaje': 'Usuario encontrado',
        'usuario': [],
        'status': 200
    }
    for usuario in users:
        if usuario.id == id:
            diccionario_salida['usuario'] = {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'edad': usuario.edad,
                'email': usuario.email,
                'telefono': usuario.telefono,
                'password': usuario.password
            }
            return jsonify(diccionario_salida), 200
    diccionario_salida['mensaje'] = 'Usuario no encontrado'
    diccionario_salida['status'] = 404
    return jsonify(diccionario_salida), 404

#Autenticación o login
@Blueprint_user.route('/login', methods=['POST'])
def Login():
    global user_logueado
    users = precargar_usuarios()
    id = request.json['id']
    password = request.json['password']
    if id == 'AdminIPC2' and password == 'IPC2VJ2024':
        user_logueado = id
        return jsonify({
            'message': 'Usuario logueado correctamente',
            'role': 0,
            'status': 200
        }), 200
    for user in users:
        if user.id == id and user.password == password:
            user_logueado = id
            return jsonify({
                'message':'Usuario logueado correctamente',
                'role':1,
                'status':200
            }), 200
    return jsonify({
        'message':'Usuario no encontrado',
        'role':0,
        'status':404
    }), 404


@Blueprint_user.route('/obtenerLogueado', methods=['GET'])
def obtenerLogueado():
    global user_logueado
    return jsonify({
        'usuario':user_logueado,
        'status':200
    }), 200


def precargar_usuarios():
    usuarios = []
    if os.path.exists('database/usuarios.xml'):
        tree = ET.parse('database/usuarios.xml')
        root = tree.getroot()
        for usuario in root:
            id = usuario.attrib['id']
            password = usuario.attrib['password']
            nombre = ''
            edad = ''
            email = ''
            telefono = ''
            for elemento in usuario:
                if elemento.tag == 'nombre':
                    nombre = elemento.text
                if elemento.tag == 'edad':
                    edad = elemento.text
                if elemento.tag == 'email':
                    email = elemento.text
                if elemento.tag == 'telefono':
                    telefono = elemento.text
            nuevo = User(id, password, nombre, edad, email, telefono)
            usuarios.append(nuevo)
    return usuarios
