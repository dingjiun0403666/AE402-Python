import turtle
a=1
dg=turtle.Turtle()
screentitle=turtle.Screen()
screentitle.title("666")
dg.shape("turtle")
dg.color("yellow")
long=10
dg.speed(0)
while a==1:
    dg.forward(long)
    dg.right(90)
    long+=0.9
    dg.color("gold")
    dg.forward(long)
    dg.left(-75)
    dg.color("silver")
    long+=0.45
