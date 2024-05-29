from pydantic import BaseModel, PositiveFloat, PositiveInt, field_validator, ValidationError
from enum import Enum

# Neste exemplo, além de usar os tipos nativos do python e alguns do pydantic, vamos personalizar alguma entradas , determinando os valores que queremos, repare

# Exemplo de entrada de dados para verificação
# Forçando erro na linha 10

dados = {
    "id_produto": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "nome": ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E", 
             "Produto F", "Produto G", "Produto H", "Produto I", "Produto J"],
    "quantidade": [100, 150, 200, 50, 120, 80, 60, 30, 90, 20],
    "preco": [10.0, 20.0, 15.0, 5.0, 22.0, 45.0, 120.0, 85.0, 55.0, 100.0],
    "categoria": ["eletronicos", "mobilia", "informatica", "decoracao", "eletronicos", 
                  "mobilia", "informatica", "decoracao", "eletronicos", "outros"]
}


class CategoriaProduto(str, Enum):
    categoria1 = 'eletronicos'
    categoria2 = 'mobilia'
    categoria3 = 'informatica'
    categoria4 = 'decoracao'


# Minha classe de validação de tipagem
class SchemaDados(BaseModel):
    id_produto: PositiveInt
    nome: str
    quantidade: PositiveFloat
    preco: PositiveFloat
    categoria: CategoriaProduto 


# Itera sobre os dados e valida cada linha
for i in range(len(dados["id_produto"])):
    item = {
        "id_produto": dados["id_produto"][i],
        "nome": dados["nome"][i],
        "quantidade": dados["quantidade"][i],
        "preco": dados["preco"][i],
        "categoria": dados["categoria"][i]
    }

    try:
        produto = SchemaDados(**item)
        print(produto)

    except ValidationError as e:
        print(f"Erro de validação no item {i + 1}: {e}")
