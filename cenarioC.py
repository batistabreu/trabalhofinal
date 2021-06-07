from openpyxl import Workbook

wb = Workbook()

planilha = wb.worksheets[0]

#Adicionando valores nas células desejadas
planilha['A1'] = int(1)
planilha['A2'] = int(2)
planilha['A3'] = int(3)
planilha['A4'] = int(4)
planilha['A5'] = int(5)
planilha['A6'] = '=SUM(A1:A5)'

#Criação da nova aba
nova_aba = wb.create_sheet("Aba 2")

#Preenchimento da nova aba
nova_aba['C3'] = 'Teste 123'

#Salvando o arquivo
wb.save(r"C:\Users\Bruna\ProjetosPython\Cenário3.xlsx")