# Draw the Belgian and Japanese flag
from turtle import *

color("black")
up()

flag_size = (150, 100)
belgium_position = (-200, 0)
japan_position = (50, 0)
goto(belgium_position[0], belgium_position[1])

# draw belgium flag
belgium_colors = ("black", "yellow", "red")
belgium_stripes_size = (flag_size[0] / len(belgium_colors), flag_size[1])
down()
for color in belgium_colors:
    # fill the rectangle
    fillcolor(color)
    begin_fill()
    # draw the rectangle
    for i in range(0, 4):
        forward(belgium_stripes_size[i % 2])
        left(90)

    end_fill()
    # move to next stripe
    forward(belgium_stripes_size[0])
up()

# move to second flag
goto(japan_position[0], japan_position[1])

# draw japan flag
# draw the rectangle
down()
for i in range(0, 4):
    forward(flag_size[i % 2])
    left(90)
up()

# draw the circle
# 55px diameter
japan_circle_diameter = 55
goto(
    japan_position[0] + flag_size[0] / 2,
    japan_position[1] + flag_size[1] / 2
)
dot(japan_circle_diameter, "red")

# don't close the window unless closed by the user
mainloop()