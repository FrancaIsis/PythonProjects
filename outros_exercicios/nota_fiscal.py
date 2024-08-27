import xml.etree.ElementTree as ET
from openpyxl import Workbook

# Função para extrair dados do XML e salvar no Excel
def xml_para_excel(xml_file, excel_file):
    # Parse do XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Criação de um novo arquivo Excel
    wb = Workbook()
    ws = wb.active
    ws.title = 'Notas Fiscais'

    # Cabeçalho das colunas no Excel
    headers = ['NumeroNota', 'DataEmissao', 'ValorTotal']

    # Escreve o cabeçalho na primeira linha
    ws.append(headers)

    # Itera sobre os elementos do XML para extrair os dados desejados
    for nota in root.findall('.//nfeProc'):
        numero_nota = nota.find('nNF').text
        data_emissao = nota.find('dhEmi').text
        valor_total = nota.find('vNF').text

        # Escreve os dados na planilha do Excel
        ws.append([numero_nota, data_emissao, valor_total])

    # Salva o arquivo Excel
    wb.save(excel_file)

# Exemplo de uso
if __name__ == '__main__':
    xml_file = r"C:\PythonProjects\outros_exercicios\notas_fiscais.xml"
    excel_file = r"C:\PythonProjects\outros_exercicios\notas_fiscais.xlsx"
    xml_para_excel(xml_file, excel_file)
