# Turtle Draw 
# By: Gavin Schnowske

from tkinter import *
import turtle as t
import math 
johnTurt = t.Turtle()

print('Welcome to Turtle Draw.')

print('Enter filename.')
user_int = input()
print(user_int)

turtleScreen = t.Screen()
turtleScreen.setup(450, 450)

johnTurt.speed(0)
johnTurt.penup()

print('Reading ' + user_int + ' file...')
turtleData = open(user_int, 'r')
line = turtleData.readline()

total_distance = 0

while line: 
    print(line, end='')
    lineSegment = line.split(' ')

    if (len(lineSegment) == 3):
        color = lineSegment[0]
        x = int(lineSegment[1])
        y = int(lineSegment[2])

        if johnTurt.isdown():  
            distance = math.sqrt((johnTurt.xcor() - x) ** 2 + (johnTurt.ycor() - y) ** 2)
            total_distance += distance

        johnTurt.color(color)
        johnTurt.goto(x, y)
        johnTurt.pendown()

    elif (len(lineSegment) == 1):
        johnTurt.penup()

    line = turtleData.readline()

johnTurt.penup()
johnTurt.goto(180, -180)
johnTurt.write(f'Total Distance: {total_distance:.2f}', align='right')

t.done()
turtleData.close()
print('\nDone!')
