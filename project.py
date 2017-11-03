#leland zheng
import turtle
turtle.colormode(255)
turtle.bgcolor("black")
bob= turtle.Turtle()
bob.speed(100)
bob.width(3)

#c = (r,b,g)
for times in range(150):
    c = (times, times,255)
    bob.color(c)#c is the variable
    bob.circle(times)
    bob.right(200)
    bob.forward(5)

bob.penup()
bob.goto(-325,250)

bob.pendown()

for times in range(256):
    
    c = (255-times,255-times,255)#loop variable in value of r
    bob.color(c)#c is the variable
    bob.forward(300-times)#loop variable value to forward
    bob.right(790)

bob.penup()
bob.goto(600,435)

bob.pendown()
      
for times in range(256):
    c = (255-times,255-times,255)#loop variable in value of r
    bob.color(c)#c is the variable
    bob.forward(300-times)#loop variable value to forward
    bob.right(790)

bob.penup()
bob.goto(800,675)

bob.pendown()

