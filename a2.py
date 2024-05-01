# DO NOT modify or add any import statements
from a2_support import *
import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Optional, Callable


# Name: Aditya Pradeep Rao
# Student Number: 48102344
# ----------------


class Tile(object):
    # docstrings
    def __init__(self):
        pass

    def get_tile_name(self) -> str:
        return TILE_NAME

    def is_blocking(self) -> bool:
        return False

    def __str__(self) -> str:
        return TILE_SYMBOL

    def __repr__(self) -> str:
        return f"{self.get_tile_name()}()"


class Ground(Tile):
    # docstrings
    def __init__(self):
        super().__init__()

    def get_tile_name(self) -> str:
        return GROUND_NAME

    def is_blocking(self) -> bool:
        return False

    def __str__(self) -> str:
        return GROUND_SYMBOL

    def __repr__(self) -> str:
        return f"{self.get_tile_name()}()"


class Mountain(Tile):

    def __init__(self):
        super().__init__()

    def get_tile_name(self) -> str:
        return MOUNTAIN_NAME

    def is_blocking(self) -> bool:
        return True

    def __str__(self) -> str:
        return MOUNTAIN_SYMBOL

    def __repr__(self) -> str:
        return f"{self.get_tile_name()}()"
"""

Tile should implement the following methods:

repr (self) -> str
Returns a machine readable string that could be used to construct an identical instance of the tile.

tile = Tile()
"""


class Building(Tile):


    def __init__(self, initial_health: int):
        super().__init__()
        self.health = initial_health

    def get_tile_name(self) -> str:
        return BUILDING_NAME

    def is_destroyed(self) -> bool:
        return self.health == 0

    def is_blocking(self) -> bool:
        return not self.is_destroyed()

    def damage(self, damage: int) -> None:
        # negative damage is supposed to heal the building
        # positive damage is supposed to damage the building
        # healing cannot be greater than 9 (max health)
        # damage cannot be less than minimum value
        # if damage is 1 and health is 5 it will make health 4
        # if damage is -1 and health is 5, 6
        # if damage is -10 and health is 5, 9
        # if damage is 10 and health is 5, 0

        if damage >= 0:
            if damage > self.health:
                self.health = 0
            else:
                self.health -= damage

        if damage < 0:
            if self.health - damage <= MAX_BUILDING_HEALTH:
                self.health -= damage
            else:
                self.health = MAX_BUILDING_HEALTH

    # go through the logic again

    def __str__(self) -> str:
        return str(self.health)

    def __repr__(self) -> str:
        return f"{self.get_tile_name()}({str(self.health)})"

"""
building = Building(5)

str(building)

building.damage(2)
print(str(building))
building.damage(20)
print(str(building))
print(str(building.is_destroyed()))
print(str(building.is_blocking()))
"""





class Board():

    def __init__(self, board: list[list[str]]) -> None:
        self.board = board


    def __str__(self):
        """
        Board([[' ', '4'], ['6', 'M']])
        >>> str(board)
        ' 4\n6M'

        """
        # need to access the individual elements and add them together
        # use a nested loop to access each element.
        # add the iterators and them return them concatenated with \n
        # ex. ("" + "\n")
        str_rep = ""
        for i in self.board:
            for j in i:
                str_rep += j
            str_rep += "\n"
        return str_rep

    def get_dimensions(self) -> tuple[int, int]:

        # dimension of columns will be based on each inner list
        # dimension of rows are based on number of values in outer list
        rows = len(self.board)
        columns = len(self.board[0])
        dimensions = (rows, columns)
        return dimensions
        #return (len(self.board), len(self.board[0]))


    def get_tile(self, position: tuple[int, int]) -> Tile:

        # have to access the numbers in the tuples
        # use those numbers as indices to find what values are in the list.
        # it should return the type of the tile and what's at the value.
        # m is mountain, " " is ground, int is building

        # self dot anything is a class property only to use across methods.

        outer_index = position[0] # 0
        inner_index = position[1] # 1

        value = self.board[outer_index][inner_index]) # 4

        if value
        # I need to attribute certain variable types to tile types using repr
        # then need to concatenate that with the value received from the indexation.








    #def get_buildings(self) -> dict[tuple[int, int], Building]:



tiles = [[" ","4"],["6","M"]]
board1 = Board(tiles)

print(board1)
print(str(board1))

print(board1.get_dimensions())
board1.get_tile((0,1))
#Building(4)










def main() -> None:
    """The main function"""
    pass


if __name__ == "__main__":
    main()
