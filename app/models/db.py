from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID
db = SQLAlchemy()

user_history = db.Table("history", 
                        db.Column("user_id", UUID(as_uuid=True), db.ForeignKey('user.id'), primary_key = True),
                        db.Column("item_id", UUID(as_uuid=True), db.ForeignKey('item.id'), primary_key = True),
                        db.Column("timestamp", db.DateTime, default=db.func.current_timestamp()))