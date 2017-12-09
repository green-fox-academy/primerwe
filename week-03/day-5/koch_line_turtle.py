import turtle
PROGNAME = 'Koch-line'
import random

rand_color = str('#%06X' % random.randint(0,256**3-1))
turtle.bgcolor(rand_color)
t = turtle.Turtle()
t.ht()
t.speed(30)
t.pencolor('black')
t.pensize(2)

def koch(t, order, size):
    if order == 0:   
        t.forward(size)
    else:
        koch(t, order-1, size/3)  
        t.left(60)
        koch(t, order-1, size/3)
        t.left(-120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        
t.penup()
t.backward(300)
t.pendown()      
koch(t, 5, 1000)
turtle.mainloop()