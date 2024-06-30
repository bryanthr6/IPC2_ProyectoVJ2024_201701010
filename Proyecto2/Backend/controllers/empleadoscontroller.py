from flask import Blueprint, jsonify, request
from models.empleado import Empleado
from controllers.estructuras import empleados
from xml.etree import ElementTree as ET
import os

Blueprint_empleado = Blueprint('empleado', __name__)

@Blueprint_empleado.route('/cargaempleados', methods=['POST'])
def cargarEmpleados():
    try:
        #OBTENEMOS EL XML
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'message': 'Error al cargar los empleados: EL XML está vacio',
                'status': 404
            }), 404
        #QUITARLE LOS SALTOS DE LINEA INNECESARIOS
        xml_entrada = xml_entrada.replace('\n', '')
        #LEER EL XML
        root = ET.fromstring(xml_entrada)
        for empleado in root:
            codigo = empleado.attrib['codigo']
            nombre = ''
            puesto = ''
            for elemento in empleado:
                if elemento.tag == 'nombre':
                    nombre = elemento.text
                if elemento.tag == 'puesto':
                    puesto = elemento.text
            nuevo = Empleado(codigo, nombre, puesto)
            empleados.append(nuevo)
            #AGREGAMOS EL EMPLEADO AL XML QUE YA EXISTE
            if os.path.exists('database/empleados.xml'):
                tree2 = ET.parse('database/empleados.xml')
                root2 = tree2.getroot()
                nuevo_empleado = ET.Element('empleado', codigo=nuevo.codigo)
                nombre = ET.SubElement(nuevo_empleado, 'nombre')
                nombre.text = nuevo.nombre
                puesto = ET.SubElement(nuevo_empleado, 'puesto')
                puesto.text = nuevo.puesto
                root2.append(nuevo_empleado)
                tree2.write('database/empleados.xml')

        #SI EN DADO CASO NO EXISTE EL XML, LO CREAMOS
        if not os.path.exists('database/empleados.xml'):
            with open('database/empleados.xml', 'w', encoding='utf-8') as file:
                file.write(xml_entrada)
                file.close()
            return jsonify({
                'message': 'Empleados cargados correctamente',
                'status': 200
            }), 200
    except:
        return jsonify({
            'message': 'Error al cargar los empleados',
            'status': 404
        }), 404
    
def precargar_empleados():
    empleados = []
    if os.path.exists('database/empleados.xml'):
        tree = ET.parse('database/empleados.xml')
        root = tree.getroot()
        for empleado in root:
            codigo = empleado.attrib['codigo']
            nombre = ''
            puesto = ''
            for elemento in empleado:
                if elemento.tag == 'nombre':
                    nombre = elemento.text
                if elemento.tag == 'puesto':
                    puesto = elemento.text
            nuevo = Empleado(codigo, nombre, puesto)
            empleados.append(nuevo)
    return empleados