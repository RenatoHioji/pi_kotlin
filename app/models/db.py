from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID
db = SQLAlchemy()

user_history = db.Table("history", 
                        db.Column("history_id", UUID(as_uuid=True), primary_key = True, default=uuid.uuid4),
                        db.Column("user_id", UUID(as_uuid=True), db.ForeignKey('user.id'), unique=False),
                        db.Column("item_id", UUID(as_uuid=True), db.ForeignKey('item.id'), unique=False),
                        db.Column("timestamp", db.DateTime, default=db.func.current_timestamp()))