import pandas as pd
import matplotlib.pyplot as plt

def analisar_vendas(caminho_arquivo):
    # Carregar dados de vendas
    try:
        dados = pd.read_excel(caminho_arquivo)
        
        # Análise básica
        total_vendas = dados['Valor'].sum()
        media_mensal = dados.groupby('Mês')['Valor'].sum().mean()
        produto_mais_vendido = dados['Produto'].value_counts().idxmax()
        
        # Gerar gráficos
        plt.figure(figsize=(10, 5))
        dados['Produto'].value_counts().plot(kind='bar')
        plt.title('Produtos Mais Vendidos')
        plt.savefig('produtos_mais_vendidos.png')
        
        return {
            'total_vendas': total_vendas,
            'media_mensal': media_mensal,
            'produto_mais_vendido': produto_mais_vendido
        }
        
    except Exception as e:
        return f"Erro ao analisar os dados: {str(e)}"

# Exemplo de uso
resultado = analisar_vendas('vendas_empresa.xlsx')
print(resultado)import pandas as pd
import matplotlib.pyplot as plt

def analisar_vendas(caminho_arquivo):
    # Carregar dados de vendas
    try:
        dados = pd.read_excel(caminho_arquivo)
        
        # Análise básica
        total_vendas = dados['Valor'].sum()
        media_mensal = dados.groupby('Mês')['Valor'].sum().mean()
        produto_mais_vendido = dados['Produto'].value_counts().idxmax()
        
        # Gerar gráficos
        plt.figure(figsize=(10, 5))
        dados['Produto'].value_counts().plot(kind='bar')
        plt.title('Produtos Mais Vendidos')
        plt.savefig('produtos_mais_vendidos.png')
        
        return {
            'total_vendas': total_vendas,
            'media_mensal': media_mensal,
            'produto_mais_vendido': produto_mais_vendido
        }
        
    except Exception as e:
        return f"Erro ao analisar os dados: {str(e)}"

# Exemplo de uso
resultado = analisar_vendas('vendas_empresa.xlsx')
print(resultado)