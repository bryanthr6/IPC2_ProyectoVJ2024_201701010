from flask import Blueprint, jsonify, request
from models.producto import Producto
from controllers.estructuras import productos
from xml.etree import ElementTree as ET
import os

Blueprint_producto = Blueprint('producto', __name__)


@Blueprint_producto.route('/cargaproductos', methods=['POST'])
def cargarProductos():
    try:
        #OBTENEMOS EL XML
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'message': 'Error al cargar los productos: EL XML está vacio',
                'status': 404
            }), 404
        #QUITARLE LOS SALTOS DE LINEA INNECESARIOS
        xml_entrada = xml_entrada.replace('\n', '')
        #LEER EL XML
        root = ET.fromstring(xml_entrada)
        for producto in root:
            id = producto.attrib['id']
            nombre = ''
            precio = ''
            descripcion = ''
            categoria = ''
            cantidad = ''
            imagen = ''
            for elemento in producto:
                if elemento.tag == 'nombre':
                    nombre = elemento.text
                if elemento.tag == 'precio':
                    precio = elemento.text
                if elemento.tag == 'descripcion':
                    descripcion = elemento.text
                if elemento.tag == 'categoria':
                    categoria = elemento.text
                if elemento.tag == 'cantidad':
                    cantidad = elemento.text
                if elemento.tag == 'imagen':
                    imagen = elemento.text
            nuevo = Producto(id, nombre, precio, descripcion, categoria, cantidad, imagen)
            productos.append(nuevo)
            #AGREGAMOS EL PRODUCTO AL XML QUE YA EXISTE
            if os.path.exists('database/productos.xml'):
                tree2 = ET.parse('database/productos.xml')
                root2 = tree2.getroot()
                nuevo_producto = ET.Element('producto', id=nuevo.id)
                nombre = ET.SubElement(nuevo_producto, 'nombre')
                nombre.text = nuevo.nombre
                precio = ET.SubElement(nuevo_producto, 'precio')
                precio.text = nuevo.precio
                descripcion = ET.SubElement(nuevo_producto, 'descripcion')
                descripcion.text = nuevo.descripcion
                categoria = ET.SubElement(nuevo_producto, 'categoria')
                categoria.text = nuevo.categoria
                cantidad = ET.SubElement(nuevo_producto, 'cantidad')
                cantidad.text = nuevo.cantidad
                imagen = ET.SubElement(nuevo_producto, 'imagen')
                imagen.text = nuevo.imagen
                root2.append(nuevo_producto)
                ET.indent(root2, space='\t', level=0)
                tree2.write('database/productos.xml', encoding='utf-8', xml_declaration=True)
        
        #SI EN DADO CASO NO EXISTE EL XML, LO CREAMOS
        if not os.path.exists('database/productos.xml'):
            with open('database/productos.xml', 'w', encoding='utf-8') as file:
                file.write(xml_entrada)
                file.close()
        return jsonify({
            'message': 'Productos cargados correctamente',
            'status': 200
        }), 200
    except:
        return jsonify({
            'message': 'Error al cargar los productos',
            'status': 404
        }), 404


@Blueprint_producto.route('/verProductos', methods=['GET'])
def ver_productos():
    try:
        if not productos:
            return jsonify({
                'productos': [],
                'message': 'No hay productos disponibles',
                'status': 404
            }), 404

        # Crear manualmente la lista de productos en formato JSON
        productos_json = [
            {
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'descripcion': producto.descripcion,
                'categoria': producto.categoria,
                'cantidad': producto.cantidad,
                'imagen': producto.imagen
            }
            for producto in productos
        ]

        return jsonify({
            'productos': productos_json,
            'message': 'Lista de productos obtenida correctamente',
            'status': 200
        }), 200
    except Exception as e:
        return jsonify({
            'message': f'Error al obtener la lista de productos: {str(e)}',
            'status': 500
        }), 500



def precargar_productos():
    productos = []
    if os.path.exists('database/productos.xml'):
        tree = ET.parse('database/productos.xml')
        root = tree.getroot()
        for producto in root:
            id = producto.attrib['id']
            nombre = ''
            precio = ''
            descripcion = ''
            categoria = ''
            cantidad = ''
            imagen = ''
            for elemento in producto:
                if elemento.tag == 'nombre':
                    nombre = elemento.text
                if elemento.tag == 'precio':
                    precio = elemento.text
                if elemento.tag == 'descripcion':
                    descripcion = elemento.text
                if elemento.tag == 'categoria':
                    categoria = elemento.text
                if elemento.tag == 'cantidad':
                    cantidad = elemento.text
                if elemento.tag == 'imagen':
                    imagen = elemento.text
            nuevo = Producto(id, nombre, precio, descripcion, categoria, cantidad, imagen)
            productos.append(nuevo)
    return productos
