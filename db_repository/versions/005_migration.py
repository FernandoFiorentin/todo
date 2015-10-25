from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tarefa = Table('tarefa', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('titulo', String(length=50)),
    Column('descricao', String(length=150)),
    Column('concluida', Boolean, default=ColumnDefault(False)),
    Column('dt_criacao', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tarefa'].columns['dt_criacao'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tarefa'].columns['dt_criacao'].drop()
