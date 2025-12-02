import os
import sqlite3
from pathlib import Path

def reset_database():
    """
    Apaga o banco de dados existente e cria um novo usando o schema
    """
    db_path = Path("bancomvc.db")
    schema_path = Path("init/schema.sql")
    
    # Apagar banco de dados existente
    if db_path.exists():
        os.remove(db_path)
        print(f"✓ Banco de dados '{db_path}' foi deletado")
    else:
        print(f"ℹ Banco de dados '{db_path}' não encontrado")
    
    # Criar novo banco de dados e executar schema
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # Ler e executar o schema
        with open(schema_path, 'r', encoding='utf-8') as schema_file:
            schema = schema_file.read()
            cursor.executescript(schema)
        
        conn.commit()
        conn.close()
        print(f"✓ Novo banco de dados criado em '{db_path}'")
        print(f"✓ Schema do arquivo '{schema_path}' foi aplicado com sucesso")
        
    except FileNotFoundError as e:
        print(f"✗ Erro: Arquivo não encontrado - {e}")
    except Exception as e:
        print(f"✗ Erro ao criar banco de dados: {e}")

if __name__ == "__main__":
    reset_database()
