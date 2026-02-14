operacao = input('''Digite um dos símbolos a seguir: +,-,/,*,% ou ^ (para potenciação)
Qual operação vai ser realizada? ''')

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

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