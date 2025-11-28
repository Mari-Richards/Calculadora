# Programa que pede que o usuário digite dois números e escolha a operação que irá realizar o cálculo

# Entrada de valores
valor1 = float(input("Insira o primeiro valor:\n"))
valor2 = float(input("Insira o segundo valor:\n"))

# Menu de operações
print("Escolha uma operação:")
print("Digite 1 para somar:")
print("Digite 2 para subtrair:")
print("Digite 3 para multiplicar:")
print("Digite 4 para dividir:")

# Entrada da operação
op = int(input())

# Processamento
if op == 1:
    resultado = valor1 + valor2
    print("A soma é:", resultado)

elif op == 2:
    resultado = valor1 - valor2
    print("A subtração é:", resultado)
elif op == 3:
    resultado = valor1 * valor2
    print("A multiplicação é:", resultado)
elif op == 4:
    if valor2 == 0:
        print("Erro: não é possível dividir por zero!")
    else:
        resultado = valor1 / valor2
        print("A divisão é:", resultado)
else:
    print("Opção inválida.")
