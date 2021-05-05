# misc project
# convert decimal number into binary

## to do: add gui, hex converter

import pyinputplus as pyip


def decToBinary(dNum, bRunningTotal):
    quotient, rem = divmod(dNum, 2)
    #print(quotient, rem)

    if rem == 0:
        bRunningTotal.insert(0, '0')
    elif rem > 0:
        bRunningTotal.insert(0, '1')
    print('running total = ' + ''.join(bRunningTotal))

    if quotient == 0:
        print('binary conversion:')
        print(''.join(bRunningTotal))
        return bRunningTotal
    else:
        decToBinary(quotient, bRunningTotal)



def binaryToDec(bNum, dRunningTotal):
    bNum.reverse()
    for i, v in enumerate(bNum):
        print(i, v, end=' ')
        print(int(v)*2**i)
        dRunningTotal.append(int(v)*2**i)
    x = sum(dRunningTotal)
    print('decimal conversion:\n' + str(x))
    return x


bRunningTotal = []
dRunningTotal = []

dNum = pyip.inputInt('enter a decimal number to convert to binary: ')
b = decToBinary(dNum, bRunningTotal)

bNum = pyip.inputInt('enter a binary number to convert to decimal: ')
d = binaryToDec(list(str(bNum)), dRunningTotal) # use list representation of bNum as parameter 



