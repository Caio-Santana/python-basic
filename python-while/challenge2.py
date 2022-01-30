import random

print("Guess a number between 1 and 10")

count = 0
guess = 0
roll = random.randint(1, 10)

while guess != roll:
    
    count += 1
    guess = input(f"Enter guess #{count}: ")
    if guess.isnumeric():
       guess = int(guess)
    else:
        print("Numbers only, please!")
    
    if guess < roll:
        print("Your guess is too low, try again!")
    elif guess > roll:
        print("Your guess is too high, try again!")
else:
    print(f"You guessed it in {count} tries!")