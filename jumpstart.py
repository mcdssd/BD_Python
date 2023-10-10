import pandas as pd
import sqlite3

#reservou um espaço de memória reservada a tabela
# create the dataframe 
data = pd.DataFrame({
  'ID': [1, 2, 3, 4 ],
  'Name': ['Marina', 'Mariana', 'Thais', 'Suellyn']
})

data 
#a tabela foi criada na memória

#dataframe é a tabela em si
#dataset é uma tabela que está no banco de dados
#database é um arquivo (objeto) com todas as tabelas

#create database and save the dataframe
conn = sqlite3.connect('mydatabase.db')

#connnect with database/ acesso ao servidor
sqlite3.connect('mydatabase.db')

#Use the to_sql method to save the Dataframe to a table in the database
data.to_sql('client', conn, if_exists='replace', index=False)

#close the database connection
conn.close()
