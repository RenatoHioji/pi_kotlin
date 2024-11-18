from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID
db = SQLAlchemy()

user_history = db.Table("history", 
                        db.Column("history_id", UUID(as_uuid=True), primary_key = True, default=uuid.uuid4),
                        db.Column("user_id", UUID(as_uuid=True), db.ForeignKey('usuario.id'), unique=False),
                        db.Column("item_id", UUID(as_uuid=True), db.ForeignKey('item.id'), unique=False),
                        db.Column("timestamp", db.DateTime, default=db.func.current_timestamp()))

game_items = db.Table("game_items", 
                        db.Column("game_items_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                        db.Column("item_id", UUID(as_uuid=True), db.ForeignKey("item.id"), nullable=False),
                        db.Column("game_id", UUID(as_uuid=True), db.ForeignKey("game.id"), nullable=False))

game_list = db.Table("game_list",
                     db.Column("game_list_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                     db.Column("game_id", UUID(as_uuid=True), db.ForeignKey("game.id"), nullable=False),
                     db.Column("quiz_id", UUID(as_uuid=True), db.ForeignKey("quiz.id"), nullable=False)
                    )