from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text


def criar_engine():
    load_dotenv()
    DB_HOST     = os.getenv("DB_HOST")
    DB_PORT     = os.getenv("DB_PORT")
    DB_USER     = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME     = os.getenv("DB_NAME")

    URL_BANCO = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    return create_engine(URL_BANCO)

def testar_conexao():
    try:
        engine = criar_engine()
        with engine.connect() as conexao:
            resultado = conexao.execute(text("SELECT version()"))
            retorno = resultado.fetchone()[0]
            print(f"Conexão OK: {retorno}")
    except Exception as erro:
        print(f"Conexão falhou: {erro}")
        