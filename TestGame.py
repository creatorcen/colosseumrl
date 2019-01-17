from typing import Tuple

import numpy as np

from Environment import BaseEnvironment

class TestGame(BaseEnvironment):
    @property
    def state_shape(self) -> tuple:
        return 1,

    @property
    def observation_shape(self):
        return 1,

    def new_state(self, num_players = 1) -> np.ndarray:
        return np.random.randint(0, 100, (1,))

    def add_player(self, state: np.ndarray):
        return state

    def next_state(self, state: np.ndarray, player: int, action: int) -> Tuple[np.ndarray, float, bool, int]:
        distance = -np.abs(action - state[0])
        if action == state[0]:
            return state, distance, True, player
        return state, distance, False, -1

    def valid_actions(self, state: np.ndarray) -> [int]:
        return np.arange(100)

    def state_to_observation(self, state: np.ndarray, player: int) -> np.ndarray:
        return np.array([0])