from collections import Counter

def analisar_clientes(caminho_arquivo):
    dados = pd.read_csv(caminho_arquivo)
    
    # Padrões de compra por horário
    dados['Hora'] = pd.to_datetime(dados['DataHora']).dt.hour
    compras_por_horario = dados['Hora'].value_counts().sort_index()
    
    # Produtos mais comprados juntos
    combinacoes = dados.groupby('CompraID')['Produto'].agg(lambda x: tuple(sorted(x)))
    combinacoes_frequentes = Counter(combinacoes).most_common(5)
    
    return {
        'compras_por_horario': compras_por_horario.to_dict(),
        'combinacoes_frequentes': combinacoes_frequentes
    }