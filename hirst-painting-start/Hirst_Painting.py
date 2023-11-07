# import colorgram
import turtle as t
from turtle import Screen, Turtle
import random

timmy = Turtle()
t.colormode(255)

"""Extracting the color from the Image."""
# pic_colors = colorgram.extract('hirst-painting-start\Hirst.jpg', 25)
# print(pic_colors)

# color_list = []
# for color in pic_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r,g,b))
# print(color_list)

color_list = [(213, 211, 210), (207, 215, 210), (199, 163, 119), (216, 209, 212), (210, 213, 218), (165, 187, 163), (38, 95, 116), (125, 38, 29), (51, 35, 34), (156, 77, 55), (114, 73, 82), (119, 163, 174), (196, 99, 73), (49, 130, 103), (126, 34, 42), (18, 56, 42), (215, 197, 121), (7, 65, 84), (102, 149, 73), (186, 152, 156), (78, 35, 38), (216, 158, 29), (176, 202, 180), (19, 80, 97), (218, 180, 171)]
timmy.hideturtle()
timmy.penup()

timmy.setheading(225)
timmy.forward(300)



timmy.speed("fastest")

timmy.setheading(0)
number_of_counts = 100

for Current_count in range(1, number_of_counts + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    
    if Current_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)




screen = Screen()
screen.exitonclick()