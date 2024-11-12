import uuid
from sqlalchemy.dialects.postgresql import UUID
from .db import db, table_game_items
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
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("app_user.id"), nullable=True)
    
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
    def seed_item():
        if not Item.query.first():
            items = [
                Item(name="Eu", syllables="Eu", img="eu.svg", video="eu.mp4", category="pessoa", subcategory="pronomes"),
                Item(name="Você", syllables="Você", img="voce.svg", video="voce.mp4", category="pessoa", subcategory="pronomes"),
                Item(name="Amigo", syllables="Ami  - go", img="amigo.svg", video="amigo.mp4", category="pessoa", subcategory="conhecido"),
                Item(name="Almoço", syllables="Al - mo - ço", img="almoco.svg", video="almoco.mp4", category="acao", subcategory="verbos"),
                Item(name="Comer", syllables="Co - mer", img="comer.svg", video="comer.mp4", category="acao", subcategory="verbos"),
                Item(name="Beber", syllables="Be - ber", img="beber.svg", video="beber.mp4", category="acao", subcategory="verbos"),
                Item(name="Brincar", syllables="Brin - car", img="brincar.svg", video="brincar.mp4", category="acao", subcategory="verbos"),
                Item(name="Dormir", syllables="Dor - mir", img="dormir.svg", video="dormir.mp4", category="acao", subcategory="verbos"),
                Item(name="Correr", syllables="Cor - rer", img="correr.svg", video="correr.mp4", category="acao", subcategory="verbos"),
                Item(name="Pular", syllables="Pu - lar", img="pular.svg", video="pular.mp4", category="acao", subcategory="verbos"),
                Item(name="Ler", syllables="Le - r", img="ler.svg", video="ler.mp4", category="acao", subcategory="verbos"),
                Item(name="Sinto", syllables="Sin - to", img="sinto.svg", video="sinto.mp4", category="acao", subcategory="verbos"),
                Item(name="Desenhar", syllables="De - se - nhar", img="desenhar.svg", video="desenhar.mp4", category="acao", subcategory="verbos"),
                Item(name="Escrever", syllables="Es - cre - ver", img="escrever.svg", video="escrever.mp4", category="acao", subcategory="verbos"),
                Item(name="Rir", syllables="Rir", img="rir.svg", video="rir.mp4", category="acao", subcategory="verbos"),
                Item(name="Cantar", syllables="Can - tar", img="cantar.svg", video="cantar.mp4", category="acao", subcategory="verbos"),
                Item(name="Feliz", syllables="Fe - liz", img="feliz.svg", video="feliz.mp4", category="emocao", subcategory="sentimentos"),
                Item(name="Triste", syllables="Tris - te", img="triste.svg", video="triste.mp4", category="emocao", subcategory="sentimentos"),
                Item(name="Bravo", syllables="Bra - vo", img="bravo.svg", video="bravo.mp4", category="emocao", subcategory="sentimentos"),
                Item(name="Amor", syllables="A - mor", img="amor.svg", video="amor.mp4", category="emocao", subcategory="sentimentos"),
                Item(name="Fome", syllables="Fo - me", img="fome.svg", video="fome.mp4", category="necessidade", subcategory="sensacoes"),
                Item(name="Quero", syllables="Que - ro", img="quero.svg", video="quero.mp4", category="necessidade", subcategory="sensacoes"),
                Item(name="Cachorro", syllables="Ca - cho - rro", img="cachorro.svg", video="cachorro.mp4", category="animal", subcategory="mamiferos"),
                Item(name="Gato", syllables="Ga - to", img="gato.svg", video="gato.mp4", category="animal", subcategory="mamiferos"),
                Item(name="Bola", syllables="Bo - la", img="bola.svg", video="bola.mp4", category="objeto", subcategory="esportes"),
                Item(name="Carro", syllables="Car - ro", img="carro.svg", video="carro.mp4", category="objeto", subcategory="transportes"),
                Item(name="Biscoito", syllables="Bis - coi - to", img="biscoito.svg", video="biscoito.mp4", category="alimento", subcategory="alimentos"),
                Item(name="Madeira", syllables="Ma - dei - ra", img="madeira.svg", video="madeira.mp4", category="material", subcategory="elementos"),
                Item(name="Pato", syllables="Pa - to", img="pato.svg", video="pato.mp4", category="animal", subcategory="aves"),
                Item(name="Sim", syllables="Sim", img="sim.svg", video="sim.mp4", category="resposta", subcategory="afirmativas"),
                Item(name="Uva", syllables="U - va", img="uva.svg", video="uva.mp4", category="alimento", subcategory="frutas")
            ]
            for item in items:
                db.session.add(item)
            db.session.commit()
            
            db.session.execute(
                table_game_items.insert().values(game_id=game.id, item_id=madeira.id),
                table_game_items.insert().values(game_id=game.id, item_id=item2.id),
                table_game_items.insert().values(game_id=game.id, item_id=item3.id),
                table_game_items.insert().values(game_id=game.id, item_id=item4.id),
                table_game_items.insert().values(game_id=game2.id, item_id=item5.id),
                table_game_items.insert().values(game_id=game2.id, item_id=item6.id),
                table_game_items.insert().values(game_id=game2.id, item_id=pato.id),
                table_game_items.insert().values(game_id=game2.id, item_id=item8.id),
                table_game_items.insert().values(game_id=game3.id, item_id=item1.id),
                table_game_items.insert().values(game_id=game3.id, item_id=uva.id),
                table_game_items.insert().values(game_id=game3.id, item_id=item4.id),
                table_game_items.insert().values(game_id=game3.id, item_id=item6.id),
                table_game_items.insert().values(game_id=game4.id, item_id=item7.id),
                table_game_items.insert().values(game_id=game4.id, item_id=sim.id),
                table_game_items.insert().values(game_id=game4.id, item_id=item2.id),
                table_game_items.insert().values(game_id=game4.id, item_id=item30.id),
                table_game_items.insert().values(game_id=game5.id, item_id=item15.id),
                table_game_items.insert().values(game_id=game5.id, item_id=sim.id),
                table_game_items.insert().values(game_id=game5.id, item_id=item29.id),
                table_game_items.insert().values(game_id=game5.id, item_id=item30.id),
                table_game_items.insert().values(game_id=game6.id, item_id=item30.id),
                table_game_items.insert().values(game_id=game6.id, item_id=item25.id),
                table_game_items.insert().values(game_id=game6.id, item_id=item2.id),
                table_game_items.insert().values(game_id=game6.id, item_id=item5.id)
            )
        else:
            pass
            