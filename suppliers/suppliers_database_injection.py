from suppliers.models import Fornecedor


#Criando vários fornecedores

fornecedores = [
    ['Lian Anhaia Correia', 'Pinnacle Electronics', 'Lian@gmail.com', 'Red Brick Way', 'tomfield', 'US', 'Fornecedor Numero 1'],
    ['Sarai Portela Caparica', 'Valkyrie Microsystems', 'Sarai@gmail.com', 'Gleaming Road', 'yerton', 'AZ', 'Fornecedor Numero 2'],
    ['Kristian Janes Fraga', 'Buckoustics', 'Kristian@gmail.com', 'Leacana Avenue', 'feehlens', 'AU', 'Fornecedor Numero 3'],
    ['Harry Castelo Delgado', 'Pixywood', 'Harry@gmail.com', 'Terrenfair Way', 'grarith', 'BS', 'Fornecedor Numero 4'],
    ['Felix Canela Cortês', 'Firetechs', 'Felix@gmail.com', 'Bartos Walk', 'taxlens', 'AT', 'Fornecedor Numero 5'],
    ['Rian Tabosa Póvoas', 'Elviations', 'Rian@gmail.com', 'Gleaming Road', 'yerton', 'AZ', 'Fornecedor Numero 6'],
]


for i in fornecedores:
    fornecedor = Fornecedor(
        fornecedor_nome = i[0],
        fornecedor_nome_empresa = i[1],
        fornecedor_email = i[2],
        fornecedor_endereco = i[3],
        fornecedor_cidade = i[4],
        fornecedor_pais = i[5],
        fornecedor_comentarios = i[6],
    )
    fornecedor.save()





# exec(open("suppliers/suppliers_database_injection.py").read())