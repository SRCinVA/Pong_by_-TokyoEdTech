import turtle

wn = turtle.Screen() #creates a window
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stops the window from updating

#Paddle A
paddle_a = turtle.Turtle() #Capital letter for the class name
paddle_a.speed(0) # the speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # means "no drawing when moving"
paddle_a.goto(-350, 0) #0 in the middle, then -350 and +350 on both sides.

#Paddle B
paddle_b = turtle.Turtle()  # Capital letter for the class name
paddle_b.speed(0)  # the speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # means "no drawing when moving"
paddle_b.goto(350, 0)  # 0 in the middle, then -350 and +350 on both sides.

#Ball
ball = turtle.Turtle()  # Capital letter for the class name
ball.speed(0)  # the speed of animation
ball.shape("square")
ball.color("white")
ball.penup()  # means "no drawing when moving"
ball.goto(0, 0)  # 0 in the middle, then -350 and +350 on both sides.
ball.dx = 2 #delta x method
ball.dy = -2 #delta y method

#Functions
def paddle_a_up():
    y = paddle_a.ycor() #.ycor method from turtle
    y += 20
    paddle_a.sety(y) #.sety to the new y

def paddle_a_down():
    y = paddle_a.ycor()  # .ycor method from turtle
    y -= 20
    paddle_a.sety(y)  # .sety to the new y


def paddle_b_up():
    y = paddle_b.ycor()  # .ycor method from turtle
    y += 20
    paddle_b.sety(y)  # .sety to the new y


def paddle_b_down():
    y = paddle_b.ycor()  # .ycor method from turtle
    y -= 20
    paddle_b.sety(y)  # .sety to the new y

#Keyboard binding
wn.listen() #sets up listener
wn.onkeypress(paddle_a_up, "w") #when user presses lower case w, call def paddle_a_up
# when user presses lower case w, call def paddle_a_up
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")

wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update() #every time it runs, it updates the screen

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    #window height was 600 in total
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverses direction

    if ball.xcor() > 390:
        ball.goto(0,0) #after falling off screen, reappears at 0,0.
        ball.dx *= -1