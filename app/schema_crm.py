import pandera as pa
from pandera.typing import Series

email_regex = r"[^@]+@[^@]+\.[^@]+"

class ProdutoSchema(pa.SchemaModel):
    """
    Define o esquema para a validação de dados de produtos com Pandera.
    
    Este esquema inclui campos básicos para produtos, incluindo um campo de e-mail
    validado por uma expressão regular.

    Attributes:
        id_produto (Series[int]): Identificador do produto.
        nome (Series[str]): Nome do produto.
        quantidade (Series[int]): Quantidade disponível do produto, deve estar entre 1 e 2000.
        preco (Series[float]): Preço do produto, deve ser maior que 0.
        categoria (Series[str]): Categoria do produto.
        email (Series[str]): E-mail associado ao produto, deve seguir o formato padrão de e-mails.
    """
    id_produto: Series[int]
    nome: Series[str]
    quantidade: Series[int] = pa.Field(ge=1, le=2000)
    preco: Series[float] = pa.Field(gt=0)
    categoria: Series[str]
    email: Series[str] = pa.Field(regex=email_regex)

    class Config:
        coerce = True # garantir que os tipos de dados estejam iguais ao nosso schema
        strict = True # garantir que os meus dados estejam com a mesma quantidade de colunas do schema


# criando o Schema de validação após o cálculo de KPI, nos preparando para criar mais colunas em nossa tabela e salvar o resultado em outro banco
class ProductSchemaKPI(ProdutoSchema):

    valor_total_estoque: Series[float] = pa.Field(ge=0)  # O valor total em estoque deve ser >= 0
    categoria_normalizada: Series[str]  # Assume-se que a categoria será uma string, não precisa de check específico além de ser uma string
    disponibilidade: Series[bool]  # Disponibilidade é um booleano, então não precisa de check específico