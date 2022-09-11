from microservice_device import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from celery import Celery

app = create_app('default')
celery = Celery(__name__, broker='redis://localhost:6379/0')
app_context = app.app_context()
app_context.push()
api = Api(app)
api.init_app(app)

@celery.task(name="tabla.registrar")
def process_signal(cancion_json):
    pass


class VistaDevice(Resource):
    
    def post(self, id_device):
        content = requests.get('http://127.0.0.1:5000/device/{}'.format(id_device))

        if content.status_code == 404:
            return content.json(),404
        else:
            device = content.json()
            device["sign"] = request.json["sign"]
            args = (device,)
            process_signal.apply_async(args)
            return json.dumps(device)

api.add_resource(VistaDevice, '/device/<int:id_device>/process_signal')
