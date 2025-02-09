from window import Window
from objects import Point, Line
from cell import Cell

def main():
    win = Window(800,600)

    # line1 = Line(Point(50, 50), Point(100,100))
    # line2 = Line(Point(300, 100), Point(700, 500))
    # line3 = Line(Point(100, 500), Point(600, 50))

    # win.draw_line(line1, color="black")
    # win.draw_line(line2, color="red")
    # win.draw_line(line3, color="blue")

    cell1 = Cell(50, 50, 100, 100, win)
    cell2 = Cell(100, 50, 150, 100, win)
    cell3 = Cell(100, 100, 150, 150, win)
    
    cell1.draw()
    cell2.draw()
    cell3.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell3)

    win.wait_for_close()

if __name__ == "__main__":
    main()