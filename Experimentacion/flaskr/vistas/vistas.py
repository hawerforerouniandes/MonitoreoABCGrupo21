from flask import request

from ..authorization import operador_required

from ..modelos import db, Device, DeviceSchema, User, UserSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token

device_schema = DeviceSchema()
user_schema = UserSchema()

class VistaLogIn(Resource):

    def post(self):
        usuario = User.query.filter(User.username == request.json["username"], User.password == request.json["password"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            additional_claims = {"role": usuario.role}
            token_de_acceso = create_access_token(identity=usuario.id, additional_claims=additional_claims)
            return {"mensaje":"Acceso concedido", "usuario": {"nombre":usuario.username, "id": usuario.id, "token": token_de_acceso}}

class VistaDevices(Resource):
    @jwt_required()
    def post(self):
        new_device = Device(name=request.json["name"], is_on=request.json["is_on"])
        db.session.add(new_device)
        db.session.commit()
        return device_schema.dump(new_device)
    
    @jwt_required()
    def get(self):
        return [device_schema.dump(ca) for ca in Device.query.all()]

class VistaDevice(Resource):
    
    @jwt_required()
    def get(self, id_device):
        return device_schema.dump(Device.query.get_or_404(id_device))

    @jwt_required(optional=True)
    @operador_required()
    def put(self, id_device):
        device = Device.query.get_or_404(id_device)
        device.is_on = request.json.get("is_on",device.is_on)
        db.session.commit()
        return device_schema.dump(device)

class VistaUsers(Resource):
    @jwt_required()
    def post(self):
        new_user = User(username=request.json["username"], password=request.json["password"], role=request.json["role"])
        db.session.add(new_user)
        db.session.commit()
        return device_schema.dump(new_user)
    @jwt_required()
    def get(self):
        return [user_schema.dump(ca) for ca in User.query.all()]


