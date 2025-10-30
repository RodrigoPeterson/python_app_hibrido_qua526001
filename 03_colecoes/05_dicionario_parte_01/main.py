import os

# Declaração de dicionário
usuario = {
    'nome': "Rodrigo Peterson",
    'idade': 40,
    'peso': 70.0,
    'altura': 1.73,
    'email': "rodrigo@gmail.com"
}

os.system("cls")

# saída de dados
print(f"nome: {usuario['nome']}")
print(f"idade: {usuario['idade']}")
print(f"peso: {usuario['peso']}kg")
print(f"altura: {usuario['altura']}m")
print(f"email: {usuario['email']}")