from flask import Flask, render_template
import requests
import pandas as pd

#instancia o meu app no servidor
app = Flask(__name__)


@app.route('/ibge/<cep>')
def retornaIBGE(cep):  # put application's code here
    url = "https://viacep.com.br/ws/"+cep+"/json"
    dados = requests.get(url)
    #dataset = pd.DataFrame(dados.json(), index=[0])
    return dados.json()

@app.route('/')
def index():
    #carrega a o html na página
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
