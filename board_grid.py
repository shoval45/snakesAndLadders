import consts

grid = [['empty'] * (consts.LENGTH_GRID) for i in range(consts.LENGTH_GRID)]

grid[consts.LENGTH_GRID - 1][0] = 'player'
grid[0][consts.LENGTH_GRID - 1] = 'end'
