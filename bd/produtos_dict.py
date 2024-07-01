import pandas as pd

novos = pd.read_csv('produtos_novo.csv',sep=';')
velhos = pd.read_csv('produtos_velho.csv',sep=';')

subs = {
    'SE': 1,
    'SU': 2,
    'NE': 3,
    'NO': 4
}

data = []
for index, prod in velhos.iterrows():
    
    A = novos['submercado'] == subs[prod['submercado']]
    B = novos['energia'] == prod['energia']
    C = novos['ini_fornec'] == prod['ini_fornec']
    D = novos['fim_fornec'] == prod['fim_fornec']
    E = novos['preco'] == prod['preco']
    
    produto_match = novos.loc[A&B&C&D&E].reset_index(drop=True)
    
    if produto_match.empty:
        continue
    
    if len(list(produto_match['nome'])) > 1:
        print('\n\niuqhiduhwiduhqi')
        exit()
        
    id_novo = produto_match.loc[0,'id_produto']
    
    data.append([prod['id_produto'],id_novo])

df = pd.DataFrame(data,columns=['id_velho','id_novo'])

df.to_csv('ids_dict.csv',index=False,sep=';')