import turtle
import random

#main turtle
turtle_screen=turtle.Screen()
turtle_screen.title("Catch the Turtle")
turtle_screen.bgcolor("white")

#time turtle
pen=turtle.Turtle()
pen.hideturtle()
pen.up()
pen.speed(0)
pen.goto(x=0,y=350)

#screen turtle
turtle_on_screen=turtle.Turtle()
turtle_on_screen.shape("turtle")
turtle_on_screen.shapesize(3)
turtle_on_screen.speed(1)
turtle_on_screen.penup()

#score turtle
score_screen=turtle.Turtle()
score_screen.hideturtle()
score_screen.penup()
score_screen.goto(x=0,y=320)


countdown=20
score=0
game_over=False

def counter():
    global countdown,game_over
    pen.clear()
    if countdown>0:
        pen.write(f"Timer:{countdown}", align="center", font=("Arial", 30, "bold"))
        countdown-=1
        turtle_screen.ontimer(counter, 1000)
    else:
        pen.write("Time's up!", align="center", font=("Arial", 30, "bold"))
        game_over=True
        turtle_on_screen.hideturtle()


def move_randomly():
    global game_over
    if game_over:
        return
    turtle_on_screen.hideturtle()
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    turtle_on_screen.goto(x,y)
    turtle_screen.ontimer(turtle_on_screen.showturtle, 200)
    turtle_screen.ontimer(move_randomly,700)


def score_clicking(x,y):
    global score
    score+=1
    score_screen.clear()
    score_screen.write(f"Score:{score}",align="center", font=("Arial", 20, "bold"))

counter()
turtle_on_screen.onclick(score_clicking)
move_randomly()

turtle.mainloop()
