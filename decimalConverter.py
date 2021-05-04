# misc project
# convert decimal number into binary

## to do: bin to dec, hex converter

import pyinputplus as pyip


def binaryConv(num, runningTotal):
    quotient, rem = divmod(num, 2)
    print(quotient, rem)

    if rem == 0:
        runningTotal = '0' + runningTotal
    elif rem > 0:
        runningTotal = '1' + runningTotal
    print('running total = ' + runningTotal)

    if quotient == 0:
        return runningTotal
    else:
        binaryConv(quotient, runningTotal)


num = pyip.inputNum()
runningTotal = ''
output = binaryConv(num, runningTotal)



