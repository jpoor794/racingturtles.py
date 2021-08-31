import turtle
import random
wn = turtle.Screen()
wn.bgcolor('lightblue')

lance = turtle.Turtle()
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

import random
N = 60
for i in range(N):
    x = random.randrange(1,10)
    andy.forward(x)
    x = random.randrange(1,10)
    lance.forward(x)

wn.exitonclick()
