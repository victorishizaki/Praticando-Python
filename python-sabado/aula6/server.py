from flask import Flask, jsonify, request, render_template

# criando aplicação e, flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# GET -> Buscar algo
@app.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({'msg': 'Ola , mundo!'})

# POST - Criar uma nova tarefa
""" 
JavaScript (Front) -> fetch
ReactJS (Front) -> axios
Insomnia (Aplicativo) -> Simular um Front
Postman (Aplicativo) -> Simular um Front

Back-end -> Modelo de API -> FULL REST
Full-stack -> Arquitetura MVC (Model, View, Controller)
"""
@app.route('/tarefas', methods =['POST'])
def add_tarefa():
    nova_tarefa = request.json # pegar a informação do body
    nova_tarefa['id'] =len(tarefas) + 1 # adicionando novo id
    tarefas.append(nova_tarefa) # adicionando nova tarefa na lista
    return jsonify(nova_tarefa), 201 # 201 -> created -> criado com sucesso

# Lista de tarefas
tarefas = [
    {'id': 1, 'titulo': 'Estudar Python', 'concluido': False},
    {'id': 2, 'titulo': 'Estudar Flask', 'concluido': True}
]

@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)

# iniciar o servidor
if __name__ == '__main__':
    
    app.run(debug=True)
    
#https://localhost:5000/helloworld
