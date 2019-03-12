from turtle import Turtle

def drawPolygon(t, vertices):
    """Draws a polygon from a list of vertices.
    The list has the form [(x1, y1), ..., (xn, yn)]."""
    t.up()
    (x, y) = vertices[-1]
    t.goto(x, y)
    t.down()
    for (x, y) in vertices:
        t.goto(x, y)

def main():
    t = Turtle()
    t.hideturtle()
    drawPolygon(t, [(20, 20), (-20, 20), (-20, -20)])

main()
