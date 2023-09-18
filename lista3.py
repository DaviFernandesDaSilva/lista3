sair = 0

while sair == 0:
    print("\nExercicios:")
    print("0 - Sair")
    print("1 - Dois numeros, maior ou igual")
    print("2 - Número Impar")
    print("3 - Ler 4 números inteiros e calcular soma dos pares")
    print("4 - Ler três valores e determinar o maior")
    print("5 - Calcular Raiz Quadrada de Positivo e se for Negativo dizer inválido")
    print("6 - Ler 3 notas e exibir medias")
    print("7 - Sálario do Trabalhador e Empréstimo")
    print("8 - Divisel por 3 ou por 5")
    print("9 - Ratos Golpistas")
    print("10 - Operações listadas")
    print("11 - Ordem crescente")
    print("12 - Dias da Semana")
    print("13 - Calculadora")

    escolha = input("Executar: ")
    # =======================================
    if escolha == "0":
        break
    if escolha == "1":
        # QUESTÃO 1
        # Faça um programa que receba dois números e imprima o maior deles, se por acaso os dois números
        # forem iguais, imprima a mensagem Números iguais.
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))

        if numero1 > numero2:
            print(f"{numero1} é maior")
        elif numero2 > numero1:
            print(f"{numero2} é maior")
        else:
            print("Os numeros são iguais")

    # =======================================
    elif escolha == "2":
        numero1 = int(input("Digite um numero: "))
        if (numero1 % 2 == 0):
            print("Par")
        else:
            print("Impar")
    # =======================================
    elif escolha == "3":
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))
        numero3 = int(input("Digite o terceiro numero: "))
        numero4 = int(input("Digite o quarto numero: "))
        numero1Par = 0
        numero2Par = 0
        numero3Par = 0
        numero4Par = 0
        soma = 0
        if numero1 % 2 == 0:
            numero1Par = numero1
        if numero2 % 2 == 0:
            numero2Par = numero2
        if numero3 % 2 == 0:
            numero3Par = numero3
        if numero4 % 2 == 0:
            numero4Par = numero4

        soma = numero1Par+numero2Par+numero3Par+numero4Par

        print(f"A Soma dos pares é {soma}")

    # =======================================
    elif escolha == "4":
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))
        numero3 = int(input("Digite o terceiro numero: "))

        if numero1 > numero2 and numero1 > numero3:
            print(f"Número 1: {numero1} é o maior")
        elif numero2 > numero1 and numero2 > numero3:
            print(f"Número 2: {numero2} é o maior")
        elif numero3 > numero2 and numero3 >= numero1:
            print(f"Número 3: {numero3} é o maior")
        elif numero1 == numero2:
            if numero2 == numero3:
                print("Todos os numeros são iguais")
            else:
                print(f"Número 1: {numero1} é igual a Número 2: {numero2}")
        elif numero2 == numero3:
            print(f"o Número 2: {numero2} é igual ao Número 3: {numero3}")
        else:
            print(f"o Número 1: {numero1} é igual a Número 3: {numero3}")
    # =======================================
    elif escolha == "5":
        numero1 = int(input("Digite um numero"))
        if numero1 >= 0:
            raiz = numero1**(1/2)
            print(f"a raiz do número positivo {numero1} é {raiz}")
        else:
            print("Número inválido")
    # =======================================
    elif escolha == "6":
        nota1 = float(input("Digite a primeira nota"))
        nota2 = float(input("Digite a segunda nota"))
        nota3 = float(input("Digite a terceira nota"))
    # valido é de 0.00 a 10.00
        if nota1 >= 0.00 and nota2 >= 0.00 and nota3 >= 0.00:
            if nota1 <= 10.00 and nota2 <= 10.00 and nota3 <= 10.00:
                media = float((nota1+nota2+nota3)/3)
                print(f"A média é {media}")
            else:
                print("Valores inválidos")

    # =======================================

    elif escolha == "7":
        salario = float(input("Digite o salário do trabalhador: "))
        parcela = float(input("Digite o valor da parcela do empréstimo: "))
        if ((salario*0.20) > parcela):
            print("Empréstimo Concedido")
        else:
            print("Empréstimo Negado")

    # =======================================
    elif escolha == "8":
        numero1 = int(print("Digite o número inteiro: "))  # type: ignore
        if numero1 % 3 == 0:
            print(f"{numero1} é divisivel or 3")
        elif numero1 % 3 == 0:
            print(f"{numero1} é divisivel por 3")
    # =======================================
    elif escolha == "9":
        print("ABAIXO A PRESIDÊNCIA!!!\n")
        Dfavor = int(input("Números de DEPURATOS a favor do GOLPE: "))
        Sfavor = int(input("Números de SENAROEDORES a favor do GOLPE: "))

        if Dfavor < 342:
            print("Colocaram Fogo na Câmara dos DepuRatos e Evitaram o Golpe")
        elif Dfavor>=342 and Sfavor<54:
            print("Homens Bombas Explodiram o Senado Federal e Evitaram o Golpe")
        elif Dfavor>=342 and Sfavor>=54:
            print("Nem Goku, nem Naruto e muitos menos os Vingadores. Tome Golpe.")
        else:
            print("Deus é bom.")
    # =======================================
    elif escolha == "10":
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))

        print("- - Operações para realizar - -")
        print("0 - Cancelar")
        print("1 - Média entre os números digitados")
        print("2 - Diferença do maior pelo menor")
        print("3 - Produto entre os números digitados")
        print("4 - Divisão do primeiro pelo segundo")
        escolha = int(input("Qual operação realizar? "))

        if escolha == 1:
            media = (primeiro_valor + segundo_valor)/2
            print(f"A média entre {primeiro_valor} e {segundo_valor} é {media}")
        elif escolha == 2:
            diferenca = (primeiro_valor - segundo_valor)
            print(f"A diferença entre {primeiro_valor} e {segundo_valor} é {diferenca}")
        elif escolha == 3:
            produto = (primeiro_valor * segundo_valor)
            print(f"A multiplicação entre {primeiro_valor} e {segundo_valor} resulta em {produto}")
        elif escolha == 4:
            divisao = (primeiro_valor / segundo_valor)
            print(f"A divisão entre {primeiro_valor} e {segundo_valor} resulta em {divisao}")
        elif escolha == 0:
            continue
        else:
            print("Inválido")

    # =======================================
    elif escolha == "11":
       #11. (Essa aqui tem analisar bem hehhe) Ler três valores e imprimi-los na tela em ordem crescente
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        valor3 = int(input("Digite o terceiro valor: "))

        if valor1 < valor3:
            valor1, valor3 = valor3, valor1

        if valor1 < valor2:
            valor1, valor2 = valor2, valor1

        if valor2 < valor3:
            valor2, valor3 = valor3, valor2

        print(f'A ordem crescente é {valor3}, {valor2} e {valor1}')
    # =======================================    
    elif escolha == "12":
