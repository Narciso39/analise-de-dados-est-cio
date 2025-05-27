def criar_tutorial():
    tutorial = """
    # Tutorial Básico de Análise de Dados com Python

    ## 1. Importação de Dados
    ```python
    import pandas as pd
    dados = pd.read_excel('vendas.xlsx')
    ```

    ## 2. Análise Básica
    ```python
    # Total de vendas
    total = dados['Valor'].sum()
    
    # Média por mês
    media_mensal = dados.groupby('Mês')['Valor'].mean()
    ```

    ## 3. Visualização
    ```python
    import matplotlib.pyplot as plt
    dados['Produto'].value_counts().plot(kind='bar')
    plt.savefig('vendas_por_produto.png')
    ```
    """
    
    with open('tutorial_analise_dados.md', 'w') as f:
        f.write(tutorial)
    
    return "Tutorial criado com sucesso!"

print(criar_tutorial())