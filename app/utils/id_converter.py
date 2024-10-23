from flask import abort
import uuid
class id_converter:
    def convert_id_uuid(id):
        if not id:
            abort(400, description="Id de usuário não foi enviado")
        try:
            user_id = uuid.UUID(id)
            return user_id
        except Exception as e:
            abort(400, description="Id não pode ser transformado em UUID")