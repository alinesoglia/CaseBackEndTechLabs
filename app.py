from flask import Flask, jsonify, request

app = Flask(__name__)
funcionarios = [
    {
        'id': 1,
        'nome': 'Aline Pelegrino',
        'nascimento': '07/03/1992',
        'endereco': 'Rua Araucária, 2534',
        'cpf': '345678912395',
        'estadocivil': 'casada'
    },
    {
        'id': 2,
        'nome': 'Beatriz Mota',
        'nascimento': '14/09/1994',
        'endereco': 'Rua Araucária, 230',
        'cpf': '12345678900',
        'estadocivil': 'casada'
    },
    {
        'id': 3,
        'nome': 'Edna Pelegrino',
        'nascimento': '03/10/1964',
        'endereco': 'Avenida Queirós Filho, 24',
        'cpf': '01234567896',
        'estadocivil': 'divorciada'
    }
]

@app.route('/funcionarios', methods=['GET'])
def obter_funcionarios():
    return jsonify(funcionarios)

@app.route('/funcionarios/<int:id>', methods=['GET'])
def obter_funcionario_por_id(id):
    for funcionario in funcionarios:
        if funcionario.get('id') == id:
            return jsonify(funcionario)

@app.route('/funcionarios/<int:id>', methods=['PUT'])
def editar_funcionario_por_id(id):
    funcionario_alterado = request.get_json()
    for indice,funcionario in enumerate(funcionarios):
        if funcionario.get('id') ==id:
            funcionarios[indice].update(funcionario_alterado)
            return jsonify(funcionarios[indice])

@app.route('/funcionarios', methods=['POST'])
def incluir_novo_funcionario():
    novo_funcionario = request.get_json()
    
    if(id_nao_existe(novo_funcionario.get('id')) and nome_nao_existe(novo_funcionario.get('name'))):
        funcionarios.append(novo_funcionario)
        return jsonify(funcionarios)
    return jsonify ("{'error': 'dados inválidos'}")

@app.route('/funcionarios/<int:id>', methods=['DELETE'])
def excluir_funcionario(id):
    for indice, funcionario in enumerate(funcionarios):
        if funcionario.get('id') == id:
            del funcionarios[indice]

    return jsonify(funcionarios)


def id_nao_existe(id):
    for indice,funcionario in enumerate(funcionarios):
        if funcionario.get('id') == id:
            return False
    return True

def nome_nao_existe(name):
    for indice,funcionario in enumerate(funcionarios):
        if funcionario.get('nome') == name:
            return False
    return True
app.run(port=5000,host='localhost', debug=True)
