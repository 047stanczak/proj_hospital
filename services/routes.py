from main import app
from flask import render_template

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

@app.route('/addConsulta.html')
def addConsulta():
    return render_template('addConsulta.html')