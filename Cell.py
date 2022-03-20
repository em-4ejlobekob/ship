import Field


class Cell(Field):
    def __init__(self, x, y):
        Field.__init__(self)
        self.project_name = self.project_name
        """
        status: 
        0 - клетка свободна 
        1 - рядом с клеткой корабль
        2 - рядом с клеткой два корабля
        3 - на клетке корабль
        4 - на клетке уничтоженный корабль
        """

        self.x = x
        self.y = y
        self.status = 0

    def draw(self):
        self.project_name

