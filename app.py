import requests

API_KEY = "3aab59826080fbbe786892b7e43594a7"  # sua chave
cidade = input("Digite o nome da cidade: ")
print(f"Cidade digitada: {cidade}")

url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt&units=metric"

resposta = requests.get(url)
dados = resposta.json()

if resposta.status_code == 200:
    temperatura = dados['main']['temp']
    sensacao = dados['main']['feels_like']
    descricao = dados['weather'][0]['description']

    print(f"\nClima em {cidade}:")
    print(f"🌡️ Temperatura: {temperatura}°C")
    print(f"🌬️ Sensação térmica: {sensacao}°C")
    print(f"🌥️ Descrição: {descricao}")
else:
    print("🚨 Cidade não encontrada. Verifique o nome e tente novamente.")
