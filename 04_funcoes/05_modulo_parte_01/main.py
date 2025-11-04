# importa as funções
import modulo as m

m.limpar()
while True:
    print("1 - Calcular Quadrado")
    print("2 - Calcular Retângulo")
    print("3 - Calcular Triângulo")
    print("4 - Calcular Circulo")
    print("5 - Calcular Trapézio")
    print("6 - Sair do programa")
    opcao = input("\nOpção desejada: \n").strip()
    m.limpar()
    match opcao:
        case "1":
            l = float(input("Informe o lado do quadrado: ").strip().replace(",","."))
            m.limpar()
            area = m.quadrado(l)
            print(f"\nÁrea do quadrado {area}\n")
            continue
        case "2":
            b = float(input("Informe a base: ").strip().replace(",","."))
            h = float(input("Informe a altura: ").strip().replace(",","."))
            m.limpar()
            area = m.retangulo(b, h)
            print(f"\nÁrea do retângulo é {area}\n")
            continue
        case "3":
            b = float(input("Informe a base: ").strip().replace(",","."))
            h = float(input("Informe a altura: ").strip().replace(",","."))
            m.limpar()
            area = m.triangulo(b, h)
            print(f"\nÁrea do triângulo {area}\n")
            continue
        case "4":
           r = float(input("Informe o raio do circulo: ").strip().replace(",","."))
           m.limpar()
           area = m.circulo(r)
           print(f"\nÁrea do círculo {area}\n")
           continue
        case "5":
            b = float(input("Informe a base menor: ").strip().replace(",","."))
            B = float(input("Informe a base maior: ").strip().replace(",","."))
            h = float(input("Informe a altura: ").strip().replace(",","."))
            m.limpar()
            area = m.trapezio(b, B, h)
            print(f"\nÁrea do trapézio {area}\n")

            continue
        case "6":
            print("\nPrograma encerrado.\n")
            break
        case _:
            print("\nOpção inválida. Tente novamente\n")
            continue