from src.coleta.client import fazer_requisicao
import os
import json
from datetime import datetime

def coletar_partidas(codigo, temporada):
    endpoint_matches = f'/competitions/{codigo}/matches'


    params = {"season": temporada}

    dados = fazer_requisicao(endpoint_matches, params=params)

    tipo_dado = "matches"
    destino = f"data/raw/{tipo_dado}"
    os.makedirs(destino, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    nome_arquivo = f"{codigo}_{temporada}_{timestamp}.json"
    caminho_completo = os.path.join(destino, nome_arquivo)

    with open(caminho_completo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    return dados


def coletar_classificacao(codigo, temporada):
    endpoint_standings = f'/competitions/{codigo}/standings'

    params = {"season": temporada}


    dados = fazer_requisicao(endpoint_standings)

    tipo_dado = "standings"
    destino = f"data/raw/{tipo_dado}"
    os.makedirs(destino, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    nome_arquivo = f"{codigo}_{temporada}_{timestamp}.json"
    caminho_completo = os.path.join(destino, nome_arquivo)

    with open(caminho_completo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


    return dados


def coletar_artilheiros(codigo, temporada):
    endpoint_scorers = f'/competitions/{codigo}/scorers'

    params = {"season": temporada}

    dados = fazer_requisicao(endpoint_scorers)

    tipo_dado = "scorers"
    destino = f"data/raw/{tipo_dado}"
    os.makedirs(destino, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    nome_arquivo = f"{codigo}_{temporada}_{timestamp}.json"
    caminho_completo = os.path.join(destino, nome_arquivo)

    with open(caminho_completo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    return dados



