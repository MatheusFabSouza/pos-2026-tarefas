from xml.dom.minidom import parse

dom = parse("cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

for prato in pratos:
    nome = prato.getAttribute('nome')
    descricao = prato.getAttribute('descricao') 
    ingredientes = prato.getElementsByTagName('ingrediente')[0]
    preco = prato.getAttribute('preco')
    caloria = prato.getAttribute('caloria')
    tempoPreparo = prato.getAttribute('tempoPreparo')

    print("Nome: ", nome)
    print("Descrição: ", descricao)
    print("ingredientes: ", ingredientes)
    print("Preco:", preco)
    print("Calorias: ", caloria)
    print("Tempo de Preparo: ", tempoPreparo)
    print("---\n")