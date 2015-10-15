# -*- encoding:utf-8 -*-
from app import app, db
from flask import render_template, request, url_for, redirect
from models import Tarefa

@app.route('/')
def index():
    tarefas_pendentes = Tarefa.query.filter(Tarefa.concluida==False).order_by(db.desc(Tarefa.id)).all()
    tarefas_concluidas = Tarefa.query.filter(Tarefa.concluida==True).all()
    return render_template('index.html',
                            tarefas_pendentes=tarefas_pendentes,
                            tarefas_concluidas=tarefas_concluidas)


@app.route('/tarefa/nova', methods=['GET', 'POST'])
def nova_tarefa():
    if request.method == 'POST':
        tarefa = Tarefa()
        tarefa.titulo = request.form['titulo']
        tarefa.descricao = request.form['descricao']
        db.session.add(tarefa)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('nova_tarefa.html')


@app.route('/tarefa/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
    tarefa = Tarefa.query.filter(Tarefa.id == id).one()
    if request.method == 'POST':
        tarefa.titulo = request.form['titulo']
        tarefa.descricao = request.form['descricao']
        db.session.add(tarefa)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editar_tarefa.html', tarefa=tarefa)


@app.route('/tarefa/concluir/<int:id>', methods=['GET', 'POST'])
def concluir_tarefa(id):
    tarefa = Tarefa.query.filter(Tarefa.id==id).one()
    tarefa.concluida = True
    db.session.add(tarefa)
    db.session.commit()
    return redirect(url_for('index'))
