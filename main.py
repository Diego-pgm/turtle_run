from turtle import Turtle, Screen, textinput
from random import randint


screen = Screen()
user_bet = textinput("Bet", "Which color will win?")
screen.screensize(500, 300)
x_list = [ x for x in range(-100, 110, 20)]
initial_positions = [ (-450, x) for x in x_list]
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "pink", "goldenrod", "magenta", "violet", "DarkOliveGreen"]
turtles = []
for position in range(0,11):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[position])
    new_turtle.shapesize(1)
    new_turtle.penup()
    new_turtle.goto(initial_positions[position])
    turtles.append(new_turtle)



game_on = True
while game_on:
    for turtle in turtles:
        turtle.forward(randint(1,10))
        if turtle.xcor() >= 460:
            winner = turtle.pencolor()
            if user_bet == winner:
                print("You win!") 
            print(f"The winner is: {winner}")
            game_on = False       


screen.exitonclick()