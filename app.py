from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atómicos'
    }
]

# Consultar(Todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
#Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
#Editar
@app.route('/livros<int:id>', methods=['PUT'])
def obter_livro_por_id(id):
   livro_alterado = request.get_json()
   for indice, livro in enumerate(livros):
    if livro.get('id') == id:
        livros[indice].update(livro_alterado)
        return jsonify(livros[indice])
#Criar
@app.route('/livros/', methods=['POST'])
def incluir_novo_livro():
   novo_livro = request.get_json()
   livros.append(novo_livro)
   return jsonify(livros)
#Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def exluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)


#LINKS PARA ESTUDAR

# https://www.codementor.io/@olawalealadeusi896/restful-api-with-python-flask-framework-and-postgres-db-part-1-kbrwbygx5
# https://dev.to/nagatodev/series/15583
# https://dev.to/nagatodev/how-to-add-login-authentication-to-a-flask-and-react-application-23i7