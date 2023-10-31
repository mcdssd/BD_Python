import sqlite3
#para abrir a janela interactive jupyter -> config. -> selecionar window shift+enter 

#função em phyton

def create_db(database_name:str):
    """Create a database

    Args:
        database_name (str): A database's name.
    """
    sqlite3.connect(database_name)
    #cria um database
