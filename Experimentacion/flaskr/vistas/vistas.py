from flask import request
from ..modelos import db, Device, DeviceSchema, User, UserSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

device_schema = DeviceSchema()
user_schema = UserSchema()


class VistaDevices(Resource):

    def post(self):
        new_device = Device(name=request.json["name"], is_on=request.json["is_on"])
        db.session.add(new_device)
        db.session.commit()
        return device_schema.dump(new_device)

    def get(self):
        return [device_schema.dump(ca) for ca in Device.query.all()]

class VistaDevice(Resource):
    
    def get(self, id_device):
        return device_schema.dump(Device.query.get_or_404(id_device))

    def put(self, id_device):
        device = Device.query.get_or_404(id_device)
        device.is_on = request.json.get("is_on",device.is_on)
        db.session.commit()
        return device_schema.dump(device)

class VistaUsers(Resource):

    def post(self):
        new_user = User(username=request.json["username"], password=request.json["password"], role=request.json["role"])
        db.session.add(new_user)
        db.session.commit()
        return device_schema.dump(new_user)

    def get(self):
        return [user_schema.dump(ca) for ca in User.query.all()]