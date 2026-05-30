from dotenv import load_dotenv
import requests
import os
import time

load_dotenv()
chaveAPI = os.getenv("FOOTBALL_API_KEY")

URL_BASE = 'https://api.football-data.org/v4'


def fazer_requisicao(endpoint, params=None):
  URL_COMPLETA = f"{URL_BASE}{endpoint}"
  headers = { 'X-Auth-Token': chaveAPI }
  while True:
        response = requests.get(URL_COMPLETA, headers=headers, params=params)

        if response.status_code == 429:
            print("Limite atingido! Aguardando 10 segundos...")
            time.sleep(10)
            continue  

        response.raise_for_status()

        return response.json()
