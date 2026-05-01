from xml.dom.minidom import parse

dom = parse("tarefa08/cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName('prato')

print("MENU")
for prato in pratos:
    print(f"{prato.getAttribute('id')} - {prato.getElementsByTagName('nome')[0].firstChild.nodeValue}")

opcao = input("Escreva o id do prato para selecionar-lo no cardapio:")

for prato in pratos:
    if opcao == prato.getAttribute("id"):
        nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
        descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue
        preco_tag = prato.getElementsByTagName("preco")[0]
        preco = preco_tag.firstChild.nodeValue
        dinheiro = preco_tag.getAttribute("dinheiro")
        calorias = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue
        tempo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue
        ingredientes = prato.getElementsByTagName("ingrediente")
        print("\nNome:", nome)
        print("Descrição:", descricao)
        print("Ingredientes:")
        for ing in ingredientes:
            print("-", ing.firstChild.nodeValue)
        print("Preço:", dinheiro, preco)
        print("Calorias:", calorias)
        print("Tempo de preparo:", tempo)