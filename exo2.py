# Draw a chessboard
from turtle import *

color("black")
up()
speed(100)

square_size = 40
colors = ("white", "black")
chessboard_size = (8, 8)
start = (-220, 0)

def square(size: int, color: str):
    # fill the square with the desired color
    fillcolor(color)
    begin_fill()

    # draw the outline
    down()
    for _ in range(0, 4):
        forward(size)
        left(90)
    
    up()
    end_fill()

for i in range(0, chessboard_size[0]):
    for j in range(0, chessboard_size[1]):
        # go to the square bottom left point
        goto(
            start[0] + square_size * i,
            start[1] + square_size * j
        )

        # alternate the color
        color = colors[(j + i) % len(colors)]
        square(square_size, color)

# don't close the window unless closed by the user
mainloop()