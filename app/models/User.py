from tortoise.models import Model
from tortoise import fields
import uuid
class User(Model):
    id = fields.UUIDField(pk = True, default = uuid.uuid4)
    username = fields.CharField(max_length=255, nullable=False, unique=True)
    email = fields.CharField(max_length=255, nullable=False, unique=True)
    password = fields.CharField(max_length=255, nullable=False)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    class Meta:
        table= "user"
    
    def seed_user():
        #Create a admin/admin
        pass            