import turtle
a=1
dg=turtle.Turtle()
screentitle=turtle.Screen()
screentitle.title("666")
dg.shape("turtle")
dg.color("yellow")
dg.penup()
dg.speed(0)
for i in range(0,100,5):
    dg.forward(30+i)
    dg.color("gold")
    dg.right(30)
    dg.stamp()
    dg.color("silver")
    dg.forward(30+i)
    dg.right(30)
    dg.stamp()