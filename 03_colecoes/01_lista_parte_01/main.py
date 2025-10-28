# importação 
import time
import os

# declaração de lista
nomes = ["Armando", "Fulano", "Ciclano", "Beltrano", "João", "Maria", "Deltan", "Eva", "Goiano", "Halfdan"]

# exibe toda a lista
os.system("cls")
for nome in nomes:
    time.sleep(1)
    print(nome)
    

# Ordena a lista em ordem alfabética
nomes.sort()

# re-exibe a lista em ordem alfábetica
os.system("cls")
print("\nOrdem Alfabética:\n")

for nome in nomes:
    time.sleep(1)
    print(nome)
    

# reverte a ordem da lista
nomes.sort(reverse=True)

os.system("cls")
print("\nOrdem alfabética reversa:\n")

for nome in nomes:
    time.sleep(1)
    print(nome)
    