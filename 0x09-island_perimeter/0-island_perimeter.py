#!/usr/bin/python3
"""Island perimeter calculating module.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    
    :param grid: List[List[int]] - 2D list representing the island grid.
                   0 represents water and 1 represents land.
    :return: int - The perimeter of the island.
    """
    rows = len(grid)
    if rows == 0:
        return 0

    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell adds 4 to the perimeter
                perimeter += 4

                # If the cell above is also land, it reduces the perimeter by 2
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # If the cell to the left is also land, it reduces the perimeter by 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
