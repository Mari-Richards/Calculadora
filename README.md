Calculadora em Python

Este projeto é uma calculadora simples em Python, criada para treinar conceitos básicos de programação, como:

Entrada de dados pelo teclado

Conversão de tipos (float e int)

Estruturas condicionais (if, elif, else)

Tratamento de erros (divisão por zero)

Saída formatada para o usuário

O objetivo é permitir que o usuário insira dois números e escolha a operação matemática que deseja realizar.

Como o programa funciona

O programa solicita que o usuário digite dois valores numéricos
Esses valores são convertidos para float, permitindo operações com números decimais.

Apresenta um menu de operações matemáticas
O usuário pode escolher uma das seguintes opções:

1 → Soma
2 → Subtração
3 → Multiplicação
4 → Divisão


O programa lê a escolha do usuário
A entrada é convertida para int, permitindo comparar a opção escolhida.

O cálculo é realizado com base na operação selecionada
O código utiliza condições (if/elif/else) para determinar qual operação executar.

Validação na divisão por zero
Caso o usuário tente dividir um número por zero, o programa exibe uma mensagem de erro.

Exibe o resultado da operação
O valor final é impresso na tela para o usuário.

Exemplo de uso
Insira o primeiro valor:
10
Insira o segundo valor:
5

Escolha uma operação:
Digite 1 para somar
Digite 2 para subtrair
Digite 3 para multiplicar
Digite 4 para dividir
Sua escolha: 1

Resultado: 15.0

Código do programa
# Programa que pede que o usuário digite dois números e escolha uma operação

# Entrada dos valores
valor1 = float(input("Insira o primeiro valor:\n"))
valor2 = float(input("Insira o segundo valor:\n"))

# Menu de operações
print("\nEscolha uma operação:")
print("Digite 1 para somar")
print("Digite 2 para subtrair")
print("Digite 3 para multiplicar")
print("Digite 4 para dividir")

# Entrada da operação
op = int(input("Sua escolha: "))

# Processamento
if op == 1:
    resultado = valor1 + valor2
    print(f"\nResultado: {resultado}")

elif op == 2:
    resultado = valor1 - valor2
    print(f"\nResultado: {resultado}")

elif op == 3:
    resultado = valor1 * valor2
    print(f"\nResultado: {resultado}")

elif op == 4:
    if valor2 == 0:
        print("\nErro: não é possível dividir por zero!")
    else:
        resultado = valor1 / valor2
        print(f"\nResultado: {resultado}")

else:
    print("\nOpção inválida!")

Objetivo do projeto

Este projeto ajuda iniciantes a praticar:

entrada e saída de dados

conversão de tipos

manipulação de números

estruturas condicionais

lógica de programação
