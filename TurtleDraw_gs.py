# Turtle Draw 
# By: Gavin Schnowske

import turtle as t

johnTurt = t.Turtle()
TURTLEDRAWTEXTFILENAME = 'turtleData.txt'

print('Turtle Draw')

print('Enter filename.')
user_int = input()
print(user_int)

turtleScreen = t.Screen()
turtleScreen.setup(450, 450)

johnTurt.speed(10)
johnTurt.penup()

print('Reading ' + user_int + ' file...')
turtleData = open(TURTLEDRAWTEXTFILENAME, 'r')
line = turtleData.readline()
while line: 
    print(line, end='')
    lineSegment = line.split(' ')

if (len(lineSegment) == 3):
    color = lineSegment[0]
    x = int(lineSegment[1])
    y = int(lineSegment[2])

    johnTurt.color(color)
    johnTurt.goto(x,y)
    johnTurt.pendown()

    if (len(lineSegment) == 1):
        johnTurt.penup()

        line = turtleData.readline()

t.done()
turtleData.close()
print('\nDone!')
