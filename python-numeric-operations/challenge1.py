# celsius = (fahrenheit - 32) * 5/9

fahrenheit = input('What is the temperature in fahrenheit? ')

if fahrenheit.isnumeric():
    celsius = int((int(fahrenheit) - 32) * 5/9)
    print('Temperature in celsius is ' + str(celsius))
else:
    print('Input is not a number.')