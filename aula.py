prosseguir = True

while prosseguir:
    val1 = float(input("Digite o primeiro valor: "))
    val2 = float(input("Digite o segundo valor: "))

    print("Escolha a operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    operacao = int(input("Digite o número da operação desejada (1-4): "))

    if operacao == 1:
        print(f"Resultado: {val1 + val2}")
    elif operacao == 2:
        print(f"Resultado: {val1 - val2}")
    elif operacao == 3:
        print(f"Resultado: {val1 * val2}")
    elif operacao == 4:
        if val2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            print(f"Resultado: {val1 / val2}")
    else:
        print("Operação inválida.")

    desejo = input("Deseja realizar outra operação? (sim/não): ")
    desejo = desejo.lower()
        
    if desejo != "sim":
        prosseguir = False
        print("Encerrando a calculadora. Até a próxima!")
