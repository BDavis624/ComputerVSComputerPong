import turtle

#I'm trying to create some basic screen parameters here.
screen = turtle.Screen()
screen.title("One Pong to Rule Them All")
screen.bgcolor("green")
screen.bgpic('mordor3.png')
screen.setup(width=1068, height=600)

#I'll now create a left paddle.
turtle.addshape("gondor3.gif")
Gondor = turtle.Turtle()
Gondor.speed(0)
Gondor.shape("gondor3.gif")
Gondor.shapesize(stretch_wid=6, stretch_len=2)
Gondor.penup()
Gondor.goto(-500, 0)

#And now for the right paddle.
turtle.addshape("sauron3.gif")
Mordor = turtle.Turtle()
Mordor.speed(0)
Mordor.shape("sauron3.gif")
Mordor.shapesize(stretch_wid=5, stretch_len=1)
Mordor.penup()
Mordor.goto(500, 0)

#I'm attempting to create a ball here.
turtle.addshape("onering4.gif")
ring = turtle.Turtle()
ring.speed(0)
ring.shape("onering4.gif")
ring.shapesize(stretch_wid=1,stretch_len=1)
ring.penup()
ring.goto(0,0)
ring.dx = 2
ring.dy = -2

def moveGondorUp():
    y = Gondor.ycor() #Getting the current y-coordinated of the left paddle
    y += 15
    Gondor.sety(y) #Updating the y-coordinated of the paddle

def moveGondorDown():
    y = Gondor.ycor()
    y -= 15
    Gondor.sety(y)

def moveMordorUp():
    y = Mordor.ycor()
    y += 15
    Mordor.sety(y)

def moveMordorDown():
   y = Mordor.ycor()
   y -= 15
   Mordor.sety(y)

#Trying to create some rudimentary computer control. I found some resources on YouTube that were helpful for this.
if Gondor.ycor() < ring.ycor() and abs(Gondor.ycor() - ring.ycor()) > 10:
    moveGondorUp()

elif Gondor.ycor() > ring.ycor() and abs(Gondor.ycor() - ring.ycor()) > 10:
    moveGondorDown()

if Mordor.ycor() < ring.ycor() and abs(Mordor.ycor() - ring.ycor()) > 10:
    moveMordorUp()

elif Mordor.ycor() > ring.ycor() and abs(Mordor.ycor() - ring.ycor()) > 10:
    moveMordorDown()

#Setting up the actual game.
while True:
    screen.update()

    #Updating ball coordinates.
    ring.setx(ring.xcor()+ring.dx)
    ring.sety(ring.ycor()+ring.dy)   

    if Gondor.ycor() < ring.ycor() and abs(Gondor.ycor() - ring.ycor()) > 10:
        moveGondorUp()

    elif Gondor.ycor() > ring.ycor() and abs(Gondor.ycor() - ring.ycor()) > 10:
        moveGondorDown()

    if Mordor.ycor() < ring.ycor() and abs(Mordor.ycor() - ring.ycor()) > 10:
        moveMordorUp()

    elif Mordor.ycor() > ring.ycor() and abs(Mordor.ycor() - ring.ycor()) > 10:
        moveMordorDown()

#I had to find a good tutorial for this next bit, where I get the ball to bounce.
    if ring.ycor() > 280:
     ring.sety(280)
     ring.dy *= -1

    if ring.ycor() < -280:
        ring.sety(-280)
        ring.dy *= -1

    if (ring.xcor() < -460 and ring.xcor() > -470) and (Gondor.ycor() + 50 > ring.ycor() > Gondor.ycor() - 50):
         ring.dx *=-1

    if (ring.xcor() > 460 and ring.xcor() < 470) and (Mordor.ycor() + 50 > ring.ycor() > Mordor.ycor() - 50):
        ring.dx *=-1