#12. Usando if e elif , escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana
# correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante
        numero = input("Digite um número inteiro entre 1 e 7: ")
        if numero == 1:
            print("Domingo")
        elif numero == 2:
            print("Segunda-Feira")
        elif numero == 3:
            print("Terça-Feira")
        elif numero == 4:
            print("Quarta-Feira")
        elif numero == 5:
            print("Quinta-Feira")
        elif numero == 6:
            print("Sexta-Feira")
        elif numero == 1:
            print("Sábado")
        else:
            print("Inválido")
    # =======================================    
    elif escolha == "13":
# 3. Faça um programa que simule uma calculadora com as 4 operações básicas. O usuário digita o
# primeiro número, escolhe a operação e em seguida digita o segundo número, exatamente nessa ordem.
# O programação deve mostrar o resultado da operação
        
        print("--- Calculadora TOP 10 ---\n\n")

        numero1 = int(input("Digite o primeiro valor: "))

        print("Operações-")
        print("1 - Adição")
        print("2- Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Exponenciação")

        operacao = input("Escolha a operação: ")

        numero2 = int(input("Digite o segundo valor: "))

        if operacao == 1:
            print(f"A resposta é {numero1 + numero2}")
        elif operacao == 2:
            print(f"A resposta é {numero1 - numero2}")
        elif operacao == 3:
            print(f"A resposta é {numero1 * numero2}")
        elif operacao == 4:
            print(f"A resposta é {numero1 / numero2}")
        elif operacao == 5:
            print(f"A resposta é {numero1 ** numero2}")
        else:
            print("Inválido")


    # =======================================
    elif escolha == "14":
# z Faça um programa que leia um valor digitado pelo usuário e imprima os resultados com base na
# tabela.
        valor = int(input("Digite o valor: "))
        if valor == 1:
            print("Bom Dia / Boa Tarde / Boa Noite")
        elif valor == 2:
            print("Por Favor :) / Com Licença :D / Muito Obrigado ;)")
        elif valor == 3:
            print("Por Gentileza / Você poderia / Desculpe")
        elif valor == 4:
            print("Boa Sorte / Tenha Fé")
        else:
            print("Estudar vale muito a pena não é !?")
        
    # =======================================
    elif escolha == "15":
        print("")
        
    # =======================================
    else:
        print("Deus é bom")
