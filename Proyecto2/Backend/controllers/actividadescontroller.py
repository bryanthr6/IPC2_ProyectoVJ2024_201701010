from flask import Blueprint, jsonify, request
from models.actividad import Actividad
from xml.etree import ElementTree as ET
import os

Blueprint_actividad = Blueprint('actividad', __name__)

actividades = []

@Blueprint_actividad.route('/cargaactividades', methods=['POST'])
def cargarActividades():
    try:
        #OBTENEMOS EL XML
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'message': 'Error al cargar las actividades: EL XML está vacio',
                'status': 404
            }), 404
        #QUITARLE LOS SALTOS DE LINEA INNECESARIOS
        xml_entrada = xml_entrada.replace('\n', '')
        #LEER EL XML
        root = ET.fromstring(xml_entrada)
        for actividad in root:
            id = actividad.attrib['id']
            nombre = ''
            descripcion = ''
            empleado = ''
            dia = ''
            for elemento in actividad:
                if elemento.tag == 'nombre':
                    nombre = elemento.text
                if elemento.tag == 'descripcion':
                    descripcion = elemento.text
                if elemento.tag == 'empleado':
                    empleado = elemento.text
                if elemento.tag == 'dia':
                    dia = elemento.text
            nueva = Actividad(id, nombre, descripcion, empleado, dia)
            actividades.append(nueva)
            #AGREGAMOS LA ACTIVIDAD AL XML QUE YA EXISTE
            if os.path.exists('database/actividades.xml'):
                tree2 = ET.parse('database/actividades.xml')
                root2 = tree2.getroot()
                nueva_actividad = ET.Element('actividad', id=nueva.id)
                nombre = ET.SubElement(nueva_actividad, 'nombre')
                nombre.text = nueva.nombre
                descripcion = ET.SubElement(nueva_actividad, 'descripcion')
                descripcion.text = nueva.descripcion
                empleado = ET.SubElement(nueva_actividad, 'empleado')
                empleado.text = nueva.empleado
                dia = ET.SubElement(nueva_actividad, 'dia')
                dia.text = nueva.dia
                root2.append(nueva_actividad)
                tree2.write('database/actividades.xml')

        #SI EN DADO CASO NO EXISTE EL XML, LO CREAMOS
        if not os.path.exists('database/actividades.xml'):
            with open('database/actividades.xml', 'w', encoding='utf-8') as file:
                file.write(xml_entrada)
                file.close()
            return jsonify({
                'message': 'Actividades cargadas correctamente',
                'status': 200
            }), 200
    except:
        return jsonify({
            'message': 'Error al cargar las actividades',
            'status': 404
        }), 404
    
def precargar_actividades():
    actividades = []
    if os.path.exists('database/actividades.xml'):
        tree = ET.parse('database/actividades.xml')
        root = tree.getroot()
        for actividad in root:
            id = actividad.attrib['id']
            nombre = ''
            descripcion = ''
            empleado = ''
            dia = ''
            for elemento in actividad:
                if elemento.tag == 'nombre':
                    nombre = elemento.text
                if elemento.tag == 'descripcion':
                    descripcion = elemento.text
                if elemento.tag == 'empleado':
                    empleado = elemento.text
                if elemento.tag == 'dia':
                    dia = elemento.text
            nueva = Actividad(id, nombre, descripcion, empleado, dia)
            actividades.append(nueva)
    return actividades