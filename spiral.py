import turtle

def spiral():
    t = turtle.Turtle()
    for i in range(1000):
        t.forward(i * 5)
        t.right(144)

spiral()
turtle.done()
