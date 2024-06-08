# Solicitar ao usuário digitar dois números

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Cálculo aritmético

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisao_int = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

# Exibição resultado

print ("\n Resultados das operações aritméticas: ")
print ("Soma:", soma)
print ("Subtração:", subtracao)
print ("Multiplicação:", multiplicacao)
print ("Divisão:", divisao)
print ("Divisão inteira:", divisao_int)
print ("Módulo:", modulo)
print ("Potência:", potencia)

# Comparação com operadores
print ("\n Resultados das operações com comparação:")
print ("Igualdade: ", num1 == num2)
print ("Diferença: ", num1 != num2)
print ("Maior que:", num1 > num2)
print ("Menor que:", num1 < num2)
print ("Maior ou igual a:", num1 >= num2)
print ("Mneor ou igual a:", num1 <= num2)

# Operadores de atribuição
print('\n Resultados dos Operadores de atribuição:')
num1 += 5
print('num1 += 5:', num1)
num2 /= 2
print('num2 /= 2:', num2)
#Verificar presença na lista de elementos
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if num1 in lista_numeros:
    print(f'o número {num1} está na lista de numeros')
else:
    print(f'o número {num1} não está na lista de números')
# Compare a identidade de objetos
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print('\n Resultados das operações de identidade de objetos:')
print('x is z:', x is z)
print('x is y:', x is y)
print('x is not y:', x is not y)