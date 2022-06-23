import random

import numpy as np

MINE_PROXIMITY = 10
MINE = 1

LEFT_SUM_MATRICES = {
    2: np.ones((1, 2), dtype=np.int8),
    3: np.ones((1, 3), dtype=np.int8),
}
RIGHT_SUM_MATRICES = {
    2: np.ones((2, 1), dtype=np.int8),
    3: np.ones((3, 1), dtype=np.int8),
}


class Minefield:
    def __init__(self, rows, columns, number_of_mines) -> None:
        self.rows = rows
        self.columns = columns
        self.number_of_mines = number_of_mines
        self.proximity_matrix = self.generate_board()

    def generate_board(self) -> np.ndarray:
        """Create a 2D matrix of the Tile sprites."""
        raw_minefield = self.get_mine_list()
        return self.create_proximity_matrix(raw_minefield)

    def get_mine_list(self) -> np.ndarray:
        """Create a zero'd 2D matrix and populate with mines."""
        raw_minefield = np.zeros((self.rows, self.columns), dtype=np.int8)

        for mine in self.generate_mines():
            row, column = mine
            raw_minefield[row][column] = MINE

        return raw_minefield

    def generate_mines(self) -> list[tuple[int, int]]:
        """Generate a list of random numbers to place mines.
        Returns a list of tuples of the row and column for the mines."""
        mines = []

        for mine in random.sample(
            range(self.rows * self.columns), self.number_of_mines
        ):
            row = mine // self.columns
            column = mine % self.columns
            mines.append((row, column))

        return mines

    def calculate_proximity(
        self, row: int, column: int, raw_minefield: np.ndarray
    ) -> int:
        """Return the mine proximity for a given tile's row and column.

        Mine tiles return an invalid value."""

        if raw_minefield[row][column] == MINE:
            return MINE_PROXIMITY

        sliced_mines = self.get_slice(row, column, raw_minefield)

        # Get summing matrices based on the size of the sliced mine matrix.
        box_rows, box_columns = sliced_mines.shape
        left_sum_matrix = LEFT_SUM_MATRICES[box_rows]
        right_sum_matrix = RIGHT_SUM_MATRICES[box_columns]

        # Mine proximity is [1,X] ⋅ [X,Y] ⋅ [Y,1] which
        # results in a 2D 1x1 matrix containing the sum of mines.
        proximity = left_sum_matrix.dot(sliced_mines).dot(right_sum_matrix)[0][0]

        return proximity

    def get_slice(self, row: int, column: int, minefield: np.ndarray) -> np.ndarray:

        left_bound, right_bound, top_bound, bottom_bound = self.get_slice_bounds(
            row, column
        )

        return minefield[top_bound : bottom_bound + 1, left_bound : right_bound + 1]

    def get_slice_bounds(self, row: int, column: int):
        """Get the boundaries for a 3x3 grid around a given row, column
        in the minefield."""
        left_bound = column if column == 0 else column - 1
        right_bound = column if column == self.columns - 1 else column + 1

        top_bound = row if row == 0 else row - 1
        bottom_bound = row if row == self.rows - 1 else row + 1

        return (left_bound, right_bound, top_bound, bottom_bound)

    def create_proximity_matrix(self, raw_minefield: np.ndarray) -> np.ndarray:
        """Use the 2D array of mines to create the mine proximity map"""
        minefield = np.ndarray(raw_minefield.shape, dtype=np.int8)

        for row in range(self.rows):
            for column in range(self.columns):
                minefield[row][column] = self.calculate_proximity(
                    row, column, raw_minefield
                )

        return minefield

    def check_for_cascade(
        self, row: int, column: int, need_to_click: set
    ) -> set[tuple[int, int]]:
        """Make a set of contiguous non-mine tiles.

        Given a row/column of a 0 proximity tile, create a set of all continguous
        0 proximity tiles as well as their non-0 proximity bordering tiles centered
        at row/column. Recursively checks any other 0 proximity tiles found."""

        left_bound, right_bound, top_bound, bottom_bound = self.get_slice_bounds(
            row, column
        )

        for row_index in range(top_bound, bottom_bound + 1):
            prox_row = self.proximity_matrix[row_index]
            for col_index in range(left_bound, right_bound + 1):
                proximity = prox_row[col_index]
                if row_index == row and col_index == column:
                    continue

                if proximity < 10 and (row_index, col_index) not in need_to_click:
                    need_to_click.add((row_index, col_index))
                    if proximity == 0:
                        self.check_for_cascade(row_index, col_index, need_to_click)

        return need_to_click
