from turtle import *
from random import randint

speed(0)

# For Branch
def draw_branch(len):
    
    if(len > 5):
        color("brown")
        forward(len)
        right(25 )
        draw_branch(len - randint(4,10))
        left(50)
        draw_branch(len - randint(4,10))
        right(25)
        color("brown")
        backward(len)
    else:
        color("green", "green")
        begin_fill()
        circle(10+ randint(0,5))
        end_fill()
        
# For Tree
def draw_tree(start_len):
    pendown()
    setheading(90)
    color("brown")
    pensize(5)
    draw_branch(start_len)
 

penup()
goto(-100, -200)
# Random shape of tree
draw_tree(randint(40, 60))
penup()
goto(100, -180)
draw_tree(randint(30, 40))
