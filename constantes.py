from random import randint
import time
import math


def random_value(a, b):
    #start = time.clock()
    # while time.clock() - start < 0.2:
    #    random_number = randint(a, b)
    # return random_number
    return randint(a, b)


sizeCromossomo = 9
sizePopulacao = 500
functrinXSize = 2 ** sizeCromossomo


def function(x):
    calc = 100 + abs(x * math.sin(math.sqrt(abs(x))))
    return calc
