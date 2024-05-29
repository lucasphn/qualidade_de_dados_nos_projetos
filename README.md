# Setup e Qualidade de dados nos projetos

Setup de projeto

Git
    commands:
    git add .
    git commit -m "meu setup de projeto"
    git push

pyenv
    commands:
    pyenv local 3.11.5

Em seguida, crie seu ambiente virtual:
    pyenv exec python -m venv .venv
    .venv\Scripts\Activate.ps1

-> Note que, é incluso 'pyenv exec' a frente do comando de criaçaõ do ambiente virtual, justamente para que o nosso ambiente considere a versão de Python que definimos no Pyenv, do arquivo .python-version criado.

-> Caso queira alterar a versão do Python, é necessário refazer essa etapa, recriando o ambiente virtual.

mkdocs
    commands:
    mkdocs new . (cria meu arquivo para documentação)
    mkdocs serve (abre uma porta local para acesso a documentação)

mkdocs-mermaid2-plugin (plugin para mkdocs, para melhorar layouts e integrar com excalidraw)
    [Commands] -> arquivo mkdocs.yml (copie e cole o script abaixo)

    plugins:
    - search
    - mermaid2

mkdocs-material (muda o layout da página html)
    [Commands] -> arquivo mkdocs.yml (copie e cole o script abaixo)

    theme:
    name: material

mkdocstrings-python (para que os comentários nas funções sejam integrados a documentação)
    [Commands] -> arquivo mkdocs.yml (copie e cole o script abaixo)

    plugins:
    - search
    - mermaid2
    - mkdocstrings

taskipy (é possível automatizar alguns comandos com essa biblioteca, repare no arquivo pyproject.toml)
isort (é uma biblioteca Python para formatar automaticamente as importações de acordo com a PEP 8: em ordem alfabética e organizada por seções e tipos.)
black (O black é uma biblioteca que formata o código de acordo com a PEP 8.)

pytest (O pytest é um framework de teste para python que fornece soluções para executar testes e fazer validações diversas)
    
    Commands:
    - Comando comum: pytest tests -v
    - Comando com taskipy: task test (por conta do nosso arquivo 'pyproject.toml' que definimos esse 'atalho')

