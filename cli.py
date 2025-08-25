import os
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("⚠️ Defina a variável de ambiente OPENWEATHER_API_KEY antes de rodar o programa.")


def obter_clima(cidade: str) -> dict:
    """
    Consulta o clima atual de uma cidade usando a API OpenWeather.

    Args:
        cidade (str): Nome da cidade a ser consultada.

    Returns:
        dict: Informações de clima contendo nome, temperatura, descrição,
              umidade e velocidade do vento.
    """
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


def exibir_clima(clima: dict) -> None:
    """
    Exibe no console as informações de clima formatadas.

    Args:
        clima (dict): Dicionário contendo informações ou erro.
    """
    if "erro" in clima:
        print(f"\n{clima['erro']}\n")
    else:
        print(f"\n🌍 Clima em {clima['nome']}:")
        print(f"🌡️ Temperatura: {clima['temp']:.1f}°C")
        print(f"☁️ Condições: {clima['descricao']}")
        print(f"💧 Umidade: {clima['umidade']}%")
        print(f"💨 Vento: {clima['vento']} m/s\n")


def main() -> None:
    """Função principal do programa."""
    print("=== Consulta de Clima ===")
    while True:
        cidade = input("Digite o nome da cidade (ou 'sair' para fechar): ").strip()
        if cidade.lower() == "sair":
            print("\nPrograma encerrado. Até logo! 👋\n")
            break
        if not cidade:
            print("⚠️ Digite uma cidade válida!\n")
            continue
        clima = obter_clima(cidade)
        exibir_clima(clima)


if __name__ == "__main__":
    main()
