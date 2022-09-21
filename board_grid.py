import consts

initialized_value = {
    "type": "empty"
}
grid = [[initialized_value] * (consts.LENGTH_GRID) for i in range(consts.LENGTH_GRID)]

def initialize_value_start():
    grid[consts.LENGTH_GRID - 1][0]["type"] = "player"
    grid[0][consts.LENGTH_GRID - 1]["type"] = "end"
    enter_snakes_value_into_grid()

# entering snakes value into grid
def enter_snakes_value_into_grid():
    grid[6][1]["type"] = "snake"
    grid[6][1].update({"end_index": [4, 3]})

    grid[4][5]["type"] = "snake"
    grid[4][5].update({"end_index": [2, 3]})

    grid[2][1]["type"] = "snake"
    grid[2][1].update({"end_index": [0, 3]})
    enter_ladders_value_into_grid()

# entering ladders value into grid
def enter_ladders_value_into_grid():
    grid[6][4]["type"] = "ladder"
    grid[6][4].update({"end_index": [4, 6]})

    grid[5][0]["type"] = "ladder"
    grid[5][0].update({"end_index": [3, 2]})

    grid[3][6]["type"] = "ladder"
    grid[3][6].update({"end_index": [1, 4]})

def returned_initialized_grid():
    initialize_value_start()
    return grid



