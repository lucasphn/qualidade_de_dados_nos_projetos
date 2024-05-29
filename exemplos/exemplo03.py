from pydantic import BaseModel, PositiveFloat, validate_call

# Neste exemplo vamos aprender a usar o pydantic para validar uma função específica nossa


# Minha classe de validação
class ValidandoFuncao(BaseModel):
    x: int
    y: int

# Minha função, mesmo definindo os tipos, não possui validação, o exemplo abaixo , mesmo usando str, ela concatena os textos.
def calculadora(x: int,y: int) -> int:
    return x + y

print(calculadora('teste','ola'))

# Para mudar isso, utilizo um decorador!

@validate_call
def calculadora(x: int,y: int) -> int:
    return x + y

print(calculadora('teste','ola'))

