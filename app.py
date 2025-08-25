from flask import Flask, render_template, request
from clima_api import obter_clima

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    clima = None
    if request.method == "POST":
        cidade = request.form.get("cidade")
        if cidade:
            dados_clima = obter_clima(cidade)
            # Verifica se a chave 'erro' está no dicionário retornado
            if "erro" in dados_clima:
                clima = {"erro": dados_clima["erro"]}
            else:
                clima = dados_clima
    return render_template("index.html", clima=clima)

if __name__ == "__main__":
    app.run(debug=True)
    