# biblioteca
from modulo import limpar, primeiro_grau, segundo_grau

def main():
    limpar()
    while True: 
        print("0 - Sair do programa.")
        print("1 - Calcular equação do primeiro grau")
        print("2 - Calcular equação do segundo grau")
        opcao = input("\nOpção desejada: ").strip()
        match opcao:
            case "0":
                limpar()
                print("\nPrograma encerrado.\n")
                break
            case "1":
                limpar()
                a = float(input("Informe o valor de 'a': ").strip().replace(",","."))
                b = float(input("Informe o valor de 'b': ").strip().replace(",","."))
                limpar()
                x = primeiro_grau(a, b)
                print(f"\nx = {x}\n")
                continue
            case "2":
                a = float(input("Informe o valor de a: ").strip().replace(",","."))
                b = float(input("Informe o valor de b: ").strip().replace(",","."))
                c = float(input("Informe o valor de c: ").strip().replace(",","."))
                limpar()
                resultados = segundo_grau(a, b, c)
                for x in resultados:
                    print(f"x = {x}")
                continue
            case _:
                limpar()
                print("\nOpção inválida.\n")
                continue


if __name__ == "__main__":
    main()