from app import db

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    descricao = db.Column(db.String(150))
    concluida = db.Column(db.Boolean(), default=False)

    def __init__(self):
        self.concluida = False

    def __repr__(self):
        return '<Tarefa, titulo=%s>' % (self.titulo)
