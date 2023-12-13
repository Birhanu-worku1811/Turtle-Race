import random
from turtle import Turtle, Screen


screen = Screen()

is_race_on =False
screen.setup(500, 400)
user_bet = screen.textinput("make your bet", "which turtle will win the race: ")
colors = ["red", "orange", "yellow", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"you have won the {winner_color} turtle is the winner")
            else:
                print(f"you lost! the {winner_color} won ")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
