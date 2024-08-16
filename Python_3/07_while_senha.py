i= 1
while i <= 3:

    user = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

# checagem
    if user != "Gisele" and senha != "123":
        print("usuário ou Senha incorretos!")
        print(" ")
        i += 1
    else:
        print(" ")
        print(f"Bem-Vindo, {user}!")
        break
      
else:
    print(f"Você excedeu todas as: {i-1} tentativas")