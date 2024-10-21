from app import ma
from flask_marshmallow import Schema, fields

class ItemSchema(ma.Schema):
    class Meta:
        name = fields.Str(required = True)
        syllables = fields.Str(required = True)
        img = fields.Str(required = True)
        audio = fields.Str(required = True)
        category = fields.Str()
        subcategory = fields.Str()