from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum


db = SQLAlchemy()


class Device(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    is_on = db.Column(db.Boolean, default=True)

class DeviceSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Device
         include_relationships = True
         load_instance = True
