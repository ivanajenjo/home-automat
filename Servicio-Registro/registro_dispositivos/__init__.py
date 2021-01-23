import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("dispositivos.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class ListaDispositivos(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])

        return {'message': 'Success', 'data': devices}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identificador', required=True)
        parser.add_argument('nombre', required=True)
        parser.add_argument('tipo_dispositivo', required=True)
        parser.add_argument('gateway_controlador', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identificador']] = args

        return {'message': 'Dispositivo registrado', 'data': args}, 201


class Dispositivo(Resource):
    def get(self, identifier):
        shelf = get_db()

        # Si la clave no existe, return a 404 error.
        if not (identifier in shelf):
            return {'mensaje': 'Dispositivo no encontrado', 'data': {}}, 404

        return {'mensaje': 'Dispositivo encontrado', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        # si la clave no existe, return a 404 error.
        if not (identifier in shelf):
            return {'mensaje': 'Dispositivo no encontrado', 'data': {}}, 404

        del shelf[identifier]
        return {'mensaje': 'Dispositivo eliminado correctamente'}, 204


api.add_resource(ListaDispositivos, '/dispositivos')
api.add_resource(Dispositivo, '/dispositivo/<string:identifier>')
