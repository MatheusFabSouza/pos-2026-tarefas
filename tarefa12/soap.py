import requests
from xml.dom.minidom import parseString

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
op = input("Digite 1 2 ou 3 para operação: ")
if op == "1":
    ope = "CountryFlag"
elif op == "2":
    ope = "CapitalCity"
elif op == "3":
    ope = "CountryName"
country_code = input("Digite o código do país: ")

# XML estruturado
payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{ope} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{country_code}</sCountryISOCode>
					</{ope}>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
if response.status_code == 200:
    if op == "1":
        print("A foto do país é (link): " + parseString(response.text).documentElement.getElementsByTagName("m:CountryFlagResult")[0].firstChild.nodeValue)
    elif op == "2":
        print("A capital do país é: " + parseString(response.text).documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue)
    elif op == "3":
        print("O nome do país é: " + parseString(response.text).documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue)