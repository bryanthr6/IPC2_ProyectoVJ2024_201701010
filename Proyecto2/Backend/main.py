from flask import Flask
from flask_cors import CORS
from controllers.usercontroller import Blueprint_user, users, precargar_usuarios
from controllers.productoscontroller import Blueprint_producto, precargar_productos
from controllers.empleadoscontroller import Blueprint_empleado, empleados, precargar_empleados
from controllers.actividadescontroller import Blueprint_actividad, actividades, precargar_actividades

app = Flask(__name__)
cors = CORS(app)

#Para PRECARGAR la data
users = precargar_usuarios()
productos = precargar_productos()
empleados = precargar_empleados()
actividades = precargar_actividades()

#REGISTRAMOS BLUEPRINTS
app.register_blueprint(Blueprint_user)
app.register_blueprint(Blueprint_producto)
app.register_blueprint(Blueprint_empleado)
app.register_blueprint(Blueprint_actividad)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)