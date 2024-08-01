nome = "Gabriela"
idade = 17

# Exibição de valores
print(nome)
print(idade)
print("\n")

# 1º método de concatenação (string: str)
print("O meu nome é: " + nome + "e tenho " + str(idade) + "anos.")

# Segundo método de concatenação (format)
print("O meu nome é {} e tenho {} anos.\n".format(nome, idade))

# 3º Método de concatenação (f string)
print(f"O meu nome é: {nome} e tenho {idade} anos.\n")