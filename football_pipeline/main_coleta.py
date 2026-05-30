from src.coleta.extratores import coletar_artilheiros, coletar_partidas, coletar_classificacao
import requests

COMPETICAO = "PL"
TEMPORADA = "2025"

try:
    print("Classificação")

    dados_classificacao = coletar_classificacao(COMPETICAO, TEMPORADA)
    tabela = dados_classificacao['standings'][0]['table']
    total_times = len(tabela)
    primeiro_colocado = tabela[0]

    chaves_principais = list(dados_classificacao.keys())
    print(f"\nChaves principais {chaves_principais}\n")

    print("\n Tabela \n")
    print(f"{'Pos':<4} | {'Clube':<25} | {'Pts':<4} | {'PJ':<3}")
    print("-" * 46)
    for linha in tabela:
        posicao = linha["position"]
        nome_clube = linha["team"]["name"]
        pontos = linha["points"]
        jogos_jogados = linha["playedGames"]
        print(f"{posicao:<4} | {nome_clube:<25} | {pontos:<4} | {jogos_jogados:<3}")

except requests.exceptions.HTTPError as erro:
    print(f"❌ Erro de API na Classificação: {erro}")
except Exception as erro:
    print(f"❌ Erro inesperado na Classificação: {erro}")

print("\n" + "=" * 50 + "\n")

try:
    print("Partidas")

    dados_partidas = coletar_partidas(COMPETICAO, TEMPORADA)

    chaves_partidas = list(dados_partidas.keys())
    print(f"Chaves principais {chaves_partidas}")

    lista_partidas = dados_partidas["matches"]
    total_jogos = len(lista_partidas)
    print(f"Total de partidas: {total_jogos}")

    print("\n Partidas \n")
    for jogo in lista_partidas:
        time1 = jogo["homeTeam"]["name"]
        time2 = jogo["awayTeam"]["name"]
        gols_mandante = jogo["score"]["fullTime"]["home"]
        gols_visitante = jogo["score"]["fullTime"]["away"]
        if gols_mandante is None:
            gols_mandante = 0
        if gols_visitante is None:
            gols_visitante = 0
        print(f"{time1:<25} {gols_mandante} x {gols_visitante} {time2:>25}")
except requests.exceptions.HTTPError as erro:
    print(f"❌ Erro de API nas Partidas: {erro}")
except Exception as erro:
    print(f"❌ Erro inesperado nas Partidas: {erro}")

try:
    print("Artilheiros")

    dados_artilheiros = coletar_artilheiros(COMPETICAO, TEMPORADA)

    chaves_artilheiros = list(dados_artilheiros.keys())
    print(f"Chaves principais {chaves_artilheiros}")

    lista_artilheiros = dados_artilheiros["scorers"]

    for artilheiro in lista_artilheiros:
        jogador = artilheiro["player"]["name"]
        time_dele = artilheiro["team"]["name"]
        gols_dele = artilheiro["goals"]
        print(f"{jogador:<25} | {time_dele:<25} | {gols_dele:<5}")

except requests.exceptions.HTTPError as erro:
    print(f"❌ Erro de API nos Artilheiros: {erro}")
except Exception as erro:
    print(f"❌ Erro inesperado nos Artilheiros: {erro}")