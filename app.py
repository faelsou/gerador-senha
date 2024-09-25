from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Função para gerar senha aleatória
def gerar_senha(tamanho=12):
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation
    todos_os_caracteres = letras_minusculas + letras_maiusculas + numeros + simbolos

    senha = [
        random.choice(letras_minusculas),
        random.choice(letras_maiusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    senha += random.choices(todos_os_caracteres, k=tamanho - 4)
    random.shuffle(senha)

    return ''.join(senha)

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para gerar senha via AJAX
@app.route('/gerar_senha', methods=['POST'])
def gerar_senha_ajax():
    tamanho = int(request.form.get('tamanho', 12))
    senha = gerar_senha(tamanho)
    return jsonify({'senha': senha})

if __name__ == "__main__":
    app.run(debug=True)
