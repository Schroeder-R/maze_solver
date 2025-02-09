from window import Window
from objects import Point, Line

class Cell():
    def __init__(self, x1, y1, x2, y2, win):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, color="black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, color="black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, color="black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, color="black")
    
    def draw_move(self, to_cell, undo=False):
        # Calculate the center coordinates of the current cell
        x1_center = (self._x1 + self._x2) / 2
        y1_center = (self._y1 + self._y2) / 2

        # Calculate the center coordinates of the to_cell
        x2_center = (to_cell._x1 + to_cell._x2) / 2
        y2_center = (to_cell._y1 + to_cell._y2) / 2

        # Create a line from the center of the current cell to the center of to_cell
        line = Line(Point(x1_center, y1_center), Point(x2_center, y2_center))

        # Set the color based on the undo flag
        color = "gray" if undo else "red"

        # Draw the line
        self._win.draw_line(line, color=color)



    