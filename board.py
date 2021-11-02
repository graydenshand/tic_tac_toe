from typing import Iterable, List, Tuple
import numpy as np


class Board:
    def __init__(self, board=None):
        if board:
            self._data = np.asarray(board)
            self._data.resize(3, 3)
        else:
            self._data = np.zeros((3, 3))
        self._state = None

    def __setitem__(self, position, value):
        if value not in (-1, 1):
            raise ValueError(f"Illegal value: {value}")
        if not isinstance(position, (Tuple, List)):
            raise ValueError(f"Illegal position (wrong type): {position}")
        if not (0 <= position[0] <= 2 and 0 <= position[1] <= 2):
            raise ValueError(f"Illegal position (out of bounds): {position}")
        if self[position] != 0.0:
            print(position, self[position], value)
            raise ValueError(f"Illegal position (already filled): {position}")
        self._data[position] = value

    def __getitem__(self, position):
        return self._data[position]

    def __str__(self) -> str:
        """
        O | X | X
        O | _ | _
        X | _ | O
        """
        d = self._data

        def render(i, j):
            if d[i, j] == 1:
                return "X"
            elif d[i, j] == 0:
                return "_"
            elif d[i, j] == -1:
                return "O"

        return f" {render(0,0)} | {render(0,1)} | {render(0,2)} \n {render(1,0)} | {render(1,1)} | {render(1,2)} \n {render(2,0)} | {render(2,1)} | {render(2,2)} "

    @property
    def state(self):
        self._state = str(self._data.reshape(9))
        return self._state
