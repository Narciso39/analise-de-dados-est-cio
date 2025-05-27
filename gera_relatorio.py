from fpdf import FPDF

def gerar_relatorio(resultados, nome_arquivo='relatorio.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Relatório de Análise de Dados", ln=1, align='C')
    
    pdf.cell(200, 10, txt=f"Total de Vendas: R${resultados['total_vendas']:,.2f}", ln=1)
    pdf.cell(200, 10, txt=f"Média Mensal: R${resultados['media_mensal']:,.2f}", ln=1)
    pdf.cell(200, 10, txt=f"Produto Mais Vendido: {resultados['produto_mais_vendido']}", ln=1)
    
    pdf.image('produtos_mais_vendidos.png', x=10, y=50, w=180)
    
    pdf.output(nome_arquivo)
    return f"Relatório gerado em {nome_arquivo}"

# Exemplo de uso
resultados = analisar_vendas('vendas_empresa.xlsx')
print(gerar_relatorio(resultados))from fpdf import FPDF

def gerar_relatorio(resultados, nome_arquivo='relatorio.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Relatório de Análise de Dados", ln=1, align='C')
    
    pdf.cell(200, 10, txt=f"Total de Vendas: R${resultados['total_vendas']:,.2f}", ln=1)
    pdf.cell(200, 10, txt=f"Média Mensal: R${resultados['media_mensal']:,.2f}", ln=1)
    pdf.cell(200, 10, txt=f"Produto Mais Vendido: {resultados['produto_mais_vendido']}", ln=1)
    
    pdf.image('produtos_mais_vendidos.png', x=10, y=50, w=180)
    
    pdf.output(nome_arquivo)
    return f"Relatório gerado em {nome_arquivo}"

# Exemplo de uso
resultados = analisar_vendas('vendas_empresa.xlsx')
print(gerar_relatorio(resultados))