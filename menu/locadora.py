#fumcionalidades do sistema
#alugar veiculo
#devolver veiculo
#cadastrar cliente
#consuçtar veiculo disponivel
opcao = 0
while opcao != 5:
    print("SIstema de locação")
    print("1 - alugar veiculo")
    print("2 - devolver veiculo")
    print("3 - cadastrar cliente")
    print("4 - consultar veiculo disponivel")
    print("5- sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        nome = input("nome: ")
        cpf = int(input("Digite seu CPF: "))
        nascimento = input("data de Nascimento: ")

        habilitacao = int(input("Habilitação: "))
        print("Cadastro efetuado com sucesso!")
    elif opcao == 4:
        tipo = input("Informe o tipo do carro (Hatch, Sedã, Suv): ")
        print("Carros disponiveis")
        print("onix 2022 Turbo - 180,00")
        print("Polo 2020 1.6 - 200,00")
        print("Mobi 2023 1.0 - 140,00")
    elif opcao == 5:
        print("Obrigado por usar nosso sistema")
    else:
        print("Opção invalida!")
