from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, func, UniqueConstraint
from src.banco.conexao import criar_engine

metadata = MetaData()

partidas_staging = Table(
    "partidas_staging", 
    metadata,
    Column("id",    Integer, primary_key=True),
    Column("competicao",  String(100), nullable=False),
    Column("temporada", Integer),
    Column("rodada", Integer),
    Column("data_partida", DateTime),
    Column("status",  String(100), nullable=False),
    Column("id_casa",  Integer, nullable=False),
    Column("nome_casa",  String(100), nullable=False),
    Column("id_fora",  Integer, nullable=False),
    Column("nome_fora",  String(100), nullable=False),
    Column("gols_casa",  Integer),
    Column("gols_fora",  Integer),
    Column("coletado_em", DateTime, default=func.now()),

    UniqueConstraint('id', 'competicao', name='unique_partida_competicao')
)

def criar_tabelas():
    engine = criar_engine()
    metadata.create_all(engine, checkfirst=True)
    print("✓ Tabelas criadas com sucesso")