# Setup e Qualidade de Dados nos Projetos

## Propósito do Projeto

O objetivo deste projeto é entregar um pipeline de dados completo, com ênfase na validação de schemas de nosso conjunto de dados. Para padronizar e qualificar nosso projeto, implementamos um setup padrão para projetos de dados e uma rotina de validação (CI/CD).

## Tecnologias Utilizadas

- **Pandera**: Utilizado para validação de DataFrames.
- **Pydantic**: Exemplos de validação disponíveis na pasta de exemplos.
- **DuckDB**: Banco de dados utilizado inicialmente para salvar nossa pipeline.
- **JSON**: Alternativa para salvar nossa tabela, demonstrando diversas possibilidades.

## Fluxo do Projeto

![Imagem MVC](images/schema_project.png)

## Documentação do Projeto

[Documentação Completa](https://lucasphn.github.io/qualidade_de_dados_nos_projetos/)

## Setup do Projeto

### Git
1. Adicione e comite suas alterações:
    ```bash
    git add .
    git commit -m "meu setup de projeto"
    git push
    ```

### Pyenv
1. Configure a versão do Python local:
    ```bash
    pyenv local 3.11.5
    ```

2. Crie seu ambiente virtual:
    ```bash
    pyenv exec python -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

    > **Nota:** Utilize `pyenv exec` para garantir que o ambiente considere a versão de Python definida no Pyenv (.python-version). Para alterar a versão do Python, recrie o ambiente virtual.

### MkDocs
1. Crie a estrutura de documentação:
    ```bash
    mkdocs new .
    mkdocs serve
    ```

2. Configure plugins no arquivo `mkdocs.yml`:
    ```yaml
    plugins:
      - search
      - mermaid2
    ```

3. Configure o tema no arquivo `mkdocs.yml`:
    ```yaml
    theme:
      name: material
    ```

4. Adicione suporte a docstrings no arquivo `mkdocs.yml`:
    ```yaml
    plugins:
      - search
      - mermaid2
      - mkdocstrings
    ```

### Ferramentas Adicionais
- **taskipy**: Automatiza comandos, configurado no arquivo `pyproject.toml`.
- **isort**: Formata automaticamente as importações de acordo com a PEP 8.
- **black**: Formata o código de acordo com a PEP 8.
- **pytest**: Framework de testes para Python.

### Comandos Úteis

- **Pytest**
    - Comando comum:
        ```bash
        pytest tests -v
        ```
    - Comando com taskipy:
        ```bash
        task test
        ```

> **Nota:** O comando `task test` é definido no arquivo `pyproject.toml` como um atalho.

### Conclusão

Este setup padrão e as ferramentas listadas proporcionam uma base sólida para garantir a qualidade dos dados e a consistência do desenvolvimento do projeto. Explore os exemplos e a documentação completa para aproveitar ao máximo as funcionalidades oferecidas.
