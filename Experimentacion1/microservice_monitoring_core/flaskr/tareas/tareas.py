from ..app import db
from ..modelos import  DeviceSignal, DeviceSignalSchema
import os
from celery import Celery
from celery.signals import task_postrun
from flask.globals import current_app
import datetime

deviceSignal_schema = DeviceSignalSchema()

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task(name="tabla.registrar")
def process_signal(deviceSignal_json):
    if deviceSignal_json["is_on"]:
         new_device_Signal = DeviceSignal(id_device=deviceSignal_json["id"], signal=deviceSignal_json["sign"])
         db.session.add(new_device_Signal)
         db.session.commit()
    else:
        with open('log_device_signal.txt','a') as file:
            file.write('{} - Dispositivo {}: {}\n'.format(datetime.datetime.now(), deviceSignal_json["id"], deviceSignal_json["msg"]))
  

@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()