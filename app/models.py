from app import db
import datetime

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    descricao = db.Column(db.String(150))
    concluida = db.Column(db.Boolean(), default=False)
    dt_criacao = db.Column(db.DateTime())
    dt_conclusao = db.Column(db.DateTime())

    def __init__(self):
        self.concluida = False
        self.dt_criacao=datetime.datetime.now()

    def __repr__(self):
        return '<Tarefa, titulo=%s>' % (self.titulo)
