import turtle             
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
my_pen.speed(20)
 
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)
