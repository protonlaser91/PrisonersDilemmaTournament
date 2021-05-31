import numpy as np
from random import random

def strategy(history, memory):
    if history.shape[1] == 0: # We're on the first turn!
        choice = 1
    else:
        prob = np.mean(history[1])
        choice = int(random() < prob)



   # prob = np.average(history[1],weights=[1 if a == 1 else 1 for a in history[1]])
    #choice = int(random() < prob)

    return choice, None