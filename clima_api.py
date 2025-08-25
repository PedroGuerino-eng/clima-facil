import os
import requests
from dotenv import load_dotenv

load_dotenv()


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("⚠️ Defina a variável de ambiente OPENWEATHER_API_KEY no .env")


def obter_clima(cidade: str) -> dict:
    """Consulta o clima atual de uma cidade usando a API OpenWeather."""
    try:
        params = {
            "q": cidade,
            "appid": API_KEY,
            "lang": "pt_br",
            "units": "metric"
        }
        resposta = requests.get(BASE_URL, params=params)
        resposta.raise_for_status()
        dados = resposta.json()

        return {
            "nome": dados["name"],
            "temp": dados["main"]["temp"],
            "descricao": dados["weather"][0]["description"].capitalize(),
            "umidade": dados["main"]["humidity"],
            "vento": dados["wind"]["speed"]
        }

    except requests.exceptions.HTTPError:
        return {"erro": "❌ Cidade não encontrada ou erro na requisição!"}
    except requests.exceptions.RequestException:
        return {"erro": "⚠️ Erro de conexão com a API!"}
    except KeyError:
        return {"erro": "⚠️ Resposta inesperada da API!"}
