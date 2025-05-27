import dash
from dash import dcc, html
import plotly.express as px

app = dash.Dash(__name__)

def criar_dashboard(dados_vendas, dados_clientes):
    app.layout = html.Div([
        html.H1("Dashboard de Análise para Pequenos Negócios"),
        
        dcc.Graph(
            figure=px.bar(
                x=list(dados_vendas['compras_por_horario'].keys()),
                y=list(dados_vendas['compras_por_horario'].values()),
                title='Vendas por Horário'
            )
        ),
        
        dcc.Graph(
            figure=px.pie(
                names=[x[0][0] for x in dados_clientes['combinacoes_frequentes']],
                values=[x[1] for x in dados_clientes['combinacoes_frequentes']],
                title='Combinações de Produtos Frequentes'
            )
        )
    ])
    
    return app

if __name__ == '__main__':
    dados_vendas = analisar_vendas('vendas.xlsx')
    dados_clientes = analisar_clientes('clientes.csv')
    app = criar_dashboard(dados_vendas, dados_clientes)
    app.run_server(debug=True)