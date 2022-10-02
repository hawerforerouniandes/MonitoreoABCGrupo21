from flask_restful import Api, Resource
from celery import Celery
from flaskr import create_app
from .modelos import db, DeviceSignal, DeviceSignalSchema

deviceSignal_schema = DeviceSignal()

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

class VistaDeviceSignal(Resource):

    def get(self):
        return [deviceSignal_schema.dump(ca) for ca in DeviceSignal.query.all()]

api = Api(app)
api.add_resource(VistaDeviceSignal, '/deviceSignal')