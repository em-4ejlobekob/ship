from Game import Game
import Cell


class Field(Game):
    def __init__(self):
        Game.__init__(self)
        self.field_cells = []
        for x in range(0, self.field_size):
            for y in range(0, self.field_size):
                self.field_cells[x][y] = Cell(x, y)
