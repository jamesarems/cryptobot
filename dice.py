#Dice start program
import os
print('Welcome to Crypto Dice Game - Alpha')
print('Select your Operating system:(windows/linux)')
osSelect = input() ##User input
if osSelect == 'windows':
    os.system('python script/crypto_dice_win.py') #Redirect to windows settings
elif osSelect == 'linux':
    os.system('python script/crypto_dice.py') #Redirect to linux
elif osSelect == 'exit':
    exit()
else:
    print('Typo error')
    os.system('python dice.py')