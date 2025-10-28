# Declaração de Lista
nomes = []

try:
    while True:
        print("1 - Inserir nome na lista")
        print("2 - Exibir lista")
        print("3 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        match opcao:
            case "1":
                novo_nome = input("Informe o novo nome: ").strip().title()
                nomes.append(novo_nome)
                print(f"{novo_nome} inserido com sucesso!")
            case "2":
                print("\nLista de nomes:\n")
                for nome in nomes:
                    print(nome)
            case "3":
                break
            case _:
                print("Opção invávlida")
                continue
except Exception as e:
    print("Deu erro, tente novamente. {e}.")
finally:
    print("programa encerrado.")