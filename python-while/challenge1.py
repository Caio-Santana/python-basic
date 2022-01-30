import random

roll = random.randint(1, 5)
count = 0
number = 0

while roll != number:

    count += 1
    number = input('Guess a number between 1 and 5: ')
    
    if number.isnumeric():
        number = int(number)

else :
    print(f'You guessed it in {count} tries!')

 
