while True:


    # biblioteca
    import math

    # entrada de dados
    r = float(input("Informe o raio do círculo: ").strip().replace(",","."))

    # cálculos
    a = math.pi*(r**2)
    c = 2*math.pi*r

    # saida de dados
    print(f"Número do pi: {math.pi}")
    print(f"Área da circunferência: {a:.2f}")
    print(f"Tamanho da circunferência: {c:.2f}")

    resposta = input("Quer calcular mais uma vez? (s/n): ").strip().lower()
    if resposta == "s":
        continue
    if resposta == "n":
        break
