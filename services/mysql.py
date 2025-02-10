from sqlalchemy import create_engine, text

engine = create_engine('mysql+pymysql://sqlalchemy:roteador@localhost:3306/hospital')

with engine.begin() as conn:
    conn.execute(text("DELETE FROM pacientes WHERE nome='Paciente';"))
    conn.execute(text("INSERT INTO pacientes VALUES ('Paciente' , '2000/01/01' , 'M' , 100000000000 , 00000000000 , 'EMPRESARIAL');") )
    conn.commit()