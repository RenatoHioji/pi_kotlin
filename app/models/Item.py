import uuid
from sqlalchemy.dialects.postgresql import UUID
from .db import db, game_items
from typing import Optional
class Item(db.Model):
    __tablename__ = 'item'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    syllables = db.Column(db.String(255), nullable = False)
    img = db.Column(db.String(255), unique=False, nullable=False)
    video = db.Column(db.String(255), unique = False, nullable = False)
    category = db.Column(db.String(255), unique = False, nullable = True)
    subcategory = db.Column(db.String(255), unique = False, nullable= True)   
    
    game_id = db.Column(UUID(as_uuid=True), db.ForeignKey('game.id'), nullable=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("usuario.id"), nullable=True)
    
    def __init__(self, name: str, syllables: str, img: str, video: str, category: Optional[str] = None, subcategory: Optional[str] = None, user_id: Optional[str] = None, game_id: Optional[str] = None ):
        self.name = name
        self.syllables = syllables
        self.img = img
        self.video = video
        self.category = category
        self.subcategory = subcategory
        self.user_id = user_id
        self.game_id = game_id
    
    def serialize(item):
        return {
            "id": item.id,
            "name": item.name,
            "syllables": item.syllables,
            "img": item.img,
            "video": item.video,
            "category": item.category,
            "subcategory": item.subcategory
        }
    def serialize_list(items):
        item_list = []
        for item in items:
            item_list.append(item.serialize())
        return item_list

    @staticmethod
    def seed_item(Game):
        if not Item.query.first():
            items = [
                Item(name="Eu", syllables="Eu", img="eu.webp", video="eu.mp4", category="pessoa", subcategory="pronomes"),
                Item(name="Você", syllables="Vo-cê", img="voce.webp", video="voce.mp4", category="pessoa", subcategory="pronomes"),
                Item(name="Amigo", syllables="A-mi-go", img="amigo.webp", video="amigo.mp4", category="pessoa", subcategory="conhecido"),
                Item(name="Comer", syllables="Co-mer", img="comer.webp", video="comer.mp4", category="acao", subcategory="verbos"),
                Item(name="Beber", syllables="Be-ber", img="beber.webp", video="beber.mp4", category="acao", subcategory="verbos"),
                Item(name="Brincar", syllables="Brin-car", img="brincar.webp", video="brincar.mp4", category="acao", subcategory="verbos"),
                Item(name="Dormir", syllables="Dor-mir", img="dormir.webp", video="dormir.mp4", category="acao", subcategory="verbos"),
                Item(name="Correr", syllables="Cor-rer", img="correr.webp", video="correr.mp4", category="acao", subcategory="verbos"),
                Item(name="Pular", syllables="Pu-lar", img="pular.webp", video="pular.mp4", category="acao", subcategory="verbos"),
                Item(name="Ler", syllables="Ler", img="ler.webp", video="ler.mp4", category="acao", subcategory="verbos"),
                Item(name="Sinto", syllables="Sin-to", img="sinto.webp", video="sinto.mp4", category="acao", subcategory="verbos"),
                Item(name="Desenhar", syllables="De-se-nhar", img="desenhar.webp", video="desenhar.mp4", category="acao", subcategory="verbos"),
                Item(name="Escrever", syllables="Es-cre-ver", img="escrever.webp", video="escrever.mp4", category="acao", subcategory="verbos"),
                Item(name="Rir", syllables="Rir", img="rir.webp", video="rir.mp4", category="acao", subcategory="verbos"),
                Item(name="Cantar", syllables="Can-tar", img="cantar.webp", video="cantar.mp4", category="acao", subcategory="verbos"),
                Item(name="Feliz", syllables="Fe-liz", img="feliz.webp", video="feliz.mp4", category="emocao", subcategory="sentimentos"),
                Item(name="Triste", syllables="Tris-te", img="triste.webp", video="triste.mp4", category="emocao", subcategory="sentimentos"),
                Item(name="Bravo", syllables="Bra-vo", img="bravo.webp", video="bravo.mp4", category="emocao", subcategory="sentimentos"),
                Item(name="Amor", syllables="A-mor", img="amor.webp", video="amor.mp4", category="emocao", subcategory="sentimentos"),
                Item(name="Fome", syllables="Fo-me", img="fome.webp", video="fome.mp4", category="necessidade", subcategory="sensacoes"),
                Item(name="Quero", syllables="Que-ro", img="quero.webp", video="quero.mp4", category="necessidade", subcategory="sensacoes"),
                Item(name="Cachorro", syllables="Ca-chor-ro", img="cachorro.webp", video="cachorro.mp4", category="animal", subcategory="mamiferos"),
                Item(name="Gato", syllables="Ga-to", img="gato.webp", video="gato.mp4", category="animal", subcategory="mamiferos"),
                Item(name="Bola", syllables="Bo-la", img="bola.webp", video="bola.mp4", category="objeto", subcategory="esportes"),
                Item(name="Carro", syllables="Car-ro", img="carro.webp", video="carro.mp4", category="objeto", subcategory="transportes"),
                Item(name="Biscoito", syllables="Bis-coi-to", img="biscoito.webp", video="biscoito.mp4", category="alimento", subcategory="alimentos"),
                Item(name="Madeira", syllables="Ma-dei-ra", img="madeira.webp", video="madeira.mp4", category="material", subcategory="elementos"),
                Item(name="Pato", syllables="Pa-to", img="pato.webp", video="pato.mp4", category="animal", subcategory="aves"),
                Item(name="Sim", syllables="Sim", img="sim.webp", video="sim.mp4", category="resposta", subcategory="afirmativas"),
                Item(name="Uva", syllables="U-va", img="uva.webp", video="uva.mp4", category="alimento", subcategory="frutas")
            ]
            db.session.add_all(items)
            db.session.commit()
            
            games = Game.query.all()
            madeira = Item.query.filter_by(name="Madeira").first()
            uva = Item.query.filter_by(name="Uva").first()
            sim = Item.query.filter_by(name="Sim").first()
            pato = Item.query.filter_by(name="Pato").first()
            items = Item.query.filter(Item.name.notin_(["Madeira", "Uva", "Sim", "Pato"])).all()
            values = [
                {'game_id': games[0].id, 'item_id': madeira.id},
                {'game_id': games[0].id, 'item_id': items[2].id},
                {'game_id': games[0].id, 'item_id': items[1].id},
                {'game_id': games[0].id, 'item_id': items[0].id},
                {'game_id': games[1].id, 'item_id': items[5].id},
                {'game_id': games[1].id, 'item_id': items[4].id},
                {'game_id': games[1].id, 'item_id': pato.id},
                {'game_id': games[1].id, 'item_id': items[8].id},
                {'game_id': games[2].id, 'item_id': items[9].id},
                {'game_id': games[2].id, 'item_id': uva.id},
                {'game_id': games[2].id, 'item_id': items[12].id},
                {'game_id': games[2].id, 'item_id': items[17].id},
                {'game_id': games[3].id, 'item_id': items[16].id},
                {'game_id': games[3].id, 'item_id': sim.id},
                {'game_id': games[3].id, 'item_id': items[9].id},
                {'game_id': games[3].id, 'item_id': items[10].id},
                {'game_id': games[4].id, 'item_id': items[11].id},
                {'game_id': games[4].id, 'item_id': items[6].id},
                {'game_id': games[4].id, 'item_id': items[19].id},
                {'game_id': games[4].id, 'item_id': pato.id},
                {'game_id': games[5].id, 'item_id': items[22].id},
                {'game_id': games[5].id, 'item_id': items[23].id},
                {'game_id': games[5].id, 'item_id': items[25].id},
                {'game_id': games[5].id, 'item_id': items[15].id}
            ]
            db.session.execute(game_items.insert(), values)
            db.session.commit()
        else:
            pass
            