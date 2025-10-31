# declaração de coleções
usuarios = [
    {
        'nome': "Fulano",
        'idade': 20,
        'email': "fulano@gmail.com"
    },
    {
        'nome': "Cicrano",
        'idade': 25,
        'email': "cicrano@gmail.com"
    }
]

for usuario in usuarios:
    print(f"\n{'-'*40}\n")
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario[chave]}")