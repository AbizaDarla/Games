from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def starting_position():
    y_coord = 0
    colour_idx = 0
    turtles = []
    for x in range(1, 7):
        turt = Turtle()
        turt.shape("turtle")
        turt.color(colors[colour_idx])
        turt.penup()
        turt.setx(-350)
        turt.sety(y_coord)
        colour_idx += 1
        if x % 2 == 0:
            y_coord += 30 * x
        else:
            y_coord -= 30 * x
        turtles.append(turt)
    return turtles


def race(turtles):
    x_pos = -350
    while x_pos < 300:
        screen.tracer(1)
        for t in turtles:
            t.speed(random.randint(0,10))
            t.forward(random.randint(1,10))
            x_pos = t.xcor()
        screen.update()
        end_pos = []
        for turt in turtles:
            end_pos.append(turt.xcor())

    return end_pos

def winner(end_positions):
    winner_coordinate = max(end_positions)
    winner_coordinate_indx = end_positions.index(winner_coordinate)
    winner_color = colors[winner_coordinate_indx]
    return winner_color

def player_bet_check(player_bet, win_color):
    if player_bet == win_color:
        print(f"You won! The {win_color} turtle did win!!")
    else:
        print(f"Sorry, you've lost :( The {win_color} turtle won")

screen = Screen()
turtles = starting_position()
player_bet = screen.textinput("Player Bet", "Which color will win?\nOptions: red, orange, yellow, green, blue, purple")
end_positions = race(turtles)
win_color = winner(end_positions)
player_bet_check(player_bet, win_color)
screen.exitonclick()
