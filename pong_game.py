# my pong game
import turtle
import winsound
import tkinter as tk
from tkinter import messagebox


wn = turtle.Screen()
wn.title("Pong game")
#
wn.setup(width=1360, height=750)
wn.tracer(0)
wn.bgpic("bag1.gif")
winsound.PlaySound("song.wav", winsound.SND_ASYNC)


# welcome screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(-500, 50)
pen.write("      This Game Is Made By:", font=("Perpetua Titling MT", 56, "normal"))
pen.goto(-450, -90)
pen.write("      Nahom Merga", font=("Old English Text MT", 96, "normal"))
user = wn.numinput("NAHOM", "Enter Your speed:", minval=1, maxval=10)
wn.clear()

wn = turtle.Screen()
wn.title("Pong game")
wn.bgpic("bag2.gif")
wn.setup(width=830, height=640)
wn.tracer(0)


# text
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 315)
pen.write("NAHOM MERGA", align="center", font=("Courier", 46, "normal"))



# Score
score_a = 0
score_b = 0


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#6600FF")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#FF6600")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)



# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player_A: 0        Player_B: 0", align="center", font=("Courier", 26, "normal"))

# line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=31, stretch_len=0.4)
line.penup()
line.goto(0, 0)

# stadium
stadium = turtle.Turtle()
stadium.end_fill()
stadium.speed(0)
stadium.shape("square")
stadium.color("black")
stadium.shapesize(stretch_wid=40, stretch_len=1)
stadium.penup()
stadium.goto(397, 0)

# stadium
stadium2 = turtle.Turtle()
stadium2.end_fill()
stadium2.speed(0)
stadium2.shape("square")
stadium2.color("black")
stadium2.shapesize(stretch_wid=40, stretch_len=1)
stadium2.penup()
stadium2.goto(-405, 0)

# stadium
stadium3 = turtle.Turtle()
stadium3.end_fill()
stadium3.speed(0)
stadium3.shape("square")
stadium3.color("black")
stadium3.shapesize(stretch_wid=1, stretch_len=40)
stadium3.penup()
stadium3.goto(0, 320)

# stadium
stadium4 = turtle.Turtle()
stadium4.end_fill()
stadium4.speed(0)
stadium4.shape("square")
stadium4.color("black")
stadium4.shapesize(stretch_wid=1, stretch_len=40)
stadium4.penup()
stadium4.goto(0, -310)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.goto(0, 0)
ball.shape("circle")
ball.color("#CCFF00")
ball.shapesize(stretch_wid=1.6, stretch_len=1.6)
ball.penup()
ball.dx = user
ball.dy = (-1*user)

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 92
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 92
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 92
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 92
    paddle_b.sety(y)

def paddle_sound():
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


# message box
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
            pass


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_sound, "c")


# main game loop
while True:
    wn.update()


    # Keyboard binding
    wn.listen()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1





    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1






    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        stadium.color("red")
        pen.write("Player_A: {}   Player_B: {}".format(score_a, score_b), align="center", font=("Courier", 26, "normal"))
        #winsound.PlaySound("ele.wav", winsound.SND_ASYNC)




    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        stadium2.color("red")
        pen.write("Player_A: {}   Player_B: {}".format(score_a, score_b), align="center", font=("Courier", 26, "normal"))
        #winsound.PlaySound("ele.wav", winsound.SND_ASYNC)




    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        stadium.color("black")



    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1
        stadium2.color("black")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)



    # ending the game
    if score_a >= 10:
        message_box('NAHOM', 'Player A WIN !!!')
        break

    if score_b >= 10:
        message_box('NAHOM', 'Player B WIN !!!')
        break
