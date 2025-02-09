from tkinter import Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1, point2):
        self.start_point = Point(point1.x, point1.y)
        self.end_point = Point(point2.x, point2.y)


    def draw(self, canvas, color, width):
        canvas.create_line(self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y, fill=color, width=width)


