# Validador de triângulo

# Apresentação


print('\n\t\t\t -- Validador de Triângulo --\n\n')

# Entrada
a = int(input('Informe o lado a: '))
b = int(input('Informe o lado b: '))
c = int(input('Informe o lado c: '))

# Processamento e saída
if a < (b + c) and b < (a + c) and c < (a + b):
    print(f'\n\n{a}, {b} e {c} formam um triângulo!')
else:
    print(f'\n\n{a}, {b} e {c} NÃO formam triângulo.')