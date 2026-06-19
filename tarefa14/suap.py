import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

#user = input("user: ")
#password = getpass()

#data = {"username":user,"password":password}

#response = requests.post(api_url+"token/pair", json=data)
#token = response.json()["access"]
#print(response.json())
token = ""
 
headers = {
    "Authorization": f"Bearer {token}"
}

ano = int(input("Ano:"))
periodo = int(input("Periodo:"))
url = f"{api_url}ensino/meu-boletim/{ano}/{periodo}/"
print(url)
response = requests.get(url, headers=headers)
disciplinas = response.json()["results"]

for disciplina in disciplinas:
    print(
        f"{disciplina['disciplina']} -"
        f"{disciplina['nota_etapa_1']} -"
        f"{disciplina['nota_etapa_2']} -"
        f"{disciplina['nota_etapa_3']} -"
        f"{disciplina['nota_etapa_4']}"
    )
print(response)