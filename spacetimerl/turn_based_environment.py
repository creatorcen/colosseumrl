from spacetimerl.base_environment import BaseEnvironment

from abc import ABC, abstractmethod
from typing import Tuple, List, Union
import numpy as np


class TurnBasedEnvironment(ABC):
    @property
    @abstractmethod
    def min_players(self) -> int:
        """ Property holding the number of players present required to play game. """
        raise NotImplementedError

    @property
    @abstractmethod
    def max_players(self) -> int:
        """ Property holding the max number of players present for a game. """
        raise NotImplementedError

    @property
    @abstractmethod
    def state_shape(self) -> tuple:
        """ Property holding the numpy shape of a single state. """
        raise NotImplementedError

    @property
    @abstractmethod
    def observation_shape(self) -> tuple:
        """ Property holding the numpy shape of a transformed observation state. """
        raise NotImplementedError

    @abstractmethod
    def new_state(self, num_players: int = 1) -> object:
        """ Create a fresh state. This could return a fixed object or randomly initialized on, depending on the game.

        Returns
        -------
        new_state : np.ndarray
            A state for the new game.
        new_players: [int]
            List of players whos turn it is now.
        """
        raise NotImplementedError

    @abstractmethod
    def next_state(self, state: object, player: int, action: str) \
            -> Tuple[object, float, bool, Union[int, None]]:
        raise NotImplementedError

    @abstractmethod
    def valid_actions(self, state: object) -> [str]:
        """ Valid actions for a specific state. """
        raise NotImplementedError

    @abstractmethod
    def is_valid_action(self, state: object, action: str) -> bool:
        """ Valid actions for a specific state. """
        raise NotImplementedError

    def state_to_observation(self, state: object, player: int) -> np.ndarray:
        """ Convert the raw game state to the observation for the agent.
        The observation must be able to be fed into your predictor.

        This can return different values for the different players. Default implementation is just the identity."""
        return np.array(state)

class TurnBasedWrapper(BaseEnvironment):
    def __init__(self, base: TurnBasedEnvironment):
        self.base = base

    @property
    def min_players(self) -> int:
        return self.base.min_players

    @property
    def max_players(self) -> int:
        return self.base.max_players

    @property
    def state_shape(self) -> tuple:
        return self.base.state_shape

    @property
    def observation_shape(self) -> tuple:
        return self.base.observation_shape

    def new_state(self, num_players: int = 1) -> Tuple[object, List[int]]:
        return (num_players, self.base.new_state(num_players)), [0]

    def next_state(self, state: object, players: [int], actions: [str]) -> Tuple[
        object, List[int], List[float], bool, Union[List[int], None]]:
        return self.base.next_state(state)

    def valid_actions(self, state: object) -> [str]:
        pass

    def is_valid_action(self, state: object, action: str) -> bool:
        pass

    def state_to_observation(self, state: object, player: int) -> np.ndarray:
        return super().state_to_observation(state, player)

