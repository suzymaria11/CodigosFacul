import math

while True:
    operacao = input('''Operações: 
    + - adição          % - resto
    - - subtração       ^ - potência 
    / - divisão         r - raiz quadrada
    * - multiplicação   f - fatorial               
    Qual operação vai ser realizada (ou 'sair' para encerrar)? ''')
    
    if operacao.lower() == 'sair':
        print("Até mais")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao not in ['+', '-', '*', '/', '%', '^']:
        print("Erro na operação. Digite novamente um dos símbolos a seguir: +,-,/,*,% ou ^ (para potenciação)")
    elif operacao == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacao == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operacao == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Divisão por zero não é possível.")
    elif operacao == '%':
        print(f"{num1} % {num2} = {num1 % num2}")
    elif operacao == '^':
        print(f"{num1} ^ {num2} = {num1 ** num2}")
    elif operacao == 'r':
        print(f"√{num1} = {math.sqrt(num1)}")
    elif operacao == '!':
        print(f"{int(num1)}! = {math.factorial(int(num1))}")


    continuar = input("Deseja fazer outra conta? (Sim ou Não): ")
    if continuar.upper() != "Sim":
        print("Operações encerradas.")
        break