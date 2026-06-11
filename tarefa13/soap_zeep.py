import zeep

# define a URL do WSDL
wsdl_url = "http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# define o código do país para BR
numero = input("Digite um número para converter: ")
# faz a chamada do serviço
result = client.service.NumberToWords(
	ubiNum=numero
)
# imprime o resultado
print(f"O número por extenso é: {result}")

