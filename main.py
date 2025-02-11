from flask import Flask, request, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get("nome")
    sexo = request.form.get("sexo")
    cpf = request.form.get("cpf")
    dataNascimento = request.form.get("dataNascimento")
    telefone = request.form.get("telefone")
    endereco = request.form.get("endereco")
    convenio = request.form.get("convenio")
    engine = create_engine('mysql+pymysql://sqlalchemy:roteador@localhost:3306/hospital')
    with engine.begin() as conn:
        query = text("INSERT INTO pacientes (nome, nascimento, sexo, cpf, telefone, convenio) VALUES (:nome, :dataNascimento, :sexo, :cpf, :telefone, :convenio)")
        conn.execute(query, {
                "nome": nome,
                "dataNascimento": dataNascimento,
                "sexo": sexo,
                "cpf": cpf,
                "telefone": telefone,
                "convenio": convenio
            })
        conn.commit()
    print(f'{nome} {sexo} {cpf} {dataNascimento} {telefone} {endereco} {convenio}')
    return render_template('addPaciente.html')

from services.routes import *

if __name__ == "__main__":
    app.run(debug=True)