from flaskr import create_app
from flask_restful import Api
from .modelos import db
from .vistas import VistaDevice
from .vistas import VistaDevices

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaDevices, '/devices')
api.add_resource(VistaDevice, '/device/<int:id_device>')