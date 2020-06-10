WIDTH = 210.0
HEIGHT = 297.0

CELLS_PER_ROW = 3
CELLS_PER_COLUMN = 15

CELLS_PER_PAGE = CELLS_PER_ROW * CELLS_PER_COLUMN

MARGIN = 10.0

CELL_WIDTH = (WIDTH - 2 * MARGIN) / CELLS_PER_ROW
CELL_HEIGHT = (HEIGHT - 2 * MARGIN) / CELLS_PER_COLUMN

# setup with 4 subcells per cell, resulting in four rows per cell
SUB_CELL_HEIGHT = CELL_HEIGHT / 4

SUB_CELL_WIDTH_A = CELL_WIDTH * 0.35
SUB_CELL_WIDTH_B = CELL_WIDTH * 0.65