resposta = input('Would you like to continue? ')
if (resposta == 'no') or (resposta == 'n'):
    print("Exiting")
elif (resposta == 'yes') or (resposta == 'y'):
    print("Continuing ...")
    print("Complete!")
else:
    print("Please try again and respond with yes or no.")