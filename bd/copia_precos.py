""" copiando os precos diarios que estao na tabela antiga para a nova
pra apagar as tabelas que nao sao mais usadas do banco de dados

dados velhos sao 2023-01-23 pra tras
"""
import pandas as pd
from logpy import tools as tl

# id que relaciona o produto da tabela antiga com a nova
ids_dict = pd.read_csv('ids_dict.csv',sep=';')

# pegando todos os precos medios da tabela antiga
db = tl.connection_db('BBCE')
query_precos = '''
    SELECT id_produto, dia, preco 
    FROM precos_bbce_geral
    ORDER BY dia ASC;
'''
df_precos = pd.DataFrame(db.query(query_precos))


query = '''
    INSERT INTO Precos_diarios (id_produto,dia,preco)
    VALUES
'''
for index, linha in df_precos.iterrows():
    
    id_novo = ids_dict.loc[ids_dict['id_velho']==linha['id_produto']].reset_index(drop=True).loc[0,'id_novo']
    
    query += f'''
        ('{id_novo}','{linha['dia']}','{linha['preco']}'),'''

query = query.rstrip(',') + ';'

db.query(query)
db.db_commit()
db.db_close()
# comentario sinistro !!! wtf ????
print(query)