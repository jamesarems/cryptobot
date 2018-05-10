# Crypto dice program
import random
import subprocess
import sys

subprocess.call(['clear'])
myBalance = '0.01'  # User balance
entReq = '0.001'
# randomDice = random.randint(0, 1)
print('###### WELCOME TO CRYPTO BITCOIN DICE GAME ###########')
print('Support us by donating BTC to develop dice bot more with graphical interface')
print('1GAN8kbtkPuLV2srrtLiAaikmqj21Q2wXF') # Donation BTC address
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('Your current balance is ', end='')
print(myBalance, end=' '),
print('BTC')


def chkBal(btc):
    #subprocess.call(['clear'])
    print('Checking your eligibility')
    #print('###Debug btc', btc)
    if btc < entReq:
        print('Your balance is not sufficient for this game.Come back when you got money')
        exit()
    else:
        #print('******************************************************')
        print('Try your luck now!')
        game(btc)


def game(crypto):
    for CryptoG in range(1, 50):
        randomDice = random.randint(0, 1)
        print('******************************************************')
        #print(randomDice)
        #print('####Debug crypto', crypto)
        print('Enter 0 or 1')
        userDice = input()
        #print(userDice)
        if userDice == 'exit':
                exitPrg()
        elif float(userDice) == float(randomDice):
            print('You Won!')
            newBal = str(float(crypto) + float(0.001))
            newTry(newBal)
        else:
            print('You loose')
            newBala = str(float(crypto) - float(0.001))
            #print('Debug', newBala)
            newTryfail(newBala)


def newTry(btcTrue):
    subprocess.call(['clear'])
    print('Your new balance is', end='')
    print(btcTrue, end=' ')
    print('BTC')
    game(btcTrue)


def newTryfail(btcFail):
    subprocess.call(['clear'])
    print('Your new balance is', end='')
    print(btcFail, end=' '),
    print('BTC')
    chkBal(btcFail)

def exitPrg():
    print('Dont worry, we all humens are facing this problem..be a programmer and hire a good job and make money man. Then come here.')

chkBal(myBalance)
