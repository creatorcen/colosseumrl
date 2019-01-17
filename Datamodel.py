from rtypes import pcc_set, merge
from rtypes import dimension, primarykey
import numpy as np
import random, sys

class Player:
    pid = primarykey(int)

    number = dimension(int)
    action = dimension(int)
    turn = dimension(bool)

    ready = dimension(bool)
    winner = dimension(bool)

    state = dimension(str)

    def __init__(self):
        self.pid = random.randint(0, sys.maxsize)

        self.number = 0
        self.action = 0
        self.turn = False
        self.ready = False
        self.winner = False

        self.state = ""

    def finalize_player(self, number, state):
        self.number = number
        self.state = state.tostring()

    def set_state(self, state: np.ndarray):
        self.state = state.tostring()
