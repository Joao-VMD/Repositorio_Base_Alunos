import sqlite3

def conexao_banco():
    conexao = sqlite3.connect(".\\teste.db")
    return conexao

def iniciar_tabelas():
    with conexao_banco() as banco:
        banco.executescript("""
            CREATE TABLE IF NOT EXISTS turma (
                id INTEGER NOT NULL PRIMARY KEY,
                serie TEXT NOT NULL,
                sala INTEGER NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                data_nasc DATE,
                cpf INTEGER,
                fk_turma INTEGER NOT NULL,
                FOREIGN KEY (fk_turma) REFERENCES turma(id)
                    ON UPDATE NO ACTION ON DELETE NO ACTION
            );

            INSERT OR IGNORE INTO turma (serie, sala) VALUES 
                ('3°B', 5), 
                ('2°A', 6), 
                ('1°C', 4);

            INSERT OR IGNORE INTO aluno (nome, data_nasc, fk_turma) VALUES
                ('Cleber Bastos', '2007-01-01', 3),
                ('Lucas Camomilo', '2008-08-01', 1),
                ('Pierre Labubu', '2006-01-01', 1);
        """)
        banco.commit()
    
    def cadastrar_aluno(nome, fk_turma, data_nasc=None, cpf=None):
     with conexao_banco() as banco:
        banco.execute(
            "INSERT INTO aluno (nome, data_nasc, cpf, fk_turma) VALUES (?, ?, ?, ?)",
            (nome, data_nasc, cpf, fk_turma)
        )
        banco.commit()  


    cadastrar_aluno("Miguel O Souza", 2, "2007-01-01")

if __name__ == "__main__":
    iniciar_tabelas()
