from flask import Flask, render_template, request
from clima_api import obter_clima

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    clima = None
    if request.method == "POST":
        cidade = request.form.get("cidade")
        if cidade:
            clima = obter_clima(cidade)
    return render_template("index.html", clima=clima)


if __name__ == "__main__":
    app.run(debug=True)
