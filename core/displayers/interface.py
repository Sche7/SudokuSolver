from abc import ABC, abstractmethod

from nptyping import NDArray


class DisplayInterface(ABC):
    """Interface for displayers"""

    @abstractmethod
    def display(self, board: NDArray):
        """
        Method for displaying a board.
        """
        raise NotImplementedError

    @abstractmethod
    def initialize(self):
        """
        Method for initializing displayer
        """
        raise NotImplementedError

    @abstractmethod
    def close(self):
        """
        Method for closing displayer
        """
        raise NotImplementedError
