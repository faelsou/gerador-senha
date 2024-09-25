# Projeto gerador-senha
Projeto em Python que gera senhas embaralhadas com um front-end simples, podemos utilizar Flask (um framework web para Python) para o back-end e HTML/CSS/JavaScript para o front-end. Abaixo está um exemplo básico de como isso pode ser feito.

1. Estrutura do Projeto
A estrutura do projeto será a seguinte:

password_generator/
│
├── app.py  # Arquivo principal do Flask
├── templates/
│   └── index.html  # Front-end HTML
└── static/
    └── style.css  # Arquivo de estilos (CSS)
    
2. Instalando Dependências
Antes de começar, você precisa instalar o Flask. Use o seguinte comando para instalar:

bash
pip install Flask

3. Arquivo Backend (app.py) python

4. Arquivo HTML (templates/index.html) html

5. Arquivo de Estilos (static/style.css) css

# 6. Rodar o Projeto
Salve os arquivos conforme a estrutura mencionada.
Execute o comando para rodar o servidor Flask:
bash
python app.py
Abra seu navegador e acesse http://127.0.0.1:5000.
7. Explicação do Funcionamento
Back-end (Flask): O Flask fornece o servidor back-end que processa a requisição de geração de senha.
O endpoint /gerar_senha é chamado via AJAX quando o usuário clica no botão de gerar senha.
A senha é gerada com a função gerar_senha que retorna uma combinação embaralhada de letras, números e símbolos.
Front-end (HTML/CSS/JavaScript): O front-end coleta o tamanho da senha desejada e envia essa informação ao Flask, exibindo a senha gerada de forma dinâmica.
Exemplo de Tela
A interface mostrará um campo para o usuário selecionar o tamanho da senha e um botão para gerar uma nova senha. A senha gerada aparecerá logo abaixo do botão.
