from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum


db = SQLAlchemy()


class DeviceSignal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_device = db.Column(db.Integer)
    signal = db.Column(db.String(128))

class DeviceSignalSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = DeviceSignal
         include_relationships = True
         load_instance = True
