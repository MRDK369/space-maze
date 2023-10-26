import turtle

rocket=turtle.Turtle()
space=turtle.Screen()

space.bgpic("back.gif")
space.addshape("spacceup.gif")
spaceman=turtle.Turtle()
spaceman.shape("spacceup.gif")
spaceman.penup()
spaceman.goto(-103,255)


space.addshape("down.gif")
space.addshape("left.gif")
space.addshape("right.gif")


space.addshape("rocket.gif")

rocket.shape("rocket.gif")
rocket.penup()
rocket.goto(180,-250)
rocket.speed(1000)
def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape("rocket.gif")
def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape("down.gif")
def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape("left.gif")
def right():
    rocket.forward(10)
    rocket.shape("right.gif")


turtle.listen()
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")





if rocket.distance(spaceman) < 10 :
    rocket.write("you win")
turtle.done()

