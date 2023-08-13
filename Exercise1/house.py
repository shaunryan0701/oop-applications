class House:
    
    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return 2.5 * self.wall_area