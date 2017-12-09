import turtle
PROGNAME = 'Koch-snowflake'
import random

rand_color = str('#%06X' % random.randint(0,256**3-1))
turtle.bgcolor('#898989')
t = turtle.Turtle()
t.ht()
t.speed(30)
t.pencolor(rand_color)
t.pensize(2)

def koch(t, order, size):
    if order == 0:   
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)
            
def koch_snowflake(size, order):
    for step in range(3):
        koch(t, order-1, size/3)
        t.left(-120)
            
t.penup()
t.backward(150)
t.left(30)
t.pendown()

koch_snowflake(1800, 6)

turtle.mainloop()