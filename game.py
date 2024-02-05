import os
import  random
import  turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor('black')
turtle.hideturtle()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __int__(self,spriteShape,color,startx,starty):
        turtle.Turtle.__init__(self,shape=spriteShape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx,starty)

        self.speed=1
player=Sprite("triagle","White",0,0)





#turtle.delay(delay=row_input('press enter  '))
turtle.done()
#delay=row_input("press enter to finish ")