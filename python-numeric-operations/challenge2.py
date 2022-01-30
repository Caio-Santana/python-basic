# Crie uma calculadora simples que aceita um primeiro número, uma operação e um segundo número

print('Simple calculator!')

first_number = input('First number? ')
if first_number.isnumeric() == False:
    print('Please input a number.')
    exit()

operation = input('Operation? ')
if operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '**' and operation != '%':
    print('Operation not recognized.')
    exit()

second_number = input('Second number? ')
if second_number.isnumeric() == False:
    print('Please input a number.')
    exit()

resultado = 0
label = ''

if operation == '+':
    resultado = int(first_number) + int(second_number)
    label = 'sum'
elif operation == '-':    
    resultado = int(first_number) - int(second_number)
    label = 'diference'
elif operation == '*':
    resultado = int(first_number) * int(second_number)
    label = 'product'
elif operation == '/':
    resultado = int(first_number) / int(second_number)
    label = 'quociente'
elif operation == '**':
    resultado = int(first_number) ** int(second_number)
    label = 'expoente'
elif operation == '%':
    resultado = int(first_number) % int(second_number)
    label = 'diference'

print(label + ' of ' + first_number + ' ' + operation + ' ' + second_number + ' equals ' + str(resultado))    
