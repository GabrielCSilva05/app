def ler_csv(nome_arquivo):
    perguntas = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            perguntas.append(linha.strip().split(';'))
    return perguntas

def construir_xml(perguntas):
    xml_parts = ['<quiz>']
    
    for tipo, texto, opcoes, resposta_correta, feedback in perguntas:
        xml_parts.append('  <question type="category">')
        xml_parts.append(f'    <name><text>{texto}</text></name>')
        xml_parts.append(f'    <questiontext format="html"><text><![CDATA[<p>{texto}</p>]]></text></questiontext>')
        
        if tipo == "escolha múltipla":
            opcoes_lista = opcoes.split(';')
            for opcao in opcoes_lista:
                is_correct = '100' if opcao.startswith(resposta_correta) else '0'
                xml_parts.append(f'    <answer fraction="{is_correct}" format="html"><text><![CDATA[{opcao}]]></text></answer>')
        
        if feedback:
            xml_parts.append(f'    <feedback><text>{feedback}</text></feedback>')
        
        xml_parts.append('  </question>')
    
    xml_parts.append('</quiz>')
    return '\n'.join(xml_parts)

def salvar_xml(xml_str, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(xml_str)

def converter_csv_para_xml(csv_arquivo, xml_arquivo):
    perguntas = ler_csv(csv_arquivo)
    xml_str = construir_xml(perguntas)
    salvar_xml(xml_str, xml_arquivo)
    print(f"Arquivo XML '{xml_arquivo}' gerado com sucesso!")

converter_csv_para_xml('perguntas.csv', 'perguntas_moodle.xml')

