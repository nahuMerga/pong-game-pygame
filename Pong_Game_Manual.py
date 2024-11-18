import turtle
import winsound
 
wn = turtle.getscreen()
wn.title('Pong Game Manual')
wn.bgpic("bag3.gif")
wn.setup(width=1360, height=750)
winsound.PlaySound("song2.wav", winsound.SND_ASYNC)
wn.tracer(0) 


while True:
	wn.update()
	#pen
	pen = turtle.Turtle()
	pen.speed(45)
	pen.color("black")
	pen.penup()
	pen.hideturtle()
	pen.goto(-12, 250) 
	pen.write("ABOUT", align="center", font=("calibri", 50, "normal"))
	pen.goto(-500, 200)
	pen.write("The folowing game is made by NAHOM MERGA", font=("calibri", 36, "normal"))
	pen.goto(-450, -210)
	pen.write("----Developed by python programing language----", font=("calibri", 36, "normal")) 
	pen.goto(-190, 130)
	pen.write("HOW TO PLAY", font=("calibri", 50, "normal"))
	pen.goto(-650, 50)
	pen.write("==> The first player use W and S to move the 1st paddle upward and downward \n  inorder to block  the ball from colliding it's own to the wall.", font=("calibri", 28, "normal"))
	pen.goto(-650, -40)
	pen.write("==>The second player use uparrow and downarrow to move the 2nd paddle upward \n and downward inorder  to block the ball from colliding it's own to the wall.", font=("calibri", 28, "normal"))
	pen.goto(-650, -80)
	pen.write("==> The game is all about preventing the ball from colliding to the player's wall", font=("calibri", 28, "normal"))
	pen.goto(-650, -120) 
	pen.write("==> The wall will be highlighted red when the player unable to protect it's wall", font=("calibri", 28, "normal"))
	pen.goto(-210, -280)
	pen.write("NAHOM MERGA", font=("calibri", 50,"normal"))
	pen.goto(-600, -330)
	pen.write("WARNING: Make sure capslock is off", font=("calibri", 36,"normal"))
      
