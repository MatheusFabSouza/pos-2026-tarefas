from xml.dom.minidom import parse
import json

dom = parse('imobiliaria.xml') 
imobiliaria = dom.documentElement
imoveis = imobiliaria.getElementsByTagName('imovel')

lista = []

for imovel in imoveis:
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue
    rua = imovel.getElementsByTagName("rua")[0].firstChild.nodeValue
    bairro = imovel.getElementsByTagName("bairro")[0].firstChild.nodeValue
    cidade = imovel.getElementsByTagName("cidade")[0].firstChild.nodeValue
    
    if imovel.getElementsByTagName("número"):
        numero = imovel.getElementsByTagName("número")[0].firstChild.nodeValue

    nome = imovel.getElementsByTagName("nome")[0].firstChild.nodeValue

    if imovel.getElementsByTagName("email"):
        email = imovel.getElementsByTagName("email")[0].firstChild.nodeValue

    telefones = imovel.getElementsByTagName("telefone")
    if telefones:
        if len(telefones) == 1:
            telefone = telefones[0].firstChild.nodeValue
        else:
            telefone = [quantidadesNumero.firstChild.nodeValue for quantidadesNumero in telefones]
    else:
        telefone = None

    tamanho = imovel.getElementsByTagName("tamanho")[0].firstChild.nodeValue
    numQuartos = imovel.getElementsByTagName("numQuartos")[0].firstChild.nodeValue
    numBanheiros = imovel.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue
    valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue

    lista.append({
        "descricao": descricao,
        "proprietario": {
            "nome": nome,
            "email": email,
            "telefone": telefone
        },
        "endereco": {
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "número": numero
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": numQuartos,
            "numBanheiros": numBanheiros
        },
        "valor": valor
    })

dados = {
    "imobiliaria": {
        "imovel": lista
    }
}

with open('imobiliaria.json', 'w', encoding="utf-8") as json_file:
    json.dump(dados, json_file)