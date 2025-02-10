from main import app
from flask import render_template, request

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/pacientes.html')
def pacientes():
    return render_template('pacientes.html')

@app.route('/consultas.html')
def consultas():
    return render_template('consultas.html')

@app.route('/relatorios.html')
def relatorios():
    return render_template('relatorios.html')

@app.route('/addPaciente.html')
def addPaciente():
    return render_template('addPaciente.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get("nome")
    idade = request.form.get("idade")
    sexo = request.form.get("sexo")
    cpf = request.form.get("cpf")
    dataNascimento = request.form.get("dataNascimento")
    telefone = request.form.get("telefone")
    endereco = request.form.get("endereco")
    convenio = request.form.get("convenio")

    print(f'{nome} {idade} {sexo} {cpf} {dataNascimento} {telefone} {endereco} {convenio}')
    return render_template('addPaciente.html')

@app.route('/addConsulta.html')
def addConsulta():
    return render_template('addConsulta.html')