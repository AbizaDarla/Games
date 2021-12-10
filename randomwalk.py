"""Random Walk Program"""

from turtle import Turtle, Screen, Shape
import random

miss_turtle = Turtle()
#miss_turtle.shape("circle")
miss_turtle.pensize(10)
miss_turtle.speed(15)
#miss_turtle.color(0.255, 0, 1)

directions = ['forward', 'backward']

angle_side = ['right', 'left']

angle_number = [0, 90, 180, 270]

#get color
def get_directions_angle(directions, angle_side, angle_number):
    return random.choice(directions), random.choice(angle_side), random.choice(angle_number)


def random_walk(miss_turtle):
    direction, side, angle = get_directions_angle(directions, angle_side, angle_number)
    miss_turtle.color(random.random(), random.random(), random.random())
    if side == 'right':
        miss_turtle.right(angle)
    elif side == 'left':
        miss_turtle.left(angle)
    if direction == 'forward':
        miss_turtle.forward(30)
    elif direction == 'backward':
        miss_turtle.backward(30)



for i in range(300):
    random_walk(miss_turtle)
#miss_turtle.circle(100)



screen = Screen()
screen.exitonclick()