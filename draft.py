from functions.createtable import create_table
from functions.createdb import create_db
from functions.insert_rows import insert_one_row

insert_one_row(
    "test.db", "tabela", 
    "id, name, age",
     "5, 'renatinha', 15"
)