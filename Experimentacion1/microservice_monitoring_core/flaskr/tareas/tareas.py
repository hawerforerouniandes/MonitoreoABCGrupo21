from ..app import db
from ..modelos import  DeviceSignal, DeviceSignalSchema
import os
from celery import Celery
from celery.signals import task_postrun
from flask.globals import current_app

deviceSignal_schema = DeviceSignalSchema()

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task(name="tabla.registrar")
def process_signal(deviceSignal_json):
    new_device_Signal = DeviceSignal(id_device=deviceSignal_json["id"], signal=deviceSignal_json["sign"])
    db.session.add(new_device_Signal)
    db.session.commit()

@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()