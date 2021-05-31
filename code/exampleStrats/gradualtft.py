import numpy as np
from random import random


def strategy(history, memory):
    currentCount,defector,hasDefected = (0,0,False) if memory is None else memory

    choice = 1
    if currentCount > 0:
        choice = 0
        currentCount -= 1
        return choice, (currentCount,defector,hasDefected)
    elif currentCount > -2:
        currentCount -= 1
        return choice, (currentCount,defector,hasDefected)
    else:
        hasDefected = False

    if history.shape[1] >= 1 and history[1,-1] == 0 and not hasDefected:
        choice = 0
        hasDefected = True
        currentCount = defector
        defector += 1

    return choice, (currentCount,defector,hasDefected)