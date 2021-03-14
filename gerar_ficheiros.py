import random


def generate_files():
    num = 1
    numero = 10
    for i in range(20):
        ficheiro = "input"
        with open(ficheiro + str(num) + ".in", 'w') as escrever:
            escrever.write(str(numero))
            escrever.write("\n")
            for j in range(numero):
                escrever.write(str(random.randint(0, 1_000_000_000)))
                escrever.write(" ")
            numero *= 2
        num += 1


def generate_files_BC():
    num = 26
    numero = 83_886_080
    numero_auxiliar = 1_000_000
    for i in range(10):
        ficheiro = "input"
        with open(ficheiro + str(num) + ".in", 'w') as escrever:
            escrever.write(str(numero))
            escrever.write("\n")
            for j in range(numero):
                escrever.write(str(random.randint(0, 1_000_000_000)))
                escrever.write(" ")
            numero += (numero_auxiliar*3)
        num += 1


generate_files_BC()
