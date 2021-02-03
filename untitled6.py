import turtle
L=int(input("邊長?"))
邊=int(input("幾邊?"))
dg=turtle.Turtle()
dg.shape("turtle")
dg.speed(0)
h=int(360/邊)
while 邊==邊:
    dg.forward(L)
    dg.left(h)
    邊+=150