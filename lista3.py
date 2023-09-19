import time

sair = 0

while sair == 0:
    time.sleep(1)
    print("\033[37m\n\nExercicios:")
    print("\033[33m0 - Sair")
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
    print("14 - Frase no Valor")
    print("15 - Equação de Segundo Grau")
    print("16 - Triangulo")
    print("17 - Aposentadoria")
    print("18 - Ano Bissexto")

    escolha = input("\033[37mExecutar: ")
    # =======================================
    # SAIR =======================================

    if escolha == "0":

        print("\033[32mPrograma finalizado.\033[37m")

        break

    # =======================================
    # QUESTÃO 1 =======================================

    if escolha == "1":

        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))

        if numero1 > numero2:
            print(f"\033[32m{numero1} é maior")
        elif numero2 > numero1:
            print(f"\033[32m{numero2} é maior")
        else:
            print("\033[32mOs numeros são iguais")
        
    # =======================================
    # QUESTÃO 2 =======================================

    elif escolha == "2":

        numero1 = int(input("Digite um numero: "))

        if (numero1 % 2 == 0):
            print("\033[32mPar")
        else:
            print("\033[32mImpar")

    # =======================================
    # QUESTÃO 3 =======================================

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

        print(f"\033[32mA Soma dos pares é {soma}")

    # =======================================
    # QUESTÃO 4 =======================================

    elif escolha == "4":

        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))
        numero3 = int(input("Digite o terceiro numero: "))

        if numero1 > numero2 and numero1 > numero3:
            print(f"\033[32mNúmero 1: {numero1} é o maior")
        elif numero2 > numero1 and numero2 > numero3:
            print(f"\033[32mNúmero 2: {numero2} é o maior")
        elif numero3 > numero2 and numero3 >= numero1:
            print(f"\033[32mNúmero 3: {numero3} é o maior")
        elif numero1 == numero2:
            if numero2 == numero3:
                print("\033[32mTodos os numeros são iguais")
            else:
                print(f"\033[32mNúmero 1: {numero1} é igual a Número 2: {numero2}")
        elif numero2 == numero3:
            print(f"\033[32mo Número 2: {numero2} é igual ao Número 3: {numero3}")
        else:
            print(f"\033[32mo Número 1: {numero1} é igual a Número 3: {numero3}")

    # =======================================
    # QUESTÃO 5 =======================================
    
    elif escolha == "5":

        numero1 = int(input("Digite um numero: "))
        if numero1 >= 0:
            raiz = numero1**(1/2)
            print(f"\033[32ma raiz do número positivo {numero1} é {raiz}")
        else:
            print("\033[31mNúmero inválido")

    # =======================================
    # QUESTÃO 6 =======================================

    elif escolha == "6":

        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))

        if nota1 >= 0.00 and nota2 >= 0.00 and nota3 >= 0.00:
            if nota1 <= 10.00 and nota2 <= 10.00 and nota3 <= 10.00:
                media = float((nota1+nota2+nota3)/3)
                print(f"\033[32mA média é {media}")
            else:
                print("\033[31mValores inválidos")

    # =======================================
    # QUESTÃO 7 =======================================

    elif escolha == "7":
        salario = float(input("Digite o salário do trabalhador: "))
        parcela = float(input("Digite o valor da parcela do empréstimo: "))

        if ((salario*0.20) > parcela):
            print("\033[32mEmpréstimo Concedido")
        else:
            print("\033[31mEmpréstimo Negado")

    # =======================================
    # QUESTÃO 8 =======================================

    elif escolha == "8":

        numero1 = int(print("Digite o número inteiro: "))  # type: ignore
        if numero1 % 3 == 0:
            print(f"\033[32m{numero1} é divisivel or 3")
        elif numero1 % 3 == 0:
            print(f"\033[32m{numero1} é divisivel por 3")

    # =======================================
    # QUESTÃO 9 =======================================

    elif escolha == "9":

        print("ABAIXO A PRESIDÊNCIA!!!\n")
        Dfavor = int(input("Números de DEPURATOS a favor do GOLPE: "))
        Sfavor = int(input("Números de SENAROEDORES a favor do GOLPE: "))

        if Dfavor < 342:
            print("\033[32mColocaram Fogo na Câmara dos DepuRatos e Evitaram o Golpe")
        elif Dfavor>=342 and Sfavor<54:
            print("\033[32mHomens Bombas Explodiram o Senado Federal e Evitaram o Golpe")
        elif Dfavor>=342 and Sfavor>=54:
            print("\033[32mNem Goku, nem Naruto e muitos menos os Vingadores. Tome Golpe.")
        else:
            print("Deus é bom.")

    # =======================================
    # QUESTÃO 10 =======================================

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
            print(f"\033[32mA média entre {primeiro_valor} e {segundo_valor} é {media}")
        elif escolha == 2:
            diferenca = (primeiro_valor - segundo_valor)
            print(f"\033[32mA diferença entre {primeiro_valor} e {segundo_valor} é {diferenca}")
        elif escolha == 3:
            produto = (primeiro_valor * segundo_valor)
            print(f"\033[32mA multiplicação entre {primeiro_valor} e {segundo_valor} resulta em {produto}")
        elif escolha == 4:
            divisao = (primeiro_valor / segundo_valor)
            print(f"\033[32mA divisão entre {primeiro_valor} e {segundo_valor} resulta em {divisao}")
        elif escolha == 0:
            continue
        else:
            print("\033[31mInválido")

    # =======================================
    # QUESTÃO 11 =======================================

    elif escolha == "11":

        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        valor3 = int(input("Digite o terceiro valor: "))

        if valor1 < valor3:
            valor1, valor3 = valor3, valor1

        if valor1 < valor2:
            valor1, valor2 = valor2, valor1

        if valor2 < valor3:
            valor2, valor3 = valor3, valor2

        print(f'\033[32mA ordem crescente é {valor3}, {valor2} e {valor1}')
    # =======================================
    # QUESTÃO 12 =======================================

    elif escolha == "12":

        numero = int(input("Digite um número inteiro entre 1 e 7: "))
        if numero == 1:
            print("\033[32mDomingo")
        elif numero == 2:
            print("\033[32mSegunda-Feira")
        elif numero == 3:
            print("\033[32mTerça-Feira")
        elif numero == 4:
            print("\033[32mQuarta-Feira")
        elif numero == 5:
            print("\033[32mQuinta-Feira")
        elif numero == 6:
            print("\033[32mSexta-Feira")
        elif numero == 1:
            print("\033[32mSábado")
        else:
            print("\033[31mInválido")
    # =======================================
    # QUESTÃO 13 =======================================

    elif escolha == "13":
        
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
            print(f"\033[32mA resposta é {numero1 + numero2}")
        elif operacao == 2:
            print(f"\033[32mA resposta é {numero1 - numero2}")
        elif operacao == 3:
            print(f"\033[32mA resposta é {numero1 * numero2}")
        elif operacao == 4:
            print(f"\033[32mA resposta é {numero1 / numero2}")
        elif operacao == 5:
            print(f"\033[32mA resposta é {numero1 ** numero2}")
        else:
            print("\033[31mInválido")


    # =======================================
    # QUESTÃO 14 =======================================

    elif escolha == "14":

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
    # QUESTÃO 15 =======================================

    elif escolha == "15":

        print("")
        print("Resolvedor de Equações do Segundo Grau")
        print("ax^2 + bx + c = 0")
        print("")
        a = int(input("Insira o valor a da sua equação: "))
        b = int(input("Insira o valor b da sua equação: "))
        c = int(input("Insira o valor c da sua equação: "))

        delta = (b**2)-(4*a*c)

        if a == 0:
            print("\033[31mNão é equação do 2º grau")
        elif delta<0:
            print("\033[31mNão existe raiz real")
        elif delta==0:
            raiz = (-(b))/(2*a)
            print(f"\033[32m{raiz}")
            print("\033[32mRaiz única")
        elif delta>0:
            raizA = ( (-(b))+(delta**(1/2))) /(2*a)
            raizB = ( (-(b))-(delta**(1/2))) /(2*a)
            print("\033[32mDuas Raizes")
            print(f"\033[32m{raizA} e {raizB}")
        else:
            print("\033[32mValores inválidos")

    # =======================================
    # QUESTÃO 16 =======================================

    elif escolha == "16":

        a = int(input("Valor A: "))
        b = int(input("Valor B: "))
        c = int(input("Valor C: "))
        if a<(b+c) and b<(a+c) and c<(b+a):
            print("É triangulo")
            if a==b or b==c:
                print("\033[32mValores de um triângulo isóceles")
            elif a==b and b==c:
                print("\033[32mValores de um triângulo equilátero")
            else:
                print("\033[32mValores de um triângulo escaleno")
        else:
            print("\033[31mIsso não é um triângulo")
    # =======================================
    # QUESTÃO 17 =======================================

    elif escolha == "17":

        idade_trabalhador = int(input("Digite a idade do trabalhador: "))
        tempo_servico = int(input("Digite o tempo de serviço do trabalhador: "))
        if idade_trabalhador>=65:
            print("\033[32mPode se aposentar")
        elif tempo_servico>=30:
            print("\033[32mPode se aposentar")
        elif idade_trabalhador>=60 and tempo_servico>=25:
            print("\033[32mPode se aposentar")
        else:
            print("\033[31mNão irá se aposentar")

    # =======================================
    # QUESTÃO 18 =======================================

    elif escolha == "18":

        ano = int(input("Digite o ano: "))
        if ano%400==0 or (ano%4==0 and ano%100!=0):
            print("\033[32mAno bissexto\033[37m")
        else:
            print("\033[31mAno convencional\033[37m")

    # =======================================
    else:
        print("Deus é bom")
