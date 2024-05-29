from pydantic import BaseModel, PositiveFloat, PositiveInt, ValidationError

# Exemplo de entrada de dados para verificação
dados = {
    "id_produto": ['aqui vai dar erro', 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "nome": ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E", 
             "Produto F", "Produto G", "Produto H", "Produto I", "Produto J"],
    "quantidade": [100, 150, 200, 50, 120, 80, 60, 30, 90, 20],
    "preco": [10.0, 20.0, 15.0, 5.0, 22.0, 45.0, 120.0, 85.0, 55.0, 100.0],
    "categoria": ["eletronicos", "mobilia", "informatica", "decoracao", "eletronicos", 
                  "mobilia", "informatica", "decoracao", "eletronicos", "mobilia"]
}

# Minha classe de validação de tipagem
class SchemaDados(BaseModel):
    id_produto: PositiveInt
    nome: str
    quantidade: PositiveFloat
    preco: PositiveFloat
    categoria: str


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
        print(f"Erro de validação no item {i + 1}:", e)
