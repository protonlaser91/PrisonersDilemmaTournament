import random
import numpy as np




def strategy(history, memory):
    if memory is False: # forceful coop
        memory = True
        return 1,memory

    choice = 1
    n = 10
    if n > history.shape[1]:
        if history.shape[1] >= 1 and history[1, -1] == 0:  # Choose to defect if and only if the opponent just defected.
            return 0,memory
        else:
            return choice,memory

    #oppMoves = history[1][-12:] #last 12
    oppMoves = history[1][:n]
    if np.count_nonzero(oppMoves) <= 6: # 80% chance this is random or full defection (in which case we do not spare)
        return 0,memory

    if history[1, -1] == 0:  # Choose to defect if and only if the opponent just defected.
        memory = False
        choice = 0
    return choice,memory