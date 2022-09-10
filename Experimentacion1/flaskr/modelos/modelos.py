from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum


db = SQLAlchemy()


class Test(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))

class TestSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Test
         include_relationships = True
         load_instance = True
