class Verificator():
    def verify(data):
        if not data["name"] or not data["syllables"]:
            abort(400, description="Um dos dados não foi enviado para a criação do item")
        if not data['image'] or not data['video'] or not data["audio"]:
            abort(400, description="Imagem, aúdio ou video não enviados")
        if not data["category"] and data["subcategory"]:
            abort(400, description="Possui subcategoria, porém não há categoria")
        if not data["imageName"] or not data["videoName"] or not data["audioName"]:
            abort(400, description="Não possui nome de imagem, nome de video ou nome de audio")
        if not data["imageType"] or not data["videoType"] or not data["videoType"]:
            abort(400, description="Não possui tipo de video, image ou audio")
        return