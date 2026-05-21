import requests

API_URL = "https://jsonplaceholder.typicode.com"

def listar_usuarios():
    response = requests.get(f"{API_URL}/users")
    if response.status_code == 200:
        return response.json()
    else:
        return False

def read_usuario(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return False

def criar_usuario(user_data):
    response = requests.post(f"{API_URL}/users", json=user_data)
    if response.status_code == 201:
        return response.json()
    else:
        return False

def deletar_usuario(user_id):
    response = requests.delete(f"{API_URL}/users/{user_id}")
    if response.status_code == 204:
        return True
    else:
        return False

def update_usuario(user_id, user_data):
    response = requests.put(f"{API_URL}/users/{user_id}", json=user_data)
    if response.status_code == 200:
        return response.json()
    else:
        return False