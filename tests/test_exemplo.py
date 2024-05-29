from app.funcao import funcao_ola_mundo

def teste_funcao_ola_mundo():
    gabarito = 'Olá mundo!'
    input = funcao_ola_mundo()
    assert input == gabarito
    